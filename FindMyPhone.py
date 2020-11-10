import bluetooth
import optparse
# Not Needed yet => import subprocess


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
    nearby_devices = bluetooth.discover_devices()
    # Variable Declaration to None, will contain bdAddr at the end
    target_address = None
    iterateur = 1
    for bdAddr in nearby_devices:
        print("Devices #{0} : {1}" .format(iterateur, bdAddr))
        if target_name == bluetooth.lookup_name(bdAddr):
            target_address = bdAddr
            break

    if target_address is not None:
        print("Found bluetooth device with address : {0}" .format(
            target_address))
    else:
        print("The specified target is not in our range scope")


def main():
    print("[+] Getting Target")
    target = getTarget()
    print("[+] Current Target : {0}".format(target.target_name))
    discovery = discoverBluetoothDevice(target.target_name)


main()
