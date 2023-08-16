# Turing machine is as powerful as any computer
X_B = {
    ("B","s1"): ("X", "R", "s2"),
    ("B","s2"): ("B", "L", "s3"),
    ("X","s3"): ("B", "R", "s4"),
    ("B","s4"): ("B", "L", "s1"),
}
# adding addition with unary digits 

ADDER = {
    ("B", "s1"): ("(", "R", "s2"),
    ("B", "s2"): ("1", "R", "s2"),
    ("B", "s3"): ("1", "R", "s2"),
    ("B", "s4"): ("+", "R", "s2"),
    ("B", "s5"): ("1", "R", "s2"),
    ("B", "s6"): ("1", "R", "s2"),
    ("B", "s7"): ("1", "R", "s2"),
    ("B", "s8"): (")", "R", "s2"),

    ("B", "s9"): ("B", "L", "s9"),
    (")", "s9"): (")", "L", "s9"),
    ("1", "s9"): ("1", "L", "s9"),
    ("+", "s9"): ("1", "R", "s10"),

    ("1", "s11"): (")", "R", "s12"),
    ("B", "s12"): ("(", "R", "s12"),
    
    
}




def simulate(instructions):
    # set up initial state, multiplied by 16 to implement addition
    tape = ["B","B"] * 16
    head = 0
    state = "s1"
    # loop:
    for _ in range(24):
        print(state.rjust(4) + ": " + "".join(tape))
        print("      " + " " * head + "^")

        # lookup an instruction
        tape[head], head_dir, state= instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else - 1
        

# simulate(ADDER)




