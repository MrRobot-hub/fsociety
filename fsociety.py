"""
Author: Umer Farid
Youtube: Neo X. Coders
The Art Of Possible
"""
import os
import sys
import argparse
import logging
from utilities.logo import Logo
import platform
from utilities.utility import Check_arch
from utilities.check_dir import create_dir
from utilities.time import get_time
from utilities.time import get_date
from utilities.check_OS import Check_OS

check_os = Check_OS.OS()
path = os.getcwd()
#initialize time
current_time = get_time()
today_is = get_date()

# print logo
Logo.create_logo()
# create directories
create_dir()


# get arguments
parser = argparse.ArgumentParser(
    description="\nLearn programming by @NEO X. CODERS. You can learn any of programming languages from here. Just give a programming name or programming name with a particular topic as an argument to the file\n"
)
parser.add_argument(
    "-l",
    "--lang",
    metavar="",
    type=str,
    help="Mention the programming language name",
)
parser.add_argument(
    "-q",
    "--query",
    metavar="",
    type=str,
    help="Label query e.g loops, functions, external execute etc",
)
parser.add_argument(
    "-eg",
    "--examples",
    action="store_false",
    help="Examples of tool",
)
parser.add_argument(
    "-sl",
    "--savelogs",
    action="store_false",
    help="Save current logs into a file",
)
parser.add_argument(
    "-s",
    "--status",
    action="store_true",
    help="Status of current flags",
)
parser.add_argument(
    "-lg",
    "--logs",
    action="store_true",
    help="Display log file",
)
parser.add_argument(
    "-c",
    "--cmdinfo",
    metavar="",
    type=str,
    help="Display information/mannual of any UNIX/CMD command",
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-qt",
    "--quiet",
    action="store_true",
    help="Execute in quiet mode",
)

group.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Display output on screen as well as saved in a system",
)
args = parser.parse_args()

if check_os == "Windows":
    path_curl32 = "bin\\curl-win32\\bin\\curl.exe"
    path_curl64 = "bin\\curl-win64\\bin\\curl.exe"
    # get logs
    logging.basicConfig(
        filename="logs\\app.log",
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
)
    param = f"{path}\\logs\\app.log"
    python = "py"
    path_to_store_cmds = f"etc\\{today_is}-COMMAND-{args.cmdinfo}.txt"
    path_to_store_prgs = f"etc\\{today_is}-PROGRAMMING-{args.lang}.txt"
elif check_os == "Linux":
    path_curl32, path_curl64 = "curl"
    param = f"{path}/logs/app.log"
    path_to_store_cmds = f"etc/{today_is}-COMMAND-{args.cmdinfo}.txt"
    path_to_store_prgs = f"etc/{today_is}-PROGRAMMING-{args.lang}.txt"
    # get logs
    logging.basicConfig(
        filename="logs/app.log",
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
)

    python = "python"
else:
    print("Os not found, Please contact via gmail: \033[31mumerfarid53@gmail.com\033[0m")

def list_logs(param):
    
    if platform.system() == "Windows":
        os.system(f"type {param}")
    elif platform.system() == "Linux":
        os.system(f"cat {param}")
    else:
        print("Didn't recognize your operating system, upgrade to the latest version")


if len(sys.argv) < 2:

    fname = sys.argv[0]
    
    os.system(f"{python} fsociety.py --help")
    print(f"\n\033[31m{fname}: error: atleast one argument is required\033[0m")

elif sys.argv[1] == "-lg" or sys.argv[1] == "--logs":
    list_logs(args.logs)

elif sys.argv[1] == "-s" or sys.argv[1] == "--status":
    print("Data configurations: %s" % args)

elif sys.argv[1] == "-eg" or sys.argv[1] == "--examples":
    fname = sys.argv[0]
    dictionary = {
        "UNIX/CMD Mannual": f"python {fname} --cmdinfo cd",
        "Learn 0 to hero": f"python {fname} --lang java --query :learn --verbose",
        "Learn Python": f"python {fname} --lang python --verbose",
        "Learn Java": f"python {fname} --lang java --verbose",
        "Learn C++": f"python {fname} --lang C++ --verbose",
        "lang & Query": f"python {fname} --lang python --query loops --verbose",
        "lang & Query": f"python {fname} --lang java --query functions --verbose",
        "lang Query quiet": f"python {fname} --lang python --query loops --quiet",
        "show status": f"python {fname} --status",
        "show logs": f"python {fname} --logs",
    }
    for key, values in dictionary.items():
        print(f"{key:>16s} : {values}")

elif sys.argv[1] == "-c" or sys.argv[1] == "--cmdinfo":
    if args.quiet:
        os.system(f"curl cht.sh/{args.cmdinfo} > {path_to_store_cmds}")
        Logo.author()
        logging.info(args)
    elif args.verbose:
        os.system(f"curl cht.sh/{args.cmdinfo}")
        Logo.author()
        logging.info(args)

elif len(sys.argv) > 2:
    if args.quiet:
        print("Fetching Data..")
        os.system(f"curl cht.sh/{args.lang}/{args.query} > {path_to_store_prgs}")
        logging.info(args)
        Logo.author()
    elif args.verbose:
        parsed_data = Check_arch(path_curl32, path_curl64, args.lang, args.query)
        parsed_data.lang_query_curl()
        Logo.author()
        logging.info(args)
    else:
        os.system(f"{python} fsociety.py --help")
        print("\033[31mPlease select mode of execution -v or --verbose to display it on screen or -qt or --quiet to save in a file\033[0m")
        

logger = logging.getLogger("Neo X. Coders")

print("\033[33m",logger, "\033[0m")
