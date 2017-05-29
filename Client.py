import Bot1
import Bot2
import requests
import json


def main():
    bot1 = Bot1
    bot2 = Bot2

    print ("Connected to client service")
    while True:
        user_input = raw_input("Type 'list' to see all bots or 'connect <Bot Name>' to be connected:\n")
        if user_input.startswith("list"):
            print "Available bots:\n" \
                  "Bot1\n" \
                  "Bot2\n"
        elif user_input.startswith('connect'):
            if user_input.split(" ")[1] == "Bot1":

                user_input = raw_input("You are now connected with Bot1\n")
                print "User Input: ", user_input

                json_user_input = json.dumps({'message': user_input})
                print "Json user input: ", json_user_input

                api_response = requests.post('http://localhost:5000/', json=json_user_input)
                print api_response, "\n"

                continue
            elif user_input.split(" ")[1] == "Bot1":
                print "You are now connected with Bot2\n"
                continue
            else:
                print "You have not selected an available bot.\n"
                continue

    # ChatBot.get_response(bot1, input_item)


if __name__ == '__main__':
    main()
