#!/usr/bin/env python3
import scapy.all as scapy

def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)                        # ARP packet object (who has IP ?.?.?.?)
    arp_request.show()                                      # show above packet - DELETE WHEN FINISHED
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")        # Broadcast address to send to all host
    broadcast.show()                                        # show above packet - DELETE WHEN FINISHED
    arp_broadcast = broadcast/arp_request                   # Combine both above packets into one
    arp_broadcast.show()                                    # show above combined packet - DELETE WHEN FINISHED
    
    # print(arp_broadcast.summary())                        # print summary - DELETE WHEN FINISHED
    # scapy.ls(scapy.Ether())                               # Access a list of fields of scapy - DELETE WHEN FINISHED


scan_network("172.16.12.1/24")                              # My Virtual Gateway Address (VMWare)