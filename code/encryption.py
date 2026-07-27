import random
import commands

def encrypt(input):
    input = input.lower()
    input = list(input)

    key = ["1", "2", "3", "4", "5"]
    random.shuffle(key)

    Command = commands.Command("1")

    for item in key:
        match item:
            case "1":
                Command.number = "1"
                input = Command.use_command(input, False)
            case "2":
                Command.number = "2"
                input = Command.use_command(input, False)
            case "3":
                Command.number = "3"
                input = Command.use_command(input, False)
            case "4":
                Command.number = "4"
                input = Command.use_command(input, False)
            case "5":
                Command.number = "5"
                input = Command.use_command(input, False)

    input.extend(key)
    input = "".join(input)
    return input

def decrypt(input):
    input = input.lower()
    input = list(input)

    key = input[-5:]
    key.reverse()

    del input[-5:]

    Command = commands.Command("1")
    
    for item in key:
        match item:
            case "1":
                Command.number = "1"
                input = Command.use_command(input, True)
            case "2":
                Command.number = "2"
                input = Command.use_command(input, True)
            case "3":
                Command.number = "3"
                input = Command.use_command(input, True)
            case "4":
                Command.number = "4"
                input = Command.use_command(input, True)
            case "5":
                Command.number = "5"
                input = Command.use_command(input, True)

    input = "".join(input)
    return input