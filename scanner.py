import scapy.all as scapy


def scan_network():
    try:
        def scan(ip):
            arp_request = scapy.ARP(pdst=ip)                                                # ARP packet object (who has IP ?.?.?.?)  
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                # Broadcast address to send to all host
            arp_broadcast = broadcast/arp_request                                           # Combine both above packets into one
            answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]           # send packet with custom ether(MAC) and capture results   
                                                                                            # timeout of 1 sec - if no response move on do not wait
            # for loop to iterate over each answered arp request
            alive_clients_list = []
            for item in answered_list:                                                      # psrc == Source IP + hwsrc == Source MAC
                alive_clients_dict = {"ip": item[1].psrc, "mac": item[1].hwsrc}             # of the packets being returned to us                                                                                 
                alive_clients_list.append(alive_clients_dict)
                    
            return alive_clients_list


        # Return results to user
        try:
            def returned_results(results):
                print("\nIP ADDRESS\t\t\tMAC ADDRESS\n-------------------------------------------")
                for alive_client in results:
                    print(alive_client["ip"] + "\t\t  " + alive_client["mac"])

                return_msg
            
            # added the input entry here 
            print("\n Enter Network with subnet\n eg. 192.168.1.1/24")
            scan_result = scan(input(" >>> "))
            returned_results(scan_result)
        
        # Error handliing when input is not compatible
        except NameError:
            input("\n\nINPUT NOT COMPATIBLE SEE e.g ABOVE\n\nRETURNING TO MAIN MENU (HIT ENTER)") 
            return  

    # Error handling Keyboard interupts
    except KeyboardInterrupt:
        print("\n\n A KEYBOARD INTERUPT DETECTED\n\n")
        return_msg = input("\n\n Press Enter to return to MAIN MENU\n\n")
        return
        
    