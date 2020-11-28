import os, platform


class Logo:
    def create_logo():
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
        logo = """\033[32m
          █████▒ ██████  ▒█████   ▄████▄   ██▓▓█████▄▄▄█████▓▓██   ██▓
        ▓██   ▒▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▓█   ▀▓  ██▒ ▓▒ ▒██  ██▒
        ▒████ ░░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒▒███  ▒ ▓██░ ▒░  ▒██ ██░
        ░▓█▒  ░  ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░▒▓█  ▄░ ▓██▓ ░   ░ ▐██▓░
        ░▒█░   ▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░░▒████▒ ▒██▒ ░   ░ ██▒▓░
        \033[31m▒ ░   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓  ░░ ▒░ ░ ▒ ░░      ██▒▒▒ 
        ░     ░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░ ░ ░  ░   ░     ▓██ ░▒░ 
        ░ ░   ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░   ░    ░       ▒ ▒ ░░  
             ░      ░ ░  ░ ░       ░     ░  ░         ░ ░     
                         ░                            ░ ░      
                         }+{Developer :.: Umer Farid}+{
                         }+{Youtube :: Neo X. Coders}+{
                      }+{Gmail :: umerfarid53@gmail.com}+{ \033[0m
        """
        print(logo)

    def author():
        dict = {
            "Developer": "Umer Farid",
            "Youtube": "Neo X. Coders",
            "Language": "Python",
            "Age": 20,
        }

        for key, value in dict.items():
            print(f"{key:>16s} : {value}")
