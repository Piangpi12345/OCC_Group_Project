'''
CS 131: Python Programming 1
Project: Student Record Management System
Team Member 1 Piang Pi
Team Member 2 Dron
'''

List = [] # list for student names
Num_Student = 0 

def addStudent():
    """
    Adds a new student to the list.
    1. Asks the user to input the student's name.
    2. Checks if the list has reached its maximum (100 students). 
    - If maximum is reached, prints an error message.
    - If there is space, add the student name to the list and prints a success message.
    """
    global Num_Student  # Use global inside the function to change Num_Student
    Name = input("Enter the student's name: ")
    if Num_Student < 100: #check
        List.append(Name) # Add student to the list
        Num_Student += 1 # Increment student count 
        print("Student record added successfully.")
    else:
        print("Error: Maximum number of students reached.")

def deleteStudent():
    """
    Deletes a student from the list.
    1. Uses findStudent() to get the index of the student's name in the list.
    2. If found, deletes the student, reduces the number of students by 1, and prints a success message.
    3. If not found, prints an error message.
    """
    global Num_Student  # Use global inside the function to change Num_Student
    Index = findStudent() # Find student index
    if Index == -1:
        print("Error: Student record not found.")
    else:
        List.pop(Index) # Delete student at found index
        Num_Student -= 1 # decrement student count 
        print("Student record deleted successfully.")

def searchStudent():
    """
    Searches for a student record in the list.
    1. Uses findStudent() to get the index of the student's name.
    2. If found, prints a success message.
    3. If not found, prints an error message.
    """
    Index = findStudent()
    if Index >= 0 and Index < 100:
        print("Student record found.")
    else:
        print("No student records found.")
    
def displayAllStudents():
    """
    Displays all student records.
    1. Checks if there are any student records.
    2. If no records exist, prints an error message.
    3. If records exist, prints each student's name on a new line.
    """
    print("Student Records:")
    print("----------------")
    if List:
        for i in List:
            print(i)
    else:
        print("Error: No student records found.")
    
def findStudent():
    """
    Finds the index of a student in the list.
    1. Asks the user to input the student's name.
    2. Searches the list for the name.
    3. Returns the index of the student if found; otherwise, returns -1.
    """
    name = input("Enter the student's name: ")
    if name in List:
        return List.index(name) #Return index if found
    else:
        return -1 # Return -1 if not found

def main():
    """
    Main function to display the menu and call other functions based on user choice.
    Keeps displaying the menu until the user selects option 5 (Exit).
    """
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
        print()
        
main() # Run the main function to start the program