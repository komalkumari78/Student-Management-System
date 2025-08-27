# Student Management System
This is a **menu-driven Python program** to manage student information in a college.  
The system uses a **dictionary** to store student records, where:

- **Key** → Roll number (string, e.g., `BTECH001`)  
- **Value** → Nested dictionary containing:
  - `name`: str  
  - `branch`: str  
  - `admission_year`: int  
  - `contact`: tuple (phone: int, email: str)  
  - `academic_history`: tuple (semester: str, cgpa: float, year: int)  
##  Example Data Structure
students = {
    "BTECH001": {
        "name": "Alice Smith",
        "branch": "Computer Science",
        "admission_year": 2023,
        "contact": (123-456-7890, "alice@example.com"),
        "academic_history": ("Semester 4", 8.5, 2024)
    }
}
## Features
- Add new student
- Fetch and display student info
- Update student details
- Display all students
- Search students by branch
- Compare academic performance

## Project Structure
- `studentdata.py` → Contains student data and menu handling

## Installation
Clone this repository:
```bash
git clone https://github.com/komalkumari78/Student-Management-System.git
cd student-management
