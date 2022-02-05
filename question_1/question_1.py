# Make a stack of dictionaries
stack = []
def insert_stack():
    global stack
    key = input("Enter the name of the class: ")
    Maths, Physics, Biology = [int(x) for x in input("Enter the no of Maths, Physics, Biology students: ").split()]
    val = {'Phy': Physics, 'Math': Maths, 'Bio': Biology}
    stack.append({key: val})

def remove_stack():
    stack.pop()

def show_stack():
    for i in stack:
        for k, v in i.items():
            print("{} = {}".format(k, v))
# Command line menu
while True:
    print("""
    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    """)
    choice = input("Please enter the choice (i,r,s,e): ")
    choices = {"i": insert_stack, "r": remove_stack, "s": show_stack, "e": exit}
    if choices.get(choice, False):
        choices[choice]()
    else:
        print("Invalid choice")


### OUTPUT
"""
    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): i
Enter the name of the class: XIA
Enter the no of Maths, Physics, Biology students: 10 20 30

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): I
Invalid choice

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): XIB
Invalid choice

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): i
Enter the name of the class: XIB
Enter the no of Maths, Physics, Biology students: 11 22 33

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): r

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): s
XIA = {'Phy': 20, 'Math': 10, 'Bio': 30}

    1. Insert (i)
    2. Remove (r)
    3. Show (s)
    4. Exit (e)
    
Please enter the choice (i,r,s,e): e
"""

