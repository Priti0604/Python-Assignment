import shutil

def CreateArchive(DirName):
    shutil.make_archive(DirName, 'zip', DirName)