import subprocess
import os

# ping a host address function
def ping_host(): 
    try:    # a function to ping given host
        def ping(host, count):
            # command we want to invoke
            command = "ping"
            # Send any number of pings to a host address (FQDN or IP Address)
            # example of the command: ping -c 2 www.google.com     
            full_command = subprocess.Popen([command, "-c", count, host], stdout = subprocess.PIPE)
            
            # store the standard output (stdout) of the ping
            # remove or split uneccessary data.
            output = str(full_command.communicate())
            output = output.split("\n")
            output = output[0].split("\\n")
        
            # variable to store the result (list)
            results = []
            for line in output:
                results.append(line)
        
            # print the results
            print("\nPING RESULTS: \n")
            print("\n".join(results[len(results) - 3:len(results) - 1]))
            input("\n\nPress Enter to return to MAIN MENU\n\n")
            
            return results

        #Take user input
        def user_input():
            ip_address = input("\n Enter a Web Address or IP Address"
                               "\n eg. www.google.com or 192.168.1.1"
                               "\n >>> ")
            
            pings_to_send = input("\n How many PINGs to send?"
                                  "\n HINT: Try 3"
                                  "\n >>> ")
            
            return ping(ip_address, pings_to_send)

        user_input()

    except KeyboardInterrupt:
            print("\n\nQUIT PING\n")