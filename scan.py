import socket , colorama , sys , os
from colorama import Fore , init
init()
def scan(target):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f'{Fore.LIGHTBLUE_EX}-' * 82)
    print("             _____  _____          _   _ _   _ _____ _   _  _____          ")  
    print("            / ____|/ ____|   /\   | \ | | \ | |_   _| \ | |/ ____|         ")
    print("   ______  | (___ | |       /  \  |  \| |  \| | | | |  \| | |  __   ______ ")
    print("  |______|  \___ \| |      / /\ \ | . ` | . ` | | | | . ` | | |_ | |______|")
    print("            ____) | |____ / ____ \| |\  | |\  |_| |_| |\  | |__| |         ")
    print("           |_____/ \_____/_/    \_\_| \_|_| \_|_____|_| \_|\_____|         ")                                                                                                                             
    print() 
    print(" Visit My Website: 'https://lukkshh.ga/' ")         
    print("-" * 82)
    print()
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"{Fore.LIGHTGREEN_EX}  [*] Port:{Fore.LIGHTYELLOW_EX} {port} {Fore.LIGHTGREEN_EX}is open ")
                s.close()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    except socket.error:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print()
        print(f"{Fore.LIGHTRED_EX}Unknown Host Or Host Not Responding, \nCheck Your IP: {target} ")
        sys.exit()
def help():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f'{Fore.LIGHTCYAN_EX}-' * 70)
    print("     ____            _     ____                                   ")
    print("    |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __  ")
    print("    | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ")
    print("    |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |    ")
    print("    |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|    ")
    print()        
    print("-" * 70)
    print()
    print()
    print(f"   {Fore.LIGHTGREEN_EX} ctrl+c {Fore.LIGHTCYAN_EX} - {Fore.LIGHTGREEN_EX} Stop Proccess Immediately ") 
    print()
    print(f"   {Fore.LIGHTGREEN_EX} --help {Fore.LIGHTCYAN_EX} - {Fore.LIGHTGREEN_EX} See List Of Functions")   
    print()
    print(f"   {Fore.LIGHTGREEN_EX}     -a {Fore.LIGHTCYAN_EX} - {Fore.LIGHTGREEN_EX} Scan All Ports")
    print()
    print(f"   {Fore.LIGHTGREEN_EX}     -p {Fore.LIGHTCYAN_EX} - {Fore.LIGHTGREEN_EX} Scan Specified Ports [Faster]")
    print()
    print()
    print()
    print(f"{Fore.LIGHTCYAN_EX}-" * 70)
def advanced_scan(target):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f'{Fore.LIGHTBLUE_EX}-' * 82)
    print("             _____  _____          _   _ _   _ _____ _   _  _____          ")  
    print("            / ____|/ ____|   /\   | \ | | \ | |_   _| \ | |/ ____|         ")
    print("   ______  | (___ | |       /  \  |  \| |  \| | | | |  \| | |  __   ______ ")
    print("  |______|  \___ \| |      / /\ \ | . ` | . ` | | | | . ` | | |_ | |______|")
    print("            ____) | |____ / ____ \| |\  | |\  |_| |_| |\  | |__| |         ")
    print("           |_____/ \_____/_/    \_\_| \_|_| \_|_____|_| \_|\_____|         ")                                                                                                                                          
    print()
    print("   Visit My Website: 'https://lukkshh.ga/' ")          
    print("-" * 82)
    print(f"{Fore.LIGHTYELLOW_EX}")
    try:
        port = input(" Target Port >>> ")
        print()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear') 
        sys.exit()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result = s.connect_ex((target,int(port)))
    if result == 0:
        print(f"{Fore.LIGHTGREEN_EX} [*] Port:{Fore.LIGHTYELLOW_EX} {port} {Fore.LIGHTGREEN_EX}is open ")
        s.close()
    else:
        print(f"{Fore.LIGHTRED_EX}")
        print("  Port Is Not Open")
def main():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f'{Fore.LIGHTBLUE_EX}-' * 70)
    print("  ____            _     ____                                   ")
    print(" |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __  ")
    print(" | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ")
    print(" |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |    ")
    print(" |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|    ")
    print()        
    print("-" * 70)
    print(" Visit My Website: 'https://lukkshh.ga/' ")                                               
    try:
        print(f"{Fore.LIGHTYELLOW_EX}")
        target = input(str(" Target IP >>> "))
        scan(target)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear') 
        sys.exit()
if len(sys.argv) == 2:
    if sys.argv[1] == '--help':
        help()
    else:
        main()        
elif len(sys.argv) < 2:
    main()
elif len(sys.argv) > 3:
    print(f" {Fore.LIGHTRED_EX} ")
    print(" Unknow Property")
    print(" Type '--help'")
    sys.exit()
elif len(sys.argv) > 2 < 3:
    target = sys.argv[1]
    property = sys.argv[2]
    if property == "--help":    
        help()
    elif property == "-a":
        scan(target)
    elif property == "-p":
        advanced_scan(target)
    else:
        print(f" {Fore.LIGHTRED_EX} ")
        print(" Unknow Property")
        print(" Type '--help'")
        sys.exit()
