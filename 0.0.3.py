# ziC Alpha 0.0.3
# Last update: 6/10/2024 @ 5:09 PM
# Created by Jelle

print("\n")

# System declarations
main_loop = True

# Program declarations
pgm = []
pgm_edit = False
pgm_input = ""
pgm_index = 0
pgm_run = False

# Command handler
def cmd_handler(cmd: str, isPGM: bool):
    if cmd == "ver":
        print("ziC Alpha 0.0.3") # Print ziC version
    elif cmd.startswith("say "):
        print(cmd.removeprefix("say ")) # Say the text
    elif cmd == "xcr":
        if not isPGM: # Restricted command
            pgm = [] # Reset pgm
            print("x-cell has been reset.")
    elif cmd == "pgm": # Open the program editor
        if not isPGM: # Restricted command
            print("pgm-editor\n")
            pgm = []
            pgm_edit = True
            while pgm_edit:
                pgm_input = input("#> ")
                pgm.append(pgm_input)
                if pgm_input == "exit":
                    pgm_edit = False
    elif cmd == "pgm -r": # Run pgm
        if not isPGM: # Restricted command
            pgm_index = 0
            main_loop = False
            pgm_run = True
    elif cmd == "pgm --view": # View what's in pgm
        if not isPGM: # Restricted command
            print(" ")
            for command in pgm:
                print(command)
            print(" ")
    elif cmd == "quit": # Close ziC
        quit()
    else:
        print("Unknown command: " + cmd) # Notify the user of their incorrect input

while True:
    while main_loop:
        cmd = input("^! ") # Set the command to the user input
        cmd_handler(cmd, False) # Run full command handler

    while pgm_run:
        cmd = pgm[pgm_index] # Set the command to the program index
        cmd_handler(cmd, True) # Run limited command handler
        pgm_index += 1 # Increment the program index