import random
import subprocess
import os
import sys
import time

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
    |_   _| / \   | \ | |   / \   / ___|| |/ /| ____||  _ \ ( )/ ___| 
      | |  / _ \  |  \| |  / _ \ | |    | ' / |  _|  | |_) ||/ \___ \ 
      | | / ___ \ | |\  | / ___ \| |___ | . \ | |___ |  _ <     ___) |
      |_|/_/   \_\|_| \_|/_/   \_\\____||_|\_\|_____||_| \_\    |____/ 
                                                                         
       __  __    _    ____ ____  ____   ___   ___  _____ _____ ____  
      |  \/  |  / \  / ___/ ___||  _ \ / _ \ / _ \|  ___| ____|  _ \ 
      | |\/| | / _ \| |   \___ \| |_) | | | | | | | |_  |  _| | |_) |
      | |  | |/ ___ \ |___ ___) |  __/| |_| | |_| |  _| | |___|  _ < 
      |_|  |_/_/   \_\____|____/|_|    \___/ \___/|_|   |_____|_| \_\

   
        
 [{}+{}] Insta :  https://instagram.com/m.tanishq.kushwaha/
 [{}+{}] Hacker Banno Chutiya nhi(TEAM VENOM)
 [{}+{}] MacSpoofer 
 {}=============================={}

			                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
logo()


print("1-To change MAC address manually ")
print("2-To get the random MAC address ")
print("3-To chnge to permanent MAC adress- ")
print("4-To show the current MAC address ")
a=int(input(">"))


perm = open("mainmac.txt", "r")
permanent = perm.read()





def show():
    return(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}"))

def get_rand():
   return random.choice("1234567890abcdef")


def rand_mac():
    new=""
    for i in range(0,5):
        new+=get_rand()+get_rand()+":"
    new+=get_rand()+get_rand()
    return new  
    
def man_mac():
    inp=""
    inp=input("Enter the new MAC address-")
    return(inp)


if a==1:
    new_m=man_mac()
    #print("Permanent MAC adress is-"+permanent) 
 

    print("Current MAC address is-")
    print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}"))

    subprocess.call(["sudo","ifconfig","wlan0","down"])




    subprocess.call(["sudo","ifconfig","wlan0","hw","ether","%s"%new_m])
    subprocess.call(["sudo","ifconfig","wlan0","up"])

    print("New MAC adddress is-")
    print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")) 
   
elif a==2:
    new_m=rand_mac()
    #print("Permanent MAC adress is-"+permanent) 
 
    try:
    	print("Current MAC address is-")
    	print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}"))

    	subprocess.call(["sudo","ifconfig","wlan0","down"])

    #print(new_m)    



    	subprocess.call(["sudo","ifconfig","wlan0","hw","ether","%s"%new_m])
    	subprocess.call(["sudo","ifconfig","wlan0","up"])

    	print("New MAC adddress is-")
    	print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")) 
   except:
	print("Sorry for error not valid MAC created try again!!! and can use manual method")
elif a==3:
    new_m=permanent   
     
 

    print("Current MAC address is-")
    print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}"))

    subprocess.call(["sudo","ifconfig","wlan0","down"])




    subprocess.call(["sudo","ifconfig","wlan0","hw","ether","%s"%new_m])
    subprocess.call(["sudo","ifconfig","wlan0","up"])

    print("Changed to permanet MAC adddress")
    print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")) 
   

elif a==4:
    print("Present Mac address is ")
    sh=show()
    print(sh)

else:
    print("Entered a invalid input")    
