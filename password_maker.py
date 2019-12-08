# Coded By Zed-Team
# Telegram : @Arch_TM
# Thank you for download
from os import system as cmd
try:
    from colorama import Fore,init
    init(autoreset=False)
except ModuleNotFoundError as e:
    print(e)
    cmd('pip install colorama')
    exit()
def main():
    print(Fore.WHITE+"*****Coded By Zed-Team*****")
    print(Fore.YELLOW+ "***Telegram : @Arch_TM***")
    try:
        start = int(input(Fore.LIGHTBLACK_EX +'\nPlease Enter Number 1 : '))
        end = int(input(Fore.LIGHTBLACK_EX +'Please Enter Number 2 (largger than number 1): '))
    except ValueError:
        print(Fore.RED +"Please Enter just number !!!")
        exit()
    from time import sleep
    i = 0
    while True:
        i +=1
        start = int(start)
        end = int(end)
        if start == end:
            print(Fore.YELLOW + "Finished ! \a")
            break
        elif start < end:            
            start += 1
            start = str(start)
            result = start + start
            print(Fore.GREEN + f"[{i}] : " +result)
            with open('passlist.txt','a') as af:
                af.write(result)
                af.write('\n')
        else:
            print(Fore.RED + "Error! Number 2 larger than number 1")
            exit()

if __name__ == "__main__":
    try:
        with open('passlist.txt','x'):
            pass
    except Exception:
        pass
    main()