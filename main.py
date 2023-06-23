import speedtest
import tkinter as tk

def measure_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert to megabits per second
    upload_speed = st.upload() / 1000000  # Convert to megabits per second

    return download_speed, upload_speed

def run_speed_test():
    download_speed, upload_speed = measure_internet_speed()
    download_label.config(text="Download Speed: {:.2f} Mbps".format(download_speed))
    upload_label.config(text="Upload Speed: {:.2f} Mbps".format(upload_speed))

# GUI setup
window = tk.Tk()
window.title("Internet Speed Test")

download_label = tk.Label(window, text="Download Speed: ")
download_label.pack(pady=10)

upload_label = tk.Label(window, text="Upload Speed: ")
upload_label.pack(pady=10)

run_test_button = tk.Button(window, text="Run Speed Test", command=run_speed_test)
run_test_button.pack(pady=10)

window.mainloop()
