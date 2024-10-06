print("\n")

pgm = []
main_loop = True
while True:
    while main_loop:
        cmd = input("^! ")
        if cmd == "ver":
            print("ziC Alpha 0.0.2")
        elif cmd.startswith("say "):
            print(cmd.removeprefix("say "))
        elif cmd == "xcr":
            pgm = []
            print("x-cell has been reset.")
        elif cmd == "pgm":
            print("pgm-editor\n")
            pgm = []
            pgm_edit = True
            while pgm_edit:
                pgm_input = input("#> ")
                pgm.append(pgm_input)
                if pgm_input == "exit":
                    pgm_edit = False
        elif cmd == "pgm -r":
            pgm_index = 0
            main_loop = False
            pgm_run = True
        elif cmd == "pgm --view":
            print(" ")
            for command in pgm:
                print(command)
            print(" ")
        elif cmd == "quit":
            quit()
        else:
            print("Unknown command: " + cmd)

    while pgm_run:
        cmd = pgm[pgm_index]
        if cmd == "ver":
            print("ziC Alpha 0.0.2")
        elif cmd.startswith("say "):
            print(cmd.removeprefix("say "))
        elif cmd == "exit":
            print("\nDone running pgm.")
            main_loop = True
            pgm_run = False
        else:
            print("Unknown command: " + cmd)
        pgm_index += 1