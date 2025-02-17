#! /usr/bin/env python
import argparse
import scapy.all as scapy
import time
import sys


def loading_animation():
    animation = [
        "[■□□□□□□□□□] 10%",
        "[■■□□□□□□□□] 20%",
        "[■■■□□□□□□□] 30%",
        "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%",
        "[■■■■■■□□□□] 60%",
        "[■■■■■■■□□□] 70%",
        "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%",
        "[■■■■■■■■■■] 100%"
    ]

    print("\n\033[1;32mInitializing Network Sniffer...\033[0m\n")
    time.sleep(1)

    for i in range(len(animation)):
        sys.stdout.write(f"\r\033[1;36mScanning Network: {animation[i]}\033[0m")
        sys.stdout.flush()
        time.sleep(0.5)

    print("\n\033[1;32m\n✔ Scan Complete! Ready to sniff network packets.\033[0m")
    print("\n\033[1;33mAuthor: Abhin Binu\033[0m")
    print("\033[1;34m=======================================\033[0m\n")


def get_argument():
    parser = argparse.ArgumentParser(description="Network Scanner using Python")
    parser.add_argument("-t", "--target", dest="target", help="TARGET IP/IP RANGE", required=True)
    args = parser.parse_args()
    return args


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    print(f"\n[DEBUG] Sending ARP Request to: {ip}")  

    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)

    if not answered_list:
        print("\n[ERROR] No devices found! Check network settings or run as root.")
        return []

    clients_list = []

    print("\nDiscovered Devices:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")

    for element in answered_list:
        print(f"[DEBUG] Found: {element[1].psrc} - {element[1].hwsrc}") 
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_list(result_list):
    if not result_list:
        print("\n[INFO] No devices found on the network.")
        return

    print("\nFinal Results:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in result_list:
        print(f"{client['ip']}\t\t{client['mac']}")


if __name__ == "__main__":
    
    loading_animation()

    
    args = get_argument()

    scan_result = scan(args.target)
    print_list(scan_result)
