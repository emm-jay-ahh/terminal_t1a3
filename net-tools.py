from simple_term_menu import TerminalMenu

def menu():
    # Main menu
    # options to display including [hotkeys]
    
    main_options = [
        "[1] Network Settings",
        "[2] Ping Host",
        "[3] Scan Network",
        "[q] Quit/Exit",
    ]
    
    main_menu = TerminalMenu(main_options,
        clear_screen=True,
        title="\n\n     🅽 🅴 🆃 - 🆃 🅾 🅾 🅻 🆂\n\n",
        status_bar="\n     Main Menu\n",
        menu_cursor_style=("fg_green", "bold",),
        menu_highlight_style=("bg_black", "fg_green"),
        status_bar_style=("bg_black", "fg_green",),
        cycle_cursor=True,
        )
    
    # Network Settings menu
    # options to display including [hotkeys]
    net_settings_options = [
        "[1] Show All (ifconfig)",
        "[2] Show Interface (ifconfig [interface])",
        "[q] Quit/Exit",
    ]
    net_settings_menu = TerminalMenu(net_settings_options, title = "\n\n     🅽 🅴 🆃 🆆 🅾 🆁 🅺  🆂 🅴 🆃 🆃 🅸 🅽 🅶 🆂\n\n")

    quitting = False

    try:
        while quitting == False:
            options_index = main_menu.show()
            options_choice = main_options[options_index]

            if(options_choice == main_options[-1]):
                print("\nQUIT NET TOOLS\n")
                quitting = True
            if(options_choice == main_options[0]):
                net_settings_menu.show()                # Open submenu to Network Settings
            if(options_choice == main_options[1]):    
                return                                  # change to Ping Host when app is built
            if(options_choice == main_options[2]):
                return                                  # change to Scan Network when app is built
    except TypeError:
        print("\nERROR:  POSSIBLE KEYBOARD INTERUPT\n")

menu()