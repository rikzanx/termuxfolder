from datetime import datetime, timedelta
import requests
# Waktu awal
start_time = datetime.strptime("07:38:00", "%H:%M:%S")

# Waktu akhir
end_time = datetime.strptime("08:00:00", "%H:%M:%S")

# Selisih waktu awal dan waktu akhir
time_difference = end_time - start_time

# Loop untuk menampilkan waktu per detik
current_time = start_time
no = 1
while current_time <= end_time:
    url = "https://synergis.prosilum.web.id/sitedata/images/hadir/checkin/ARTN0000005201308154428605_2023-10-16_"
    time_str = current_time.strftime("%H:%M:%S")
    url_full = url+time_str+".jpg"
    print(no)
    no+=1
    try:
        response = requests.head(url_full)
        if response.status_code == 200:
            print(url_full)
            print("Link dapat diakses.")
    except Exception as e:
        print("")
    current_time += timedelta(seconds=1)
