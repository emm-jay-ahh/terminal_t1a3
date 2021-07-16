# 🅽🅴🆃-🆃🅾🅾🅻🆂

My Terminal Application Assignment

Network Tool Box (AIO)

<br />

## Instructions for setup

### System Requirments

<br />

This application requires Unix/Linux Operating Systems.

No Testing on a Mac; however, this should work.

The following is required for net-tools to function.

 - python3              
 - argparse             (standard library)
 - subprocess           (standard library)
 - simple_term_menu     (library)
 - scapy                (library)
 

Instructions to install are below under Dependencies.

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

As mentioned above, there are some dependencies required for net-tools to function correctly.

<br />

#### argparse   - https://docs.python.org/3/library/argparse.html
#### subprocess - https://docs.python.org/3/library/subprocess.html

Both argparse and subprocess libraries are a part of the standard library in Python and will not require any installation prior


<br />

#### simple-term-menu    - https://pypi.org/project/simple-term-menu/


```
sudo pip install simple-term-menu
```

It is recommended to install this python library with sudo privileges to avoid any issues when first launching net-tools.

<br />

#### scapy    - https://pypi.org/project/scapy/  or https://scapy.net/
            

```
sudo pip install scapy
```

It is recommended to install this python library with sudo privileges to avoid any issues when running the scanner tool.


<br />

---------  ABOVE ALL SPELL AND GRAMMAR CHECKED --------------

### Installing net-tools

First clone the repository to a directory of your choice

```
git clone https://github.com/emm-jay-ahh/terminal_t1a3.git
```

Next

Install net-tools

```
Run Bash Script
```



<br />
<br />

## Statement of Purpose and Scope

<br />

###### Describe at a high level what the application will do
Net-Tools is a collection of IT Networking Tools that I use almost daily both work and home. 
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

<br />

###### At least THREE features, describe each feature

1. Net-Tools Menu System
    - Utilising simple_term_menu (Library)  - https://pypi.org/project/simple-term-menu/
    - A simple interactive and intuitive design
    - Easy navigation up/down + enter or assigned shortcut keys (also VIM shortcuts work)
    - And Future proof to handle a growing toolset

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

The idea is to be able to check network settings without opening another terminal or leaving this application to do so.
Other tools current and future this application will house will require the user to know this type of information before tolls can be deployed correctly.

<br />

3. Ping Host
    - Utilising subprocess library to invoke Linux Commands (Python Standard Library).
    - Can ping internal hosts (e.g. 192.168.1.50).
    - Can also ping externally (e.g. www.google.com).
    - User is required to enter an IP or FQDN and then the number of ping packets to send.

The idea here is to check that we have network access, either internal or external or both.
Ping is a great tool for helping to troubleshoot network-related issues.
The addition of a ping tool was to avoid having to open a new terminal or close the application to check for network connectivity.

<br />

4. Scan Network
    - Utilising scapy library - A powerful and interactive packet manipulation program. 
    - This is for local network use only (Connecting to a network externally over VPN will also work)
    - User can scan for a specific IP. However, the tool is for discovering all IPs on a network

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

User will launch net-tools and the following menu will be displayed

![Image of Main Menu]
https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/app_images/matthew-rooney-T1A3-main_menu.jpg

Currently three options(tools) the user can choose to run.
The user will utilise keyboard with up/down + enter 
Or enter or the associated shortcut key to to launch desired tool

(PICTURE HERE)

Option One - Network Settings

(PICTURE HERE)

Option Two - Ping Host

(PICTURE HERE)

Option Three - Scan Network

(PICTURE HERE)


## Control Flow Diagram

## Implementation Plan

## Status Updates

- Status Update One complete - see development-log.md
- Status Update Two complete - see development-log.md

https://github.com/emm-jay-ahh/terminal_t1a3/blob/main/development-log.md



