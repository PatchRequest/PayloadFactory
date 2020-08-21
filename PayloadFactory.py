class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def windows():
    print(bcolors.BOLD + "Choose your payload:" + bcolors.ENDC)
    print(bcolors.OKBLUE + "1. windows/meterpreter/reverse_tcp")
    print("2. windows/meterpreter/reverse_tcp_uuid")
    print("3. windows/meterpreter/reverse_tcp_dns")
    print("4. windows/meterpreter/reverse_http")
    print("5. windows/meterpreter/reverse_https")
    print("6. windows/meterpreter/reverse_winhttp")
    print("7. windows/meterpreter/reverse_winhttps" + bcolors.ENDC)


def linux():
    pass


def macos():
    pass


def android():
    pass


def osSwitch(i):
    switcher = {
        1: windows,
        2: linux,
        3: macos,
        4: android
    }
    func = switcher.get(i, lambda: print("No valid choice!"))
    return func


def main():

    print(bcolors.FAIL + """


  _____            _                 _ ______         _                   
 |  __ \          | |               | |  ____|       | |                  
 | |__) |_ _ _   _| | ___   __ _  __| | |__ __ _  ___| |_ ___  _ __ _   _ 
 |  ___/ _` | | | | |/ _ \ / _` |/ _` |  __/ _` |/ __| __/ _ \| '__| | | |
 | |  | (_| | |_| | | (_) | (_| | (_| | | | (_| | (__| || (_) | |  | |_| |
 |_|   \__,_|\__, |_|\___/ \__,_|\__,_|_|  \__,_|\___|\__\___/|_|   \__, |
              __/ |                                                  __/ |
             |___/                                                  |___/ 

    """ + bcolors.ENDC)

    os = input(bcolors.BOLD +
               "What is the target OS: " + bcolors.ENDC + bcolors.OKBLUE + "\n1. Windows\n2. Linux\n3. MacOS\n4. Android\n" + bcolors.ENDC + bcolors.WARNING + "Input:")
    print(bcolors.ENDC)
    func = osSwitch(int(os))
    func()


if __name__ == "__main__":
    main()
