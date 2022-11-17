myStudents= {}

print("Welcome to Student Grade Organizer!")
print()
print()

#Negative int == 0
while True:
    try: 
        howMany = int(input("How Many Students Are In Your Class?"))
        break
    except ValueError:
        print("Invalid Input: Please input a number")
        print()

count = 0

#Modify to only accept int from 0-100
while count < howMany:
    studentName = input("Enter a student name.")
    while True:
        try: 
            studentGrade = int(input("Enter a grade for the student?"))
            while studentGrade < 0 or studentGrade > 100:
                while True:
                    try: 
                        print()
                        print("Enter a number from 0-100")
                        print()
                        studentGrade = int(input("Enter a grade for the student?"))
                        break
                    except ValueError:
                        print("Invalid Input: Please input a number")
                        print()
            break
        except ValueError:
            print("Invalid Input: Please input a number")
            print()
    print()
    myStudents[studentName] = studentGrade
    count += 1

#Add more functions
def printMenu():
    print()
    print("1. List of Students")
    print("2. Change a student's grade")
    print("3. Add/Remove a student")
    print()

def executeMenu(x):
    if x == "1":
        printStudents()
    if x == "2":
        changeGrade()
    if x == "3":
        addOrDrop()

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
    for key, values in sorted(myStudents.items()):
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
            new_grade = int(input("What is the new grade for " + changeName + "?"))
            myStudents[key] = new_grade
            found = True
            break
    if found == False:
        print("Name not Found")


def addOrDrop():
    print()
    print("Add or Drop Students")
    print("----------------------")
    print()
    choice = input("Do you want to add or drop a student to your roster?: ")
    while choice != "Add"  and choice != "add" and choice != "Drop" and choice != "drop":
        print("Invalid input")
        print()
        choice = input("Do you want to add or drop a student to your roster")
    if choice == "Add" or choice == "add":
        print()
        studentName = input("Enter a new student's name: ")
        found = False
        for key, values in myStudents.items():
            if studentName == key:
                print("Student is already in the system")
                found = True
                break
        if found == False:
            myStudents[studentName] = 0
            print("Added Student:", studentName)
    if choice == "Drop" or choice == "drop":
        print()
        studentName = input("Enter a student's name to drop: ")
        found = False
        for key, values in myStudents.items():
            if studentName == key:
                print("Removed:", studentName)
                del myStudents[studentName]
                found = True
                break
        if found == False:
            print("There was no student found by the name:", studentName)

printMenu()
userOption = input("Choose an option number:")
while userOption != "Quit"  and userOption != "quit":
    if userOption != "1" and userOption != "2" and userOption != "3":
        print("Invalid Option")
        userOption = input("Choose an option number:")
    else:
        executeMenu(userOption)
        printMenu()
        userOption = input("Choose an option number:")




