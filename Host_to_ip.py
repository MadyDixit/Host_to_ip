import socket

def get_detail():
    try:
        host_name = input("Enter The Hostname("'Without https://www.'"):")
        host_ip = socket.gethostbyname(host_name)
        #print("Host-Name:",socket.gethostname(host_name))
        print("Host-IP:",host_ip)
    except:
        print("Unable to detect:")

get_detail()
