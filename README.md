# Lab 003 Function Exploration with your Peers!

## Objectives
In this lab, you will build a **VERY** basic peer-to-peer chat system using existing Python libraries and the [lab_chat.py](lab_chat.py) file shared in this repo. The goal is to create functions that allow users to join a chat group and send and receive messages. You’ll explore core concepts of Python defining functions, parameters, simple loops, and importing and calling existing functions.

This lab is divided into four parts and should take approximately two hours to complete.

## Prerequisites:
* Installation of necessary Python modules
    * You can install the necessary modules either through your IDE's terminal as indicated below, or by installing each module as depicted in the [linked video](https://redwoods.us-west-2.instructuremedia.com/embed/fe6c9462-136a-423a-bf5d-32eba7128321).
      ```shell
      pip install zeromq-pyre
      ```

## Part 1: Core Functions – Data Handling and User Input
In this part, you'll create several basic functions to handle user input and data that will be used in the later stages. Here you should focus on practicing creating proper function headers and bodies.

### Put your Functions in a new Python File

1. Create a new file in your project named **lab003.py**

### Create a Function to Get Your Username

1. Create a function named **get_username** that asks the user for their desired username. (HINT: input())
    * If you are not sure about the proper parts of a function see the [class notes](https://thartmanoftheredwoods.github.io/CIS-12/week_3py.html#defining-functions).
2. Your function should remove forward and trailing whitespace. (HINT: strip())
3. Your function should **return** the username in upper case letters. (HINT: upper())
    * **return** is a keyword you can put at the end of a function that will send back any data you type after it.
    * **return** returns to the location in the code the **function** was called from.

### Create a Function to Select a Chat Group to Join

1. Write a function named **get_group** that asks the user for a group name they'd like to join. (HINT: input())
    * If you are not sure about the proper parts of a function see the [class notes](https://thartmanoftheredwoods.github.io/CIS-12/week_3py.html#defining-functions).
2. Your function should remove forward and trailing whitespace. (HINT: strip())
3. Your function should return the username in upper case letters. (HINT: upper())

### Create a Function to Send a Message

1. Create a function named **get_message** that asks the user to input the message they’d like to send.
2. Your function should remove forward and trailing whitespace.
3. Your function should return the typed message.

## Part 2: Understanding Peer-to-Peer Communication Functions
Now that you have user inputs ready, you’ll move to handling peer-to-peer communication using the [lab_chat.py](lab_chat.py) code. In this file, there are some preexisting functions to connect/become a peer-to-peer node, join a chat group, and get a communication channel to send and receive messages. Your job is to identify these functions and their parts, then integrate these functions into your functions.

* In your project create a **README.md** file
* For each function in the [lab_chat.py](lab_chat.py) file add the following to your **README.md** file:
  1. Full Function Header, and indicate the function name with a comment.
  ```python
  # Example
  def chat_task(ctx, pipe, n, group):  # function name is chat_task 
  def get_peer_node(username): #function name is get_peer_mode
    # Username: I assume this is the Username from get_username function
    # This function returns something that looks like a pyre node to me, possibly my peer node.
  def join_group(node, group): #fuuction name is join_group
    # Node: I assume this is my peer computer node
    # Group: I assume this is a group that we want to join from our get_group function
    # This function returns nothing
  def get_channel(node, group): #function name is get_channel
    # Node: I assume this is my peer computer node
    # Group: I assume this is a group that we want to join, similar to get_group
    # Returns a zhelper but I do not understand what it is for at all. Seems to deal with the node and group though.
  2. List all parameters and what you think they are. Put "UNSURE" if you don't have a guess.
  ```shell
  # Example
  ctx: This is a ZeroMQ Connection Context
  pipe: This is a communications pipe polled by ZeroMQ for messages.
  n: This is the peer to peer node my chat app is connected as
  group: This is the peer chat group I wanted to join
  node: The computer used by a particular username
  username: This is the chosen username
  ```
  3. Note if the function **returns** anything. If it does, note what you believe it returns, and make a final note about what you believe the function may do.
  ```shell
  # Example
  The chat_task method does not return anything, it appears to be the send/recieve manager.
  ```

## Combining the Functions to Create the Peer-to-Peer Chat
In this part, you will combine all the functions from Part 1 and Part 2 to create a functioning peer-to-peer chat.

### Initializing the Chat

1. Import the lab_chat.py functions into your lab003.py file
    * Remember, there are a few ways you could do this.
        * import the entire file `import lab_chat`, but then every function would need to be called by `lab_chat.func`
        * import the functions by name `from lab_chat import get_peer_node, other_funcs`
        * OR import the entire file and **alias** the module so it's shorter `import lab_chat as lc`
2. Now, create a function name **initialize_chat** that initializes the chat
    * It should get the user's username. (HINT: you wrote this method in part 1)
    * Get the desired chat group to join. (HINT: you wrote this method in part 1)
    * Connect as a peer node. (HINT: you identified this method in part 2)
        * Pay attention to your parameters and return notes for clues on how to use this function!
    * Joins the group. (HINT: you identified this method in part 2)
        * Pay attention to your parameters and return notes for clues on how to use this function!
    * **return** a chat channel. (HINT: you identified a method for this in part 2 also!)

### Sending and Receiving Messages

Write a function named **start_chat** that uses your ```get_message``` function, **a loop**, and the **channel** returned by **initialize_chat** to send a message.

* HINT: Your last function should look like the below example:
    * Obviously there are a few things we've not talked about, so now is your time to ask me what they are!
     
```python
def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")
```

## Part 4: Testing and Debugging the Chat Application

In this final part, you will focus on testing and debugging your chat application. This will involve testing each of the functions independently and then testing the entire system.

### Testing Individual Functions

1. Test `get_username()`, `get_group()`, and `get_message()` to ensure they return the expected inputs.
2. Test the `initialize_chat()` function by running it and making sure it returns a channel without throwing any exceptions. (HINT: use the type() function)
    * A channel type will be something like: `<class 'zmq.sugar.socket.Socket'>`
3. Test the `start_chat()` function by running a basic chat where you send and receive messages to a group with a single other peer.

### Debugging Common Errors
 
* If messages are not being received, check whether the group has been joined correctly.
* Verify that Pyre is installed correctly by running `pip list | grep pyre` in your terminal or simply checking your installed modules in your IDE settings.

## Part 5: Pushing to GitHub
[Review video of this process](https://redwoods.us-west-2.instructuremedia.com/embed/72299bfd-8420-4ad0-8af5-18fb8e32e50a)
1. **Create a GitHub Repository:**
   * Log in to your GitHub account.
   * Create a new repository with a suitable name (e.g., "python_lab3").
2. **Configure Git in PyCharm:**
   * Open the "Git" menu in PyCharm and initialize a Git repository for your project.
   * Add your GitHub remote repository by going to "Git" -> "Manage Remotes".
3. **Commit Changes:**
   * Stage all changes in your PyCharm project.
   * Commit the changes with a descriptive message (e.g., "Initial commit").
4. **Push to GitHub:**
   * Push the committed changes to your GitHub repository using the "Push" button in PyCharm.

### Submission
Submit the link from your GitHub repository containing your lab 3 repo to Canvas.
