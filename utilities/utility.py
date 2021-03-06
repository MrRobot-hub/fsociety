import platform, os


class Check_arch:
    def __init__(self, path_curl32, path_curl64, query_language, query):
        self.path_curl32 = path_curl32
        self.path_curl64 = path_curl64
        self.query_language = query_language
        self.query = query

    def lang_query_curl(self):
        # print(type(self.platfrm))
        if platform.machine().endswith("64"):
            if os.system(f"{self.path_curl64} cht.sh/{self.query_language}/{self.query}"):
                print("\033[31mMake sure you have a strong internet connection and try again!\033[0m")
                
            else:
                pass
        else:
            os.system(f"{self.path_curl32} cht.sh/{self.query_language}/{self.query}")
        return True
