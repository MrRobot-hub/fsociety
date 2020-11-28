"""
Author: Umer Farid
Youtube: Neo X. Coders
The Art Of Possible
"""
import os
import sys
import argparse
import logging
from pprint import pprint
from utilities.logo import Logo
import platform
from utilities.utility import Check_arch
from utilities.check_dir import create_dir

path_curl32 = "bin\\curl-win32\\bin\\curl.exe"
path_curl64 = "bin\\curl-win64\\bin\\curl.exe"
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


# get logs
logging.basicConfig(
    filename="logs\\app.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

"""
def lang_query_curl(language, query):
    os.system(f"curl cheat.sh/{language}/{query}")
"""


def list_logs(param):
    path = os.getcwd()
    param = f"{path}\\logs\\app.log"
    if platform.system() == "Windows":
        os.system(f"type {param}")
    elif platform.system() == "Linux":
        os.system(f"cat {param}")
    else:
        print("Didn't recognize your operating system, upgrade to the latest version")


args = parser.parse_args()

if len(sys.argv) < 2:

    fname = sys.argv[0]
    print(parser.description)
    print(f"usage: {fname} [-h] [-l] [-q] [-slogs] [-s] [-lg] [-qt | -v | -c]")
    print(f"{fname}: error: atleast one argument is required")
    print(f"{fname} -h or --help to list out decriptive args\n")

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
    os.system(f"curl cht.sh/{args.cmdinfo}")
    Logo.author()
    logging.info(args)

elif len(sys.argv) > 2:
    if args.quiet:
        print("Fetching Data..")
        os.system(f"curl cht.sh/{args.lang}/{args.query} > etc\\app.txt")
        logging.info(args)
        Logo.author()
    elif args.verbose:
        parsed_data = Check_arch(path_curl32, path_curl64, args.lang, args.query)
        parsed_data.lang_query_curl()
        Logo.author()
        logging.info(args)

logger = logging.getLogger("Neo X. Coders")

print(logger)
