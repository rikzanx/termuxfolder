from datetime import datetime, timedelta

# Waktu awal
start_time = datetime.strptime("00:00:00", "%H:%M:%S")

# Waktu akhir
end_time = datetime.strptime("23:59:59", "%H:%M:%S")

# Selisih waktu awal dan waktu akhir
time_difference = end_time - start_time

# Loop untuk menampilkan waktu per detik
current_time = start_time
while current_time <= end_time:
    print(current_time.strftime("%H:%M:%S"))
    current_time += timedelta(seconds=1)
