stack = []

def push(value : int):
    stack.insert( 0 , value)

def pop():
    stack.pop(0)

def add():
    return stack[0] + stack[1]

def sub():
    return stack[0] - stack[1]

def mult():
    return stack[0] * stack[1]

def div():
    return stack[0] / stack[1]

def parse(expr):
    e = expr.split()
    for i in e:
        if i == "help":
            print("[0] PUSH | Push a value to the stack | PUSH 10")
            print("[1] POP | Pop the first value from the stack | POP")
            print("[2] STACK | Print the stack | STACK")
            print("[3] EXIT | Exit the REPL | EXIT")
            print("[4] ADD | Add the first two numbers in the stack | ADD")
            print("[5] SUB | Subtract the first two numbers in the stack | SUB")
            print("[6] MULT | Multiply the first two numbers in the stack | MULT")
            print("[7] DIV | Divide the first two numbers in the stack | DIV")
            break
        elif i == "EXIT":
            exit()
        elif i == "PUSH":
            try:
                push(int(e[e.index(i) + 1]))
                print("Pushed. Current stack." , stack)
                break
            except:
                print(f"Must be int.")
                break
        elif i == "POP":
            try:
                pop()
                print("Popped. Current stack." , stack)
                break
            except:
                break
        elif i == "ADD":
            try:
                print(add())
                break
            except:
                break
        elif i == "SUB":
            try:
                print(sub())
                break
            except:
                break
        elif i == "MULT":
            try:
                print(mult())
                break
            except:
                break
        elif i == "DIV":
            try:
                print(div())
                break
            except:
                break
        elif i == "STACK":
            try:
                print(stack)
                break
            except:
                break
        else:
            print(f"Command {expr} not found")
            break
print("Welcome to kekscript.")
while True:
    parse(input("> "))