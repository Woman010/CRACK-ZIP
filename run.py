from tqdm import tqdm
import zipfile
import sys, os
from colorama import Fore, Back, Style
import time

def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/30)

#banner = (Fore.WHITE+"\n       ∟ THANK YOU FOR USING MY SCRIPT!"+Fore.RED+" ▐")
banner1 = (Fore.WHITE+"\n       ∟ THANK YOU FOR USING MY SCRIPT!"+Fore.RED+" ▐"+Fore.RED+"\n")
t = ("\n")
# the password list path you want to use
wordlist = sys.argv[2]
# the zip file you want to crack its password
zip_file = sys.argv[1]
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
open_wordlist = len(list(open(wordlist, "rb")))
os.system("clear")
slowprints(banner1)
time.sleep(3)
os.system("clear")
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=open_wordlist, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
            os.system("clear")
        except:
            continue
        else:
            print(Fore.WHITE+"\n["+Fore.RED+"✔︎"+Fore.WHITE+"]"+Fore.RED+" รหัสผ่าน"+Fore.WHITE+" :"+Fore.RED+"", word.decode().strip())
            slowprints(banner1)
            exit(0)
print(Fore.WHITE+"\n["+Fore.RED+"!"+Fore.WHITE+"]"+Fore.RED+" ไม่มีรหัสผ่านที่ถูกต้อง!\n")
