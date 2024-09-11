
# Free API

## Sign Endpoint

### Endpoint

`POST https://neutral-ladybug-desired.ngrok-free.app/sign`

### Description

This endpoint generates a signature and related information based on the provided data.

### Request

The request should be sent as a JSON object in the body of the POST request. The following parameters are supported:

- `params` (required, str): A string representing the parameters.
- `data` (optional, str): Request Payload.
- `device_id` (optional, str): Device ID.
- `aid` (optional, int): Application ID.
- `license_id` (optional, int): License ID.
- `sdk_version_str` (optional, str): SDK version string.
- `sdk_version` (optional, int): SDK version.
- `platform` (optional, int): Platform.
- `cookie` (optional, str): Cookie.

### Response

The API will respond with a JSON object containing the following keys:

- `success`: Indicates whether the request was successful.
- `result`: A dictionary containing the generated signatures and related information.

### Example

#### Request

```json
{
  "params": "param1=value1&param2=value2",
  "data": "request_payload",
  "device_id": "7268580072775517702",
  "aid": 1233,
  "license_id": 123456789,
  "sdk_version_str": "v1.2.3",
  "sdk_version": 123456789,
  "platform": 0,
  "cookie": "cookie1=value1&cookie2=value2"
}
```
#### Response

```json
{
  "success": true,
  "result": {
    "x-argus": "",
    "x-ladon": "",
    "x-gorgon": "",
    "x-khronos": "",
    "x-ss-req-ticket": "",
    "x-tt-trace-id": "",
    "x-ss-stub": ""
  }
}
```
