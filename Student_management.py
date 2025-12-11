import json 
import os
def save_data():
    """Save all students to a JSON file"""
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
def load_data():
    global students
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            students = json.load(f)
    else:
        students = {}
load_data()  
students={}
def add_student():
    roll=input("Enter your roll number:")
    if roll in students:
        print("-----Student already exists----")
        return
    name=input("Enter student name:")
    branch=input("Enter student branch:")
    admission_year=input("Enter student admission year:")
    while True:
        try:
            admission_year=int(admission_year)
            break
        except:
            admission_year=input("Please Enter a valid admission year:")
    phone_number=input("Enter student phone number:")
    while not (phone_number.isdigit() and len(phone_number)==10):
        print("invalid phone number")
        phone_number=input("enter phone number again:")
    email=input("Enter student email:")
    while "@" not in email or not email.endswith("gmail.com"):
        print("Email must be @ and ends with gmail.com")
        email=input("please enter a valid email:")
    semester=input("Enter student semester:")
    cgpa=float(input("Enter student cgpa:"))
    year=int(input("Enter student year:"))
    students[roll]={
        "name":name,
        "branch":branch,
        "admission_year":admission_year,
        "contact":(phone_number,email),
        "academic_history":(semester,cgpa,year),
    }
    save_data()
    print("Student added successfully")
def fetch_student():
    roll=input("Enter your roll number:")
    if roll not in students:
        print("-----Student roll not exists.-----")
        return
    s=students[roll]
    print(f"Roll no :{roll}")
    print(f"Name:{s["name"]}")
    print(f"Branch: {s["branch"]}")
    print(f"Admissin year:{s["admission_year"]}")
    print(f"contact:phone:{s["contact"][0]} email:{s["contact"][1]}")
    print(f"academic history:semester:{s["academic_history"][1]} cgpa:{s["academic_history"][1]} year:{s["academic_history"][2]}")
    print("fetch student data successfully")
def update_student():
    roll=input("Enter roll no:")
    if roll not in students:
        print("------Student roll not exists------")
        return
    s=students[roll]    
    print("What do you want to update ?")
    print("1.name 2.branch 3.admission Year 4.contact 5.academic history")
    choice=input("Enter your choice you want to update:")
    if choice=="1":
        s["name"]=input("enter student name:")
    elif choice=="2":
        s["branch"]=input("Enter student branch:")
    elif choice=="3":
        s["admission_year"]=input("Enter student admission year:")
    elif choice=="4":
        phone_number=input("Enter student phone number:")
        while not (phone_number.isdigit() and len(phone_number)==10):
            print("invalid phone number")
            phone_number=input("enter phone number again:")
        email=input("Enter student email:")
        while "@" not in email or not email.endswith("gmail.com"):
            print("Email must be @ and ends with gmail.com")
            email=input("please enter a valid email:")
        s["contact"]=(phone_number,email)
    elif choice=="5":
        semester=input("Enter student semester:")
        cgpa=float(input("Enter student cgpa:"))
        year=int(input("Enter student year:"))
        s["academic_history"]=(semester,cgpa,year)
    else:
        print("Invalid input!!")
        return
    print("update student data successfully!!")
def display_all():
    if not students:
        print("-----no students available.-----")
        return
    for roll, val in students.items():
        print(f"{roll}  |   {val["name"]}  | {val["branch"]}   |    {val["academic_history"][1]}")
def find_by_branch():
    branch=input("Enter branch:")
    found=False
    print("Students in branch:-",branch)
    for roll,stud in students.items():
        if stud["branch"].lower()==branch.lower():
            print(f"Roll number: {roll} Name:{stud["name"]}")
            found=True
    if not found:
        print("----No student found in this branch----")
def compare_cgpa(students,roll1,roll2):
    if roll1 not in students or roll2 not in students:
        print("-----Roll nunber not found-----")
        return
    cgpa1 = students[roll1]["academic_history"][1]
    cgpa2 = students[roll2]["academic_history"][1]

    print(f"{roll1} have {cgpa1} CGPA")
    print(f"{roll2} have {cgpa2} CGPA")

    if cgpa1 > cgpa2: 
        print(f" {students[roll1]['name']} has higher CGPA.")
    elif cgpa1 < cgpa2:
        print(f" {students[roll2]['name']} has higher CGPA.")
    else:
        print("Both students have equal CGPA.")
    print()
while True:
    print("1 press 1 for add student")
    print("2 press 2 for call a fetch and display student information")
    print("3 press 3 for update student information")
    print("4 press 4 for display student information")
    print("5 press 5 for find student by branch")
    print("6 press 6 for compare academic performance")
    print("7 press 7 for Exit the program")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            add_student()
        case 2:
            fetch_student()
        case 3:
            update_student()
        case 4:
            display_all()
        case 5:
            find_by_branch()
        case 6:
            roll1 = input("Enter First Roll Number: ")
            roll2 = input("Enter Second Roll Number: ")
            compare_cgpa(students,roll1,roll2)
        case 7:                       
            print("Exit the program")
            break
        case _:
            print("Invalid input!")