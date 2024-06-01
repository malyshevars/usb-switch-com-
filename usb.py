import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import time

usb_device_path = '/sys/bus/usb/devices/1-4.1'

def disable_usb_device():
    try:
        subprocess.run(['sudo', 'sh', '-c', f'echo 0 > {usb_device_path}/authorized'], check=True)
        messagebox.showinfo("Информация", f"Устройство {usb_device_path} отключено.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Не удалось отключить устройство: {e}")

def enable_usb_device():
    try:
        subprocess.run(['sudo', 'sh', '-c', f'echo 1 > {usb_device_path}/authorized'], check=True)
        messagebox.showinfo("Информация", f"Устройство {usb_device_path} включено.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Не удалось включить устройство: {e}")

def disable_usb_device_after_delay(delay):
    time.sleep(delay)
    disable_usb_device()

def schedule_disable_usb():
    delay = 5 * 60  # 5 минут в секундах
    threading.Thread(target=disable_usb_device_after_delay, args=(delay,)).start()
    messagebox.showinfo("Информация", "Отключение устройства через 5 минут запланировано.")

root = tk.Tk()
root.title("Управление USB устройством")

btn_enable = tk.Button(root, text="Включить", command=enable_usb_device)
btn_enable.pack(pady=10)

btn_disable = tk.Button(root, text="Отключить", command=disable_usb_device)
btn_disable.pack(pady=10)

btn_schedule_disable = tk.Button(root, text="Отключить через 5 минут", command=schedule_disable_usb)
btn_schedule_disable.pack(pady=10)

root.mainloop()

#lsusb
#dmesg | grep usb
#sudo apt-get install python3-tk