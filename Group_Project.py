'''
CS 131: Python Programming 1
Project: Student Record Management System
Team Member 1 Piang Pi
Team Member 2 Dron
'''
List = []
Num_Student = 0


def addStudent():
    Name = input("Enter the student's name: ")
    if Num_Student <= 100:
        List.append(Name)
        print("Student record added successfully.")
    else:
        print("Error: Maximum number of students reached.")

def deleteStudent():
    Index = findStudent()
    if Index == -1:
        print("Error: Student record not found.")
    else:
        List.pop(List[Index])
        print("Student record deleted successfully.")

def searchStudent():
    Index = findStudent()
    if Index >= 0 and Index <= 100:
        print("Student record found.")
    else:
        print("No student records found.")
    
def displayAllStudents():
    print("Student Records:")
    print("----------------")
    for i in List:
        print(i)
    
def findStudent():
    name = input("Enter the student's name: ")
    if name in List:
        return List.index(name)
    else:
        return -1



def main():
    while True:
        print("--------------------------------")
        print("Student Record Management System")
        print("--------------------------------")
        print("1. Add a new student record")
        print("2. Delete a student record")
        print("3. Search for a student record")
        print("4. Display all student records")
        print("5. Exit")
        Option = int(input("Enter your choice (1-5): "))
        if Option == 1:
            addStudent()
        elif Option == 2:
            deleteStudent()
        elif Option == 3:
            searchStudent()
        elif Option == 4:
            displayAllStudents()
        elif Option == 5:
            print("Thank you for using the Student Record Management System!")
            break
        else:
            print("Invalid choice. Please try again between 1 to 5.")
        
main()