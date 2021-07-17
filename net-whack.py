import argparse
from sys import argv
from simple_term_menu import TerminalMenu
from ping import ping_host
from settings import show_all, show_interface
from scanner import scan_network


def parse_arguments():
    parser = argparse.ArgumentParser(
        usage="\n\nTRY\tsudo python3 net-whack.py\nOR\t./run-me.sh",
        description="\nSudo privileges are required for the tools inside to function correctly\n",)
    parser.parse_args()


def menu(): 
    # Menu display and style
    # Main Menu
    main_options = [
        "[1] Network Settings",
        "[2] Ping Host",
        "[3] Scan Network",
        "[q] Quit/Exit",
    ]
    main_menu = TerminalMenu(
        main_options,
        clear_screen=True,
        title="\n\n     🅽 🅴 🆃 - 🆆 🅷 🅰 🅲 🅺\n\n",
        status_bar="\n     Tools\n",
        menu_cursor_style=("fg_green", "bold",),
        menu_highlight_style=("bg_black", "fg_green"),
        status_bar_style=("bg_black", "fg_green",),
        cycle_cursor=True,
        )
    
    # Network Settings menu
    net_options = [
        "[1] Show All",
        "[2] Show [Interface]",
        "[b] Back To Main Menu",
    ]
    net_menu = TerminalMenu(
        net_options, 
        clear_screen=True,
        title = "\n\n     🆂 🅴 🆃 🆃 🅸 🅽 🅶 🆂\n\n",
        status_bar="\n     Check network related settings\n",
        menu_cursor_style=("fg_green", "bold",),
        menu_highlight_style=("bg_black", "fg_green"),
        status_bar_style=("bg_black", "fg_green",),
        cycle_cursor=True,
        )

    
    def menu_operation():
        try:
            quitting = False
            while quitting == False:
                options_index = main_menu.show()
                options_choice = main_options[options_index]

                if(options_choice == main_options[-1]):
                    print("\n\nQUIT NET TOOLS\n\n")
                    quitting = True                             # Quit/Exit Net-Tools
                
                elif(options_choice == main_options[0]):              
                    options_index = net_menu.show()             # Open submenu to Network Settings
                    options_choice = net_options[options_index]
                    
                    try:
                        if(options_choice == net_options[0]):
                            show_all()
                        elif(options_choice == net_options[1]):
                            show_interface()
                        elif(options_choice == net_options[-1]):
                            main_menu.show()

                    except AttributeError:
                        continue
                    except KeyboardInterrupt:
                        print("\n\nKEYBOARD INTERUPT - EXIT NET-WHACK\n\n")
                        

                elif(options_choice == main_options[1]):    
                    ping_host()                                 # change to Ping Host when app is built
                
                elif(options_choice == main_options[2]):
                    scan_network()                              # change to Scan Network when app is built
    
        except TypeError:
            print("\n\nPOSSIBLE KEYBOARD INTERUPT OR TYPE ERROR - EXITING NET-WHACK\n\n")
        
    
    
    menu_operation()


parse_arguments()
menu()