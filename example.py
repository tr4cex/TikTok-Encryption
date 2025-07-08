import requests

response = requests.post(
	"http://localhost:80/sign",
	json={
		"params": "iid=7269719797901231877&device_id=7269718763266737669&ac=mobile&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300804&version_name=30.8.4&device_platform=android&os=android&ab_version=30.8.4&ssmix=a&device_type=SM-A500H&device_brand=Samsung&language=&os_api=26&os_version=8&openudid=92bfedf2f1dc0774&manifest_version_code=2023008040&resolution=1220%2A2712&dpi=387&update_version_code=2023008040&_rticket=1692613566176&app_type=normal&sys_region=PH&mcc_mnc=51501&timezone_name=Asia%5C%2FManila&carrier_region_v2=515&app_language=en&carrier_region=PH&ac2=lte&uoo=0&op_region=PH&timezone_offset=28800&build_number=30.8.4&host_abi=arm64-v8a&locale=en&region=PH&ts=1692613566&cdid=bb8b6f0a-f374-40a2-a493-8a7282fff873&support_webview=1&cronet_version=f022bf57_2023-08-01&ttnet_version=4.1.120.34-tiktok&use_store_region_cookie=1"
	}
).json()

print(response)