import enquiries


class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def chooseOptions(options):
    choice = enquiries.choose("Which payload do you want?", options)
    lhost = enquiries.freetext("LHOST:")
    lport = enquiries.freetext("LPORT:")
    return lhost, lport, choice


def windows():

    options = ["windows/meterpreter/reverse_tcp", "windows/meterpreter/reverse_tcp_uuid", "windows/meterpreter/reverse_tcp_dns",
               "windows/meterpreter/reverse_http", "windows/meterpreter/reverse_https", "windows/meterpreter/reverse_winhttp", "windows/meterpreter/reverse_winhttps"]
    lhost, lport, choice = chooseOptions(options)
    print(choice, lhost, lport)


def linux():

    options = ["linux/x86/meterpreter/reverse_tcp", "linux/x86/meterpreter/reverse_tcp_uuid", "linux/x86/meterpreter/reverse_http",
               "linux/x86/meterpreter/reverse_https", "linux/x86/meterpreter/reverse_ipv6_tcp", "linx/x86/meterpreter/reverse_nonx_tcp"]
    lhost, lport, choice = chooseOptions(options)
    print(choice, lhost, lport)


def java():

    options = ["java/meterpreter/reverse_tcp",
               "java/meterpreter/reverse_http", "java/meterpreter/reverse_https"]
    lhost, lport, choice = chooseOptions(options)
    print(choice, lhost, lport)


def android():

    options = ["android/meterpreter/reverse_tcp",
               "android/meterpreter/reverse_http", "android/meterpreter/reverse_https"]
    lhost, lport, choice = chooseOptions(options)
    print(choice, lhost, lport)


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
    options = ["Windows", "Linux", "Java", "Android"]

    choice = enquiries.choose("What is the target OS?", options)
    globals()[choice.lower()]()


if __name__ == "__main__":
    main()
