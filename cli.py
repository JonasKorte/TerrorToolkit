import core.terror as terror
import os

def main():
    terror.scanModules()
    terror.executeModule("wifi-bruteforce", args = {'interface': 0, 'ssid': 'guest network', 'wordlist_path': os.pardir + '/PlainText.txt'})

if __name__ == '__main__':
    main()