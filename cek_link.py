import requests

url = "https://synergis.prosilum.web.id/sitedata/images/hadir/checkin/ARTN0000005201308154428605_2023-10-20_07:52:32.jpg"

response = requests.head(url)

if response.status_code == 200:
    print("Link dapat diakses.")
else:
    print("Link tidak dapat diakses. Status code:", response.status_code)
