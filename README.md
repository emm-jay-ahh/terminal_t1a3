# 🅽🅴🆃-🆆🅷🅰🅲🅺

My Terminal Application Assignment

Network Tool Box (AIO)

<br />

## Instructions for setup

### System Requirments

<br />

This application requires Unix/Linux Operating Systems.

No Testing on a Mac; however, this should work.

The following is required for net-whack to function.

 - python3              
 - argparse             (standard library)
 - subprocess           (standard library)
 - simple_term_menu     (library)
 - scapy                (library)
 


<br />

#### Steps to install the application

<br />

First, check if you have python3 installed from a CLI.

```
python3 --version
```

Alternatively, you can check the path location.

```
which python3 
```

If you need to install Python 3 please vist:

https://www.python.org/downloads/



<br />

### Dependencies

As mentioned above, there are some dependencies required for net-whack to function correctly.

<br />

#### argparse   - https://docs.python.org/3/library/argparse.html
#### subprocess - https://docs.python.org/3/library/subprocess.html

<br />

Both argparse and subprocess libraries are a part of the standard library in Python and will not require any installation prior


<br />

I have avoided using a requirements.txt file, my application requires Sudo privileges and the following dependencies need to be installed using Sudo

I would rather the user know what is taking place when Sudo privileges are invoked.  I think it is best the user manually installs for peace of mind and not from an automated script they may not understand.

If you have these dependencies already and the application is still not working, it may be due to the dependencies being installed but not with Sudo privileges.


<br />

#### simple-term-menu    - https://pypi.org/project/simple-term-menu/


```
sudo pip install simple-term-menu
```

It is recommended to install this python library with sudo privileges to avoid any issues when first launching net-whack.

<br />

#### scapy    - https://pypi.org/project/scapy/  or https://scapy.net/
            

```
sudo pip install scapy
```

It is recommended to install this python library with sudo privileges to avoid any issues when running the scanner tool.

<br />

The Network Settings tool is using 'ifconfig' rather than the newer 'ip address'. 

I'm old skool and have not embraced the change yet, so shoot me.

<br />

Would you please check if this is installed by running the following command.

```
ifconfig
```
<br />

Otherwise, if not installed, you can install with the following command


```
sudo apt install net-tools
```

<br />

<br />



### Installing net-whack

First, clone the repository to a directory of your choice

```
git clone https://github.com/emm-jay-ahh/terminal_t1a3.git
```

<br />

Next, we need to convert run-me.sh to be executable.

```
chmod 755 run-me.sh
```
<br />

Finally, we can now execute run-me.sh


```
./run-me.sh
```
net-whack.py should now launch

<br />

Alternatively, after you have cloned the repo, we can run the net-whack.py as follows

```
sudo python3 net-whack.py
```
<br />

If you wish to view help information (sudo is not required)

```
python3 net-whack.py -h
```
OR
```
python3 net-whack.py --help
```
OR
```
./run-me.sh -h
```
OR
```
./run-me.sh --help
```

<br />
<br />


## Statement of Purpose and Scope

###### Describe at a high level what the application will do
net-whack is a collection of IT Networking Tools that I use almost daily both work and home. 
Combining these tools into one application for quick execution and ease of use was a must for me.
It will also be an ever-growing tool-kit for testing and diagnosing networks including hacking tools.

<br />

###### Identify the problem it will solve and explain why you are developing it
It happens to us all from time to time where you forget an argument to a command or the command itself.
Either a man page or google is usually the rescue plan, but even that at times feels tedious.
So I thought it was best I build a Python App that houses all the network tools I need and use most frequently.
As I am intersted in Pen-Testing and all things Off-Sec it makes sense to build around what interests me most.

<br />

###### Identify the target audience
This tool is available for anyone to use, IT Admins, Network & Security folk I think will appreciate it most.
But this is also to assist newcomers to IT and Networking or even the avid home user troubleshooting their network.
This tool is for Unix/Linux users.
Mac & Windows WSL2 should work but currently untested.

<br />

###### Explain how a member of the target audience will use it
The tool requires execution from a terminal CLI and will display a simple and easy-to-navigate menu system.
The user can navigate with the up/down arrows and Enter key or by using a quick key that is assigned.
Some tools will also have submenus allowing for different operations or tasks that they can perform.


