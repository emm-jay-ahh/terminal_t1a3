# 🅽🅴🆃-🆃🅾🅾🅻🆂

Terminal Application Assingment

<br />


## Statement of Purpose and Scope

<br />

###### Describe at a high level what the application will do
Net-Tools is a collection of IT Networking Tools that I use almost daily both work and home. 
Combining these tools into one application for quick execution and ease of use.
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

The idea here is to keep the interface clean and uncluttered, we are going for function over fashion.
I decided to go with "simple_term_menu" library for a terminal menu system as it seems to tick all the boxes.
The navigation is baked in but allowing hotkeys assignment will speed things up.
The documentation is solid and getting a quick demo up and running was relatively quick, I had to get a feel for how it operates before committing to it.
   
<br />

2. Network Settings
    - Utilising subprocess library to invoke Linux Commands (Python Standard Library).
    - 2 options to choose from (a sub-menu is displayed)
        - Show All - Check Settings on all network interfaces
            - This Will display all current network interfaces including virtual devices, if available.
        - Show Interface - Check Settings on a specific interface
            - It requires the user to enter an interface name, it then will return the results for that interface only.

The idea is to be able to check network settings without opening another terminal or leaving this application to do so.
Other tools current and future this application will house will require the user to know this type of information before tolls can be deployed correctly.l

<br />

3. Ping Host
    - Utilising subprocess library to invoke Linux Commands (Python Standard Library).
    - Can ping internal hosts (e.g 192.168.1.50).
    - Can also ping externally (e.g www.google.com).
    - User is required to enter an IP or FQDN and then the number of ping packets to send.

The idea here is to check that we have network access either internal or external or both.
Ping is a great tool for helping to troubleshoot network-related issues.
The addition of a ping tool was to avoid having to open a new terminal or close the application to check for network connectivity.

<br />

4. Scan Network
    *

<br />
<br />

## User Interaction and Experience

User will launch net-tools and the following menu will be displayed

(PICTURE HERE)

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

- Status Update One complete - see LOGS.md
- Status Update Two (expected entry 17.07.21) - see LOGS.md

## Implement Application

## 