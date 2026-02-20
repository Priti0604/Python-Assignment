import psutil

def ThreadCommand():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print("Process Name :", proc.info['name'])
            print("PID :", proc.info['pid'])
            print("Thread Count :", proc.num_threads())
            print("-" * 40)
        except psutil.AccessDenied:
            print("Access Denied")