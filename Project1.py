myStudents= {}

print("Welcome to Student Grade Organizer!")
print()
print()

howMany = int(input("How Many Students Are In Your Class?"))
count = 0

while count < howMany:
    studentName = input("Enter a student name.")
    studentGrade = int(input("Enter a grade for the student?"))
    print()
    myStudents[studentName] = studentGrade
    count += 1

def printMenu():
    print()
    print("List of Students")
    print("Change a student's grade")
    print("Add/Remove a student")
    print()

def executeMenu(x):
    if x == "1":
        printStudents()
    if x == "2":
        changeGrade()

def getLetterGrade(x):
    if x >= 97:
        return "A+"
    elif x <= 96 and x >=93:
        return "A"
    elif x <= 92 and x >= 90:
        return "A-"
    elif x <= 89 and x >= 87:
        return "B+"
    elif x <= 86 and x >= 83:
        return "B"
    elif x <= 82 and x >= 80:
        return "B-"
    elif x <= 79 and x >= 77:
        return "C+"
    elif x <= 76 and x >= 73:
        return "C"
    elif x <= 72 and x >= 70:
        return "C-"
    elif x <= 69 and x >= 67:
        return "D+"
    elif x <= 66 and x >= 63:
        return "D"
    elif x <= 62 and x >= 60:
        return "D-"
    elif x <= 59:
        return "F"
        
def printStudents():
    print()
    print("                      Student Roster")
    print("     ----------------------------------------------------") 
    print()
    for key, values in myStudents.items():
        print("Student Name:", key, "     Student Grade:", values, "     Student Letter Grade:", getLetterGrade(values))

def changeGrade():
    print()
    print("Change A Students Grade")
    print("----------------------")
    print()
    changeName = input("Enter a student's name:")

    found = False
    for key, values in myStudents.items():
        if changeName == key:
            new_grade = print("What is the new grade for", changeName + "?")
            myStudents[key] = new_grade
            found = True
            break
    if found == False:
        print("Name not Found")



printMenu()
userOption = input("Choose an option:")
while userOption != "Quit"  and userOption != "quit":
    if userOption != "1" and userOption != "2" and userOption != "3":
        print("Invalid Option")
        userOption = input("Choose an option:")
    else:
        executeMenu(userOption)
        printMenu()
        userOption = input("Choose an option:")




