# ========================================
# Mini Task: Student Record System
# ========================================

students = {}

def add_student(roll, name, age, marks):
    students[roll] = {
        "name": name,
        "age": age,
        "marks": marks,
        "grade": calculate_grade(marks)
    }
    print(f"   ✅ Student '{name}' added successfully!")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

def view_all_students():
    if not students:
        print("   No students found.")
        return
    print(f"\n   {'Roll':<6} {'Name':<15} {'Age':<5} {'Marks':<7} {'Grade'}")
    print("   " + "-" * 45)
    for roll, info in students.items():
        print(f"   {roll:<6} {info['name']:<15} {info['age']:<5} {info['marks']:<7} {info['grade']}")

def search_student(roll):
    if roll in students:
        s = students[roll]
        print(f"\n   Found! Roll: {roll}")
        print(f"   Name  : {s['name']}")
        print(f"   Age   : {s['age']}")
        print(f"   Marks : {s['marks']}")
        print(f"   Grade : {s['grade']}")
    else:
        print(f"   ❌ No student with Roll No. {roll}")

def update_marks(roll, new_marks):
    if roll in students:
        students[roll]["marks"] = new_marks
        students[roll]["grade"] = calculate_grade(new_marks)
        print(f"   ✅ Marks updated for Roll {roll}!")
    else:
        print(f"   ❌ Student not found.")

def delete_student(roll):
    if roll in students:
        name = students[roll]["name"]
        del students[roll]
        print(f"   ✅ Student '{name}' deleted.")
    else:
        print(f"   ❌ Student not found.")

# ---- DEMO RUN ----
print("=" * 50)
print("       STUDENT RECORD SYSTEM")
print("=" * 50)

print("\n--- Adding Students ---")
add_student(101, "MOUSAM",   20, 92)
add_student(102, "SANJU",     19, 85)
add_student(103, "NATASHA",    21, 73)
add_student(104, "ANUSHKA",    20, 60)
add_student(105, "RITIKA",    22, 45)

print("\n--- All Student Records ---")
view_all_students()

print("\n--- Searching for Roll 103 ---")
search_student(103)

print("\n--- Updating Marks for Roll 105 ---")
update_marks(105, 78)

print("\n--- Deleting Roll 104 ---")
delete_student(104)

print("\n--- Final Student Records ---")
view_all_students()

print("\n" + "=" * 50)
print("   Student Record System — Done!")
print("=" * 50)
