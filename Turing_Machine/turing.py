# Turing machine is as powerful as any computer
X_B = {
    ("B","s1"): ("X", "R", "s2"),
    ("B","s2"): ("B", "L", "s3"),
    ("X","s3"): ("B", "R", "s4"),
    ("B","s4"): ("B", "L", "s1"),
}
# 
def simulate(instructions):
    # set up initial state
    tape = ["B","B"]
    head = 0
    state = "s1"
    # loop:
    for _ in range(8):
        print(state.rjust(4) + ": " + "".join(tape))
        print("      " + " " * head + "^")

        # lookup an instruction
        tape[head], head_dir, state= instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else - 1
        

simulate(X_B)