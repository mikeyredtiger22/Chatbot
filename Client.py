import requests
import json


def main():

    print ("Connected to client service")
    while True:
        user_input = raw_input("Type 'list' to see all bots or 'connect <Bot Name>' to be connected:\n")
        if user_input.startswith("list"):
            print "Available bots:\n" \
                  "\tBot1\n" \
                  "\tBot2\n"
        elif user_input.startswith('connect'):
            if user_input.split(" ")[1] == "Bot1":
                conversation('http://localhost:5000/')
                print "You have disconnected from Bot1"
                continue
            elif user_input.split(" ")[1] == "Bot2":
                conversation('http://localhost:5001/')
                print "You have disconnected from Bot2"
                continue
            else:
                print "You have not selected an available bot.\n"
                continue
        else:
            print "You have not entered a valid instruction.\n"


def conversation(bot_url):
    user_input = raw_input("You are now connected with Bot1. Type 'exit' to disconnect\n")
    while not user_input.startswith("exit"):
        json_user_input = json.dumps({'message': user_input})
        api_response = str(requests.post(bot_url, json=json_user_input)) + "\n"
        user_input = raw_input(api_response)

if __name__ == '__main__':
    main()
