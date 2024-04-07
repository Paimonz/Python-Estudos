'''Create a Python program that takes the following input from a user (via the command-line).
• Students full name
• Exam score 1 (out of 100)
• Exam Score 2 (out of 100)
• Exam Score 3 (out of 100)
• Attendance Percentage (out of 100)
If the user enters an invalid value for any input, then discontinue the program.
With this input, produce the following and print the values:
• Average Exam Score
• The students initials
• The students second name
• The students overall grade given their average exam score
o The grade thresholds are given below. If a student has an attendance less than 75%,
they automatically receive an F grade
A 85-100; B 70-85; C 55-70; D 40-55; F <40'''

cont = 'YES'
prog = 'YES'
name = ""
exam1 = ""
exam2 = ""
exam3 = ""
aten = ""

while cont == 'YES':
    cont = input("Would you like to start a new analysis?\n[Yes]x[No]: ").upper()
    if cont != 'YES':
        break
    try:
        name = str(input("Please, digit your full name:").upper())
        exam1 = int(input("Insert your Exam Score 1: "))
        exam2 = int(input("Insert your Exam Score 2: "))
        exam3 = int(input("Insert your Exam Score 3: "))
        aten = float(input("Insert your Attendance in Percentage: "))
        prog = "YES"
    except ValueError:
        print("You must write your full name using letters\nYour Exam Score must be in integer number\nYour Attendance must be in float numbers")
        #cont = input("Do you want to continue?\n[Yes]x[No]: ").upper()
    if prog == "YES":
        n = type(name)
        e1 = type(exam1)
        e2 = type(exam2)
        e3 = type(exam3)
        at = type(aten)
    if n == str and e1 == int and e2 == int and e3 == int and at == float:
        initial = next(zip(*name.split()))
        print("The initials of your name are: {}".format(initial))
        print("Your full name is : {}".format(name))
        print("Your first name is: {}\nYour second name is: {}".format(name.split(' ')[0], name.split(' ')[1]))
        med = (exam1+exam2+exam3)/3
        print("Your mean score is: {}".format(med))
        if med >= 85 and aten > 75:
            print("Your classification is A")
        elif 75 < med <= 84 and aten >= 75:
            print("Your classification is B")
        elif 55 < med <= 74 and aten >= 75:
            print("Your classification is C")
        elif 40 < med <= 54:
            print("Your classification is D")
        else:
            print("Your classification is F")
print("Program Finalized!")
