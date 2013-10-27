import portfinder
import socket, re, os, time
import threading, platform
#from Imer_Client import IM_Client
import Imer_Client

def first ():
    title = ("Welcome to IMer V0.1")
    print(title.center(21,))
    print("----------------------")
    print("Starting initial OS detection")
    time.sleep(3)        #dramatic pause...
    if detect() == 1:
        print(linux())
        Servip = portfinder.find(readIp())
        if Servip:
            IM = Imer_Client.IM_Client()
            IM().login(Servip)
        else:
            print("Server Not Found, generating one..")
            print("Please Leave the window open and start another IMER session")
            print("NOTE--- you are now the sever DONOT close this window")
            time.sleep(2)
            import Imer_Server
            Serve = Imer_Server.IM_Server()
            Serve.listen(ip)

    else:
        Servip = portfinder.find(windows())
        if Servip:
            IM = Imer_Client.IM_Client()
            IM().login(Servip)
        else:
            if Servip:
                IM = Imer_Client.IM_Client()
                IM().login(Servip)
            else:
                print("Server Not Found, generating one..")
                print("Please Leave the window open and start another IMER session")
                print("NOTE--- you are now the sever DONOT close this window")
                time.sleep(2)
                import Imer_Server
                Serve = Imer_Server.IM_Server()
                Serve.listen(ip)



def linux():
    #checks for private ip and validates then bootstraps
    print("Please enter your machine's local IP \n")
    print("Press Enter and I will bring it up for you")
    raw_input()
    print("-------------------------------------")
    os.system("ifconfig")


def readIp():
    ip = ""
    booltest = True
    while booltest:
        ip = raw_input("Please Enter your ip here -->")
        if ip[0:2] == "19" or ip[0:2] =="17" or ip[0:2] == "10":
            print("your ip is %s" % ip)
            booltest = False
            global ip
            return ip
        else:
            print("Invalid input, try again\n")

def windows():
    #checks for private ip and validates then bootstraps
    print("Grabbing your machines current IP....one sec \n")
    print("-------------------------------------")
    time.sleep(3)
    ip = socket.gethostbyname(socket.gethostname())
    print("Your IP is %s" % ip)
    global ip
    return ip
def detect():
    #The purpose of this funciton is OS detection.
    os = platform.system()
    if os[0:3] == "Lin":
        print ("I see you are on linux")
        return 1
    elif os[0:3] == "Win":
        print ("I see you are on windows.. bummer")
        return 2
    else:
        print("sytem error, shuting down")
        #1 is linux 2 is windows, returned

def IP_Parse(ip):
    servValue=""
    ip2 = re.split(r'(\.|)', ip) #this puts each octet and dot into a value in list
    servValue=ip2[-1]    #this is where you will enter the new desired ip
    return servValue #this will return the last ip if peer is server

first()
