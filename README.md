# TikTok Encryption Algorithms Implementation

## ⚠️ Legal Disclaimer

**This project is for educational purposes only. It should not be used for any illegal purposes or to violate terms of service.**

## 📋 Overview

This project contains implementations of encryption algorithms used by TikTok to generate required security headers for requests. The project includes implementations of the following algorithms:

- **x-argus**: Main signature algorithm
- **x-ladon**: Data encryption algorithm
- **x-gorgon**: Signature generation algorithm
- **x-khronos**: Timestamp
- **x-ss-req-ticket**: Request ticket
- **x-tt-trace-id**: Trace ID
- **x-ss-stub**: Data fingerprint

## 🏗️ Project Structure

```
TikTok-Encryption/
├── main.py                 # Flask API server
├── requirements.txt        # Python dependencies
├── signer/                 # Core signing modules
│   ├── __init__.py
│   ├── argus.py           # X-Argus algorithm implementation
│   ├── ladon.py           # X-Ladon algorithm implementation
│   ├── gorgon.py          # X-Gorgon algorithm implementation
│   └── lib/               # Supporting libraries
│       ├── ByteBuf.py     # Buffer management
│       ├── Simon.py       # Simon cipher implementation
│       ├── Sm3.py         # SM3 hash algorithm
│       ├── pkcs7_padding.py # PKCS7 padding utilities
│       └── protobuf.py    # Protocol Buffers implementation
```

## 🔧 Requirements

- Python 3.7+
- Flask 2.3.3
- pycryptodome 3.19.0

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/tr4cex/TikTok-Encryption.git
cd TikTok-Encryption
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python main.py
```

The server will run on `http://localhost:80`

## 🚀 Usage

### API Endpoint

**POST** `/sign`

### Request Body

```json
{
    "params": "device_id=123&version_name=1.0.0&...",
    "data": "request_body_data",
    "device_id": "123456789",
    "aid": 1233,
    "license_id": 1611921764,
    "sdk_version_str": "v04.04.05-ov-android",
    "sdk_version": 134744640,
    "platform": 0,
    "cookie": "session_cookie_data"
}
```

### Response

```json
{
    "success": true,
    "result": {
        "x-argus": "encoded_argus_signature",
        "x-ladon": "encoded_ladon_data",
        "x-gorgon": "gorgon_signature",
        "x-khronos": "1674223203",
        "x-ss-req-ticket": "1674223203123",
        "x-tt-trace-id": "00-trace-id-span-id-01",
        "x-ss-stub": "DATA_HASH"
    }
}
```

### Example using curl

```bash
curl -X POST http://localhost:80/sign \
  -H "Content-Type: application/json" \
  -d '{
    "params": "device_id=123456&version_name=1.0.0",
    "data": "test_data",
    "device_id": "123456"
  }'
```

### Python Example

You can run the included example:

```bash
python example.py
```

Or use the following code:

```python
import requests
import json

url = "http://localhost:80/sign"
data = {
    "params": "device_id=123456789&version_name=1.0.0",
    "data": "test_data",
    "device_id": "123456789"
}

response = requests.post(url, json=data)
result = response.json()
print(json.dumps(result, indent=2))
```

## 🔍 Algorithm Details

### X-Argus
- Uses Simon cipher and SM3 hashing
- Generates encrypted signature using AES-CBC
- Includes device and application information

### X-Ladon
- Custom encryption algorithm
- Uses MD5 hashing and PKCS7 padding
- Encrypts timestamp, license_id, and aid

### X-Gorgon
- Generates signature based on parameters, data, and cookies
- Uses MD5 hashing and bit manipulation
- Custom encryption algorithm with transformations

### Supporting Libraries
- **Simon Cipher**: Simon symmetric encryption algorithm implementation
- **SM3 Hash**: Chinese standard hash algorithm
- **ProtoBuf**: Protocol Buffers implementation for serialization
- **PKCS7 Padding**: Padding utilities for encryption

## 🧪 Testing

To test the project, make sure to run the server first:

```bash
python main.py
```

Then in another terminal, run the test file:

```bash
python example.py
```

## ⚙️ Configurable Parameters

- `aid`: Application ID (default: 1233)
- `license_id`: License identifier (default: 1611921764)
- `platform`: Platform type (0=Android, 1=iOS)
- `sdk_version_str`: SDK version string
- `sdk_version`: SDK version integer

## 🔒 Security

This project contains:
- Hardcoded encryption keys
- Custom encryption algorithms
- Sensitive data processing

**Reminder: Use this code responsibly and only for research and learning purposes**

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details

## ⚠️ Disclaimer

- This project is for educational and research purposes only
- Developers are not responsible for any illegal use
- Use at your own risk
- Respect TikTok's terms of service
