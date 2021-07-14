import subprocess
import os

# Check network settings
   
def show_all():       
    # command we want to invoke
    command = "ifconfig"
    # Send any number of pings to a host address (FQDN or IP Address)
    # example of the command: ping -c 2 www.google.com     c
    full_command = subprocess.getoutput(command)

    print(full_command)

    print("\n\nScroll up to see results")
    input("\nPress ENTER to return to Main Menu\n\n")


def show_interface():       
    # command we want to invoke
    interface = input(  "\nEnter an interface name"
                        "\ne.g eth0, wlan0, eno2"
                        "\n>>> ")
    
    command = ("ifconfig " + interface) 
    # Send any number of pings to a host address (FQDN or IP Address)
    # example of the command: ping -c 2 www.google.com     
    full_command = subprocess.getoutput(command)

    print(full_command)

    input("\nPress ENTER to return to Main Menu\n\n")

