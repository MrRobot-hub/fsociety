import os


def create_dir():
    dir_path = os.getcwd()
    if not os.path.exists(f"{dir_path}\\etc"):
        os.system("mkdir etc")
    if not os.path.exists(f"{dir_path}\\logs"):
        os.system("mkdir logs")
