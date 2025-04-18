import os
import time

# Fungsi untuk memeriksa status sistem
def check_system_status():
    # Mengecek penggunaan CPU
    cpu_usage = os.popen("top -bn1 | grep 'Cpu(s)'").read()
    print("Status CPU: ", cpu_usage)

    # Mengecek penggunaan memori
    memory_usage = os.popen("free -h").read()
    print("Status Memori: ", memory_usage)

# Fungsi untuk menjalankan tugas harian
def run_daily_tasks():
    print("Menjalankan tugas harian...")
    check_system_status()
    # Tambahkan tugas lain yang ingin dijalankan di sini

# Menjalankan tugas setiap 24 jam
while True:
    run_daily_tasks()
    time.sleep(86400)  # Tidur selama 24 jam (86400 detik)