<br />
<br />


## Features

###### At least THREE features, describe each feature

1. net-whack Menu System
    - Utilising simple_term_menu (Library)  - https://pypi.org/project/simple-term-menu/
    - A simple interactive and intuitive design
    - Easy navigation up/down + enter or assigned shortcut keys (also VIM shortcuts work)
    - And Future proof to handle a growing toolset

<br />

The idea here is to keep the interface clean and uncluttered; we are going for function over fashion.
I decided to go with "simple_term_menu" library for a terminal menu system as it seems to tick all the boxes.
The navigation is baked in but allowing hotkeys assignment will speed things up.
The documentation is solid, and getting a quick demo up and running was relatively quick. I had to get a feel for how it operates before committing to it.
   
<br />

2. Network Settings
    - Utilising subprocess library to invoke Linux Commands (Python Standard Library).
    - 2 options to choose from (a sub-menu is displayed)
        - Show All - Check Settings on all network interfaces
            - This Will display all current network interfaces, including virtual devices, if available.
        - Show Interface - Check Settings on a specific interface
            - It requires the user to enter an interface name; it then will return the results for that interface only.

<br />

The idea is to be able to check network settings without opening another terminal or leaving this application to do so.
Other tools current and future this application will house will require the user to know this type of information before tolls can be deployed correctly.

<br />

3. Ping Host
    - Utilising subprocess library to invoke Linux Commands (Python Standard Library).
    - Can ping internal hosts (e.g. 192.168.1.50).
    - Can also ping externally (e.g. www.google.com).
    - User is required to enter an IP or FQDN and then the number of ping packets to send.

<br />

The idea here is to check that we have network access, either internal or external or both.
Ping is a great tool for helping to troubleshoot network-related issues.
The addition of a ping tool was to avoid having to open a new terminal or close the application to check for network connectivity.

<br />

4. Scan Network
    - Utilising scapy library - A powerful and interactive packet manipulation program. 
    - This is for local network use only (Connecting to a network externally over VPN will also work)
    - User can scan for a specific IP. However, the tool is for discovering all IPs on a network

<br />

The idea is to scan your whole network for connected devices and have them return the IP address of active hosts.
Scan network is utilising the ARP protocol, which is a layer 2 protocol of the OSI Model, also known as the Data Link layer. ARP is short for Address Resolution Protocol
Scan Network is forwarding a broadcast packet to your switch. 
The switch will then flood out of all connected ports the ARP request packet it just received.
Any operating devices connected will see this ARP packet request.
The devices will then reply with a unicast packet stating, this is my MAC, and this is my IP Address associated with that MAC.
This information is then updated within the ARP Table on your system.


<br />
<br />


## User Interaction and Experience


### Main Menu

![Main Menu](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-main_menu.jpg)

Currently three options or tools the user can choose to run.

The user can utilise the keyboard with up/down + enter, or the user can use the shortcut keys to launch a tool.

<br />


### TOOL 01 - Network Settings Menu     
- shortcut key [1]

![Network Settings Menu](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-net_settings_menu.jpg)

A submenu to the Main Menu and provides two options to the user.

<br />

#### Show All 
- Shows all Network Settings      shortcut key [1]

![Show All](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-net_settings_menu-show_all.jpg)

Hit Show All, and it will display all interfaces on your PC.
This tool is utilising 'ifconfig' if you have issues please see above under Dependencies on how to install

Error:

NONE

<br />

#### Show Interface 
- Shows Specfic Network Inteface      shortcut key [2]

![Show Interface](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-net_settings_menu-show_interface.jpg)

You will need to enter the interface name (network adapter), then press Enter to get your result. 

To go back to the Main Menu you can select and enter Back to Main Menu or use the shortcut key [b]

Error:

Providing the wrong interface will show the following error.

"error fetching interface information: Device not found"

<br />

#### Back to Main Menu
- Return you back to the main menu      shortcut[b]

<br />

### TOOL 02 - Ping Host     
- shortcut key [2]

![Ping Host](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-ping_host.jpg)

Here we can either enter a web address (e.g. www.google.com) or an IP address (e.g. 192.168.1.200).
It will then ask for how many ping packets to send (3 - 4 is usually enough)
An excellent tool for troubleshooting network connectivity both internally and externally.

