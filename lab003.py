import zmq
import lab_chat as lc
import time

def get_user_input(message, to_upper=True):
    if to_upper:
        response = input(message).strip().upper() #assigned to response, which is returned to get_user_input
    else:
        response = input(message).strip()
    return response

def get_username():
    return get_user_input("Enter your username: ") #argument gets assigned to (message)
    #after message typed, assigned to get_username

def get_group():
    return get_user_input("Enter your group to join: ")

#asks user to type message they want to send
def get_message():
    return get_user_input("Enter your message: (type 'exit' to end the chat) ", False)

#part 3
def initialize_chat():
    user = get_username()
    group = get_group()
    node = lc.get_peer_node(user)
    lc.join_group(node, group)  #found an error here, I originally had it as "lc.join.group and it was returning an error
                                # saying lab_chat has no attribute to join.  Changed to "lc.join_group"
    time.sleep(5)
    channel = lc.get_channel(node, group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()

            # checks to see if user ended the chat
            if msg.lower() in ['exit']:
                #Uses the existing channel
                channel.send("$$STOP".encode('utf_8')) #was using $$$STOP instead of $$STOP
                print("FINISHED")
                break
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break

    #print("FINISHED") commented out because it was creating a redundent "FINISHED" upon typing exit


start_chat()

#print(type(initialize_chat()))


