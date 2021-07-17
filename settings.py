import subprocess


# Check network settings
   
def show_all():       
    # command we want to invoke
    command = "ifconfig"
    # Send any number of pings to a host address (FQDN or IP Address)
    # example of the command: ping -c 2 www.google.com     c
    full_command = subprocess.getoutput(command)

    print(full_command)

    input("\n\n Press Enter to return to MAIN MENU\n\n")


def show_interface():       
    # command we want to invoke
    interface = input(  "\n Enter an interface name"
                        "\n e.g eth0, wlan0, eno2"
                        "\n\n >>> ")
    
    command = ("ifconfig " + interface) 
    # Send any number of pings to a host address (FQDN or IP Address)
    # example of the command: ping -c 2 www.google.com     
    full_command = subprocess.getoutput(command)

    print(full_command)

    input("\n\n Press Enter to return to MAIN MENU\n\n")

