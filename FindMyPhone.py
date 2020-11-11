import bluetooth
import optparse
# Not Needed yet => import subprocess


def showBanner():
    print(""" 
    
  ▄████  ██▀███  ▓█████  ███▄ ▄███▓ ██▓     ██▓ ███▄    █ 
 ██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓██▒    ▓██▒ ██ ▀█   █ 
▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░    ▒██▒▓██  ▀█ ██▒
░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██░    ░██░▓██▒  ▐▌██▒
░▒▓███▀▒░██▓ ▒██▒░▒████▒▒██▒   ░██▒░██████▒░██░▒██░   ▓██░
 ░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ 
  ░   ░   ░▒ ░ ▒░ ░ ░  ░░  ░      ░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░
░ ░   ░   ░░   ░    ░   ░      ░     ░ ░    ▒ ░   ░   ░ ░ 
      ░    ░        ░  ░       ░       ░  ░ ░           ░ \n""")


def getTarget():
    pOptions = optparse.OptionParser()
    pOptions.add_option("-t", "--target", dest="target_name",
                        help="The target you would like to discover")
    # pOptions.add_option("-a", "--address", dest="target_address", help = "The address of the target you would like to discover")
    (rOptions, arguments) = pOptions.parse_args()
    if not rOptions.target_name:
        # error handling
        pOptions.error(
            '\n[-] Usage : (python/python3) FindMyPhone.py -t "YOUR TARGET"\n[-] Please specify a target, use --help for more infos.')
    return rOptions


def discoverBluetoothDevice(target_name):
    # Starting bluetooth discovery
    print("[+] Starting Bluetooth Discovery")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    # Variable Declaration to None, will contain bdAddr at the end
    target_address = None
    iterateur = 1
    fAddr = {}
    for bdAddr, bdName in nearby_devices:
        print("\n[+] Devices #{0} : {1}\n[+] With the name : {2}" .format(
            iterateur, bdAddr, bdName))
        fAddr["DeviceName"] = bdName
        fAddr["DeviceMac"] = bdAddr
        if target_name == bdName:
            target_address = bdAddr
            break
        iterateur += 1

    if target_address is not None:
        print("\n[+] Target Found ! : " + target_address)
        print("[+] Name of the Device : {0}" .format(target_name))
        print("[+] Address of the Device : {0}" .format(target_address))
        print("[+] Gathering Device Service Infos...")
        # sList = bluetooth.find_service(name=target_name, , address=target_address)
        # if len(services) <= 0:
        #    print("[+] No services found on the target device !")
        # else:
        #    for sServ in services:
        #        print("sServ :", sServ)
    else:
        print("[-] The specified target is not in our range scope")


def main():
    showBanner()
    print("[+] Getting Target")
    target = getTarget()
    print("[+] Current Target : {0}".format(target.target_name))
    discovery = discoverBluetoothDevice(target.target_name)


main()
