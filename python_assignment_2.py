import psutil

cpu_threshold = 80

print("Monitoring CPU usage...")
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > cpu_threshold:
            print("Alert! CPU usage exceeds threshold: " + str(cpu_usage) + "%")
except KeyboardInterrupt:
    print("Monitoring stopped.")
