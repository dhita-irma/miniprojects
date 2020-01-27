message = None


def input_message():
    global message
    # Enter your Good Morning Msg
    print()
    print("Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
    message = []
    temp = ""
    done = False

    while not done:
        temp = input()
        if len(temp) != 0 and temp[-1] == "~":
            done = True
            message.append(temp[:-1])
        else:
            message.append(temp)
    message = "\n".join(message)
    print()
    print(message)


