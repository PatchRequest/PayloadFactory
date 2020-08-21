
def windows():
    print("Windows!")
    pass


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

    os = input(
        "What is the target OS:\n1. Windows\n2. Linux\n3. MacOS\n4. Android\nInput:")
    func = osSwitch(int(os))
    func()


if __name__ == "__main__":
    main()
