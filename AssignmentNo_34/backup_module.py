import os
import shutil
import time

def BackupData(SourceDir):
    if not os.path.exists(SourceDir):
        print("Source directory does not exist")
        return

    BackupDir = "Backup_" + time.strftime("%Y-%m-%d_%H-%M-%S")

    os.mkdir(BackupDir)
    print("Backup directory created :", BackupDir)

    for foldername, subfolders, filenames in os.walk(SourceDir):
        for file in filenames:
            src_path = os.path.join(foldername, file)
            dst_path = os.path.join(BackupDir, file)
            shutil.copy2(src_path, dst_path)

    print("Backup completed successfully")