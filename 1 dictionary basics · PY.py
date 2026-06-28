# ========================================
# Program 1: Dictionary Basics
# ========================================

# --- Creating a Dictionary ---
student = {
    "name": "MOUSAM",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

print("=" * 40)
print("       DICTIONARY BASICS")
print("=" * 40)

# --- Accessing Values ---
print("\n1. Accessing Values:")
print("   Name   :", student["name"])
print("   Age    :", student["age"])
print("   Course :", student["course"])
print("   Grade  :", student["grade"])

# --- Updating Values ---
print("\n2. Updating Values:")
student["grade"] = "A+"
print("   Updated Grade:", student["grade"])

# --- Adding New Key ---
print("\n3. Adding New Key:")
student["city"] = "Delhi"
print("   City added:", student["city"])

# --- Deleting a Key ---
print("\n4. Deleting a Key:")
del student["city"]
print("   City key deleted.")

# --- Looping Through Dictionary ---
print("\n5. All Key-Value Pairs:")
for key, value in student.items():
    print(f"   {key}: {value}")

# --- Dictionary Methods ---
print("\n6. Dictionary Methods:")
print("   Keys   :", list(student.keys()))
print("   Values :", list(student.values()))
print("   Length :", len(student))

# --- Nested Dictionary ---
print("\n7. Nested Dictionary:")
school = {
    "student1": {"name": "SANJU", "marks": 95},
    "student2": {"name": "NATASHA", "marks": 88},
}
for sid, info in school.items():
    print(f"   {sid} -> Name: {info['name']}, Marks: {info['marks']}")

print("\n" + "=" * 40)
print("   Program Completed Successfully!")
print("=" * 40)
