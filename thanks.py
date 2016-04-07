import sys
import socket
import time
import datetime

access_token = ''  # Paste your token here

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
    import fb
except ImportError:
    print "\nfb not installed, please install using :\npip install fb\n"
    sys.exit(1)

try:
    from facepy import GraphAPI
except ImportError:
    print "\nfacepy not installed, please install using :\npip install facepy\n"
    sys.exit(1)

facebook = fb.graph.api(access_token)
graph = GraphAPI(access_token)
response = graph.get('me/feed?since=' + str(int(time.time()) - (3600*int(datetime.datetime.now().hour) + 60*int(datetime.datetime.now().minute) + int(datetime.datetime.now().second)) + 1))
# print response['data'][0]['from']
