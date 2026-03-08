

def startServer():
    print("Server started")

def stopServer():
    print("Server stopped")

def restartServer():
    print("Server restarted")

def checkStatus():
    print("Server status: Running")



commandTable = {
    "1": startServer,
    "2": stopServer,
    "3": restartServer,
    "4": checkStatus
}


def runCommand(command):

    if command in commandTable:
        commandTable[command]()
    else:
        print("Invalid command")


while True:

    print("\nServer Management Console")
    print("1. Start Server")
    print("2. Stop Server")
    print("3. Restart Server")
    print("4. Check Status")
    print("5. Exit")

    command = input("Enter command: ")

    if command == "5":
        print("Exiting program")
        break

    runCommand(command)
