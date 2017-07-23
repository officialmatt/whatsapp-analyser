import chatData
from pprint import pprint

def main():
    json = chatData.readChat()
    pprint(json)


main()
