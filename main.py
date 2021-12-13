from steam.client import SteamClient
from config import username, password
sc: SteamClient = SteamClient()

sc.login(username=username, password=password)
while True:
    message = sc.wait_event("chat_message")
    print(message)