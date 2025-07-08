from flask import Flask, request, jsonify
from signer import md5, ladon, argus, gorgon
from time import time
from random import choice
import json

app = Flask(__name__)

@app.route('/sign', methods=['POST'])
def sign_endpoint():
    try:
        request_data = request.json
        params = request_data.get('params')
        data = request_data.get('data', None)
        sec_device_id = request_data.get('device_id', '')
        aid = int(request_data.get('aid', 1233))
        license_id = int(request_data.get('license_id', 1611921764))
        sdk_version_str = request_data.get('sdk_version_str', 'v04.04.05-ov-android')
        sdk_version = int(request_data.get('sdk_version', 134744640))
        platform = int(request_data.get('platform', 0))
        cookie = request_data.get('cookie', '')

        x_ss_stub = md5(data.encode()).hexdigest() if data else None
        ticket = time()
        unix = int(ticket)
        trace = (
            str("%x" % (round(ticket * 1000) & 0xffffffff))
            + "10"
            + "".join(choice('0123456789abcdef') for _ in range(16))
            if not sec_device_id
            else hex(int(sec_device_id))[2:]
            + "".join(choice('0123456789abcdef') for _ in range(2))
            + "0"
            + hex(int(aid))[2:]
        )

        result = {
            'x-argus': argus.Argus.get_sign(
                params, x_ss_stub, unix,
                platform=platform,
                aid=aid,
                license_id=license_id,
                sec_device_id=sec_device_id,
                sdk_version=sdk_version_str,
                sdk_version_int=sdk_version
            ),
            'x-ladon': ladon.Ladon.encrypt(unix, license_id, aid),
            'x-gorgon': gorgon.get_xgorgon(
              params=params, ticket=ticket, data=data if data else "", cookie=cookie
            ),
            'x-khronos': str(unix),
            'x-ss-req-ticket': str(time()).replace(".", "")[:13],
            'x-tt-trace-id': f"00-{trace}-{trace[:16]}-01",
            'x-ss-stub': x_ss_stub.upper() if data else None
        }

        return json.dumps({'success': True, 'result': result},sort_keys=False), 200

    except Exception as e:
        return jsonify({'success': False}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)