import netifaces
import ipaddress
import socket

def main():
    gws = netifaces.gateways()
    print(f'INTERFACES: {netifaces.interfaces()}')
    print(f'GATEWAYS  : {gws["default"][netifaces.AF_INET]}\n')

    print(f'INTERFACE "lo"')
    addrs = netifaces.ifaddresses("lo")
    print(f'{addrs[netifaces.AF_INET]}\n')

    print(f'INTERFACE "eth0"')
    addrs = netifaces.ifaddresses("eth0")
    print(f'{addrs[netifaces.AF_INET]}\n')

    ip = addrs[netifaces.AF_INET][0]["addr"]
    subnet = addrs[netifaces.AF_INET][0]["netmask"]

    hostname = socket.gethostname()
    ip_interface = ipaddress.ip_interface(f'{ip}/{subnet}')
    print(f'HOSTNAME            : {hostname}')
    print(f'IP                  : {ip_interface.ip}')
    print(f'NETWORK             : {ip_interface.network}\n')

    print(f'NUMBER OF ADDRESSES : {ip_interface.network.num_addresses}\n')

    print(f'NETWORK ADDRESS     : {ip_interface.network.network_address}')
    print(f'BROADCAST ADDRESS   : {ip_interface.network.broadcast_address}')

if __name__ == '__main__':
    main()
