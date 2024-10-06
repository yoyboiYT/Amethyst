print("\n")
while True:
    cmd = input("^! ")
    if cmd == "ver":
        print("ziC Alpha 0.0.1")
    elif cmd.startswith("say "):
        print(cmd.removeprefix("say "))
    elif cmd == "xcr":
        print("x-cell has been reset.")
    elif cmd == "quit":
        quit()
    else:
        print("Unknown command: " + cmd)