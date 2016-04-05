import sys
import socket

REMOTE_SERVER = "www.google.com"
def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
if is_connected() is False:
    print "\nInternet Connection Required!\n"
    sys.exit(1)

try:
    from facepy import GraphAPI
except ImportError:
    print "\nfacepy not installed, please install using :\npip install facepy\n"
    sys.exit(1)


