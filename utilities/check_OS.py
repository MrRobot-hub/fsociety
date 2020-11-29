import platform
class Check_OS:
    def OS():
        check_os = platform.uname()[0]     
        return check_os