100% packet loss indicates the host you are sending the pings to is either offline, ICMP has been disabled on the host, a firewall is blocking ICMP requests, or the address entered is incorrect

Error:

There are no errors displayed to the user. The only indication that you may have entered an incorrect address is 100% packet loss 

<br />

### TOOL 03 - Scan Network      
- shortcut key [3]

![Scan Network](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-scan_network.jpg)

Scan Network requires that we enter a Network and Subnet in the following format 10.0.0.1/24

This tool is great for scouting out all live hosts on a network.

It returns the IP Address in use and the associated MAC tied to it.

Error:
No actual errors will display; however, if you input the incorrect network, the results returned will be empty. Double-check the network and subnet and try again.

Please also note that I have a 1-second timeout on un-returned packets. This is to avoid the tool from 'hanging' as it waits for a return packet that will never actually be returned.
High network latency can cause a further issue in returning host IPs that are alive and have gone beyond the 1-second threshold.

<br />

### EXIT/QUIT

To exit net-whack you can select and enter Quit/Exit or use the shortcut key [q]

This will also work in the submenu and will exit the application


<br />
<br />


## Control Flow Diagram

![Control Flow](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-control_flow.jpg)


<br />
<br />


## Implementation Plan

The first thing I needed to do was find a terminal menu system, which was easy to use and not too difficult to implement.
I eventually stumbled upon simple_term_menu (python library) from a (7 min) Youtube video tutorial (how-to). 
Sold, the inbuilt navigation (up/down arrows) is baked in.
The simplicity of adding colour and descriptions to menu options was another great feature.
Overall this allowed me to focus more on constructing the network tools in the app.

An MVP was up and ready within an hour. Approx 5 hours total spent on the Menu System.

Second I needed to get more familiar with subprocess (python library) as I wanted to invoke some *nix commands to perform some actions directly from the application.  I spent approx 2-3 hours researching and playing with subprocess.

An MVP for Network Settings was ready in 2 hours, and I roughly took a total of 4 hours to finalise it.

An MVP for Ping Host was ready in approx 1.5 hours.  I roughly spent about 3-4 hours getting it to where I wanted it.

Last I needed to research scapy (python library) for Scan Network to function.  Had spent quite a bit of time here researching and following tutorials to wrap my head around it better approx 4 hours of researching and fiddling with scapy.

An MVP for Scan Network took approx 3-4 hours, and I have spent probably close to 6-7 hours in total. I had some issues implementing it to the Terminal Menu System, but I got there in the end; with a bit of help from my teacher, I got it to work.

<br />

- MAIN MENU SYSTEM      (APP OPENS HERE)

    - Network Settings  (SUBMENU)
        
        - Show All      (show all network interface on system)        
            - app will invoke 'ifconfig'

        - Show Interface    (show only a specific network interface on system)
            - user enters {interface} name - app will invoke 'ifconfig {interface}'
        
        - Back to Main Menu 
            - app will return user to main menu

   

     - Ping Host    (TOOL)
        
        - User is required to enter a IP or WEB Address {host} and then the amount {count} of pings to send    
            - app will invoke 'ping -c {count} {host}'
        
        - Alot of information is normally returned, stripping away uneccarry data was required
            - app to display only relevant data back to user

        - User is required to hit 'Enter' to return to main menu



    - Scan Network  (TOOL)
        - User is required to enter a Network and subnet
            - app then sends our a Broadcast ARP packet (ICMP)
            - Any alive hosts on network will return a reply packet 
                - Stating their IP address
                - Stating their MAC Address
            - app processes this information
                - Return back to user in a table form Host information
            
            - User is required to hit 'Enter' to return to main menu



    - Exit/Quit  
        - This will reuturn the user back to the CLI
            - this simple task is built in to simple_term_menu


<br />

### TESTING

Testing I undertook to ensure the application operates as intended

![Testing](https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-testing.jpg)


<br />
<br />


## Status Updates

- Status Update One complete - see development-log.md
- Status Update Two complete - see development-log.md

https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/development-log.md


<br />

- Trello worklog can be found here:

https://github.com/emm-jay-ahh/terminal_t1a3/tree/main/trello