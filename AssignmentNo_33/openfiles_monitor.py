import psutil

def OpenFilesCommand():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print("Process Name :", proc.info['name'])
            print("Open Files :", len(proc.open_files()))
            print("-" * 40)
        except psutil.AccessDenied:
            print("Access Denied")