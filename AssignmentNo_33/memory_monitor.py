import psutil

def MemoryCommand():
    process_list = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            process_list.append(
                (proc.info['name'], proc.info['memory_info'].rss)
            )
        except psutil.AccessDenied:
            pass

    process_list.sort(key=lambda x: x[1], reverse=True)

    print("Top 10 Memory Consuming Processes")
    for p in process_list[:10]:
        print("Process :", p[0], "RSS :", p[1])