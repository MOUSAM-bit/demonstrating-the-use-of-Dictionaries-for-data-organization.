# ========================================
# Mini Task: Contact Book
# ========================================

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(f"   ✅ Contact '{name}' added!")

def view_contacts():
    if not contacts:
        print("   No contacts found.")
        return
    print(f"\n   {'Name':<18} {'Phone':<15} {'Email'}")
    print("   " + "-" * 55)
    for name, info in contacts.items():
        print(f"   {name:<18} {info['phone']:<15} {info['email']}")

def search_contact(name):
    if name in contacts:
        print(f"\n   Contact Found!")
        print(f"   Name  : {name}")
        print(f"   Phone : {contacts[name]['phone']}")
        print(f"   Email : {contacts[name]['email']}")
    else:
        print(f"   ❌ '{name}' not in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"   ✅ '{name}' deleted.")
    else:
        print(f"   ❌ Contact not found.")

# ---- DEMO RUN ----
print("=" * 55)
print("             CONTACT BOOK")
print("=" * 55)

print("\n--- Adding Contacts ---")
add_contact("MOUSAM",  "9876543210", "mousam@email.com")
add_contact("SANJU",    "9123456789", "sanju@email.com")
add_contact("NATASHA",   "9988776655", "natasha@email.com")
add_contact("ANUSHKA",   "9001122334", "anushka@email.com")

print("\n--- All Contacts ---")
view_contacts()

print("\n--- Searching 'NATASHA' ---")
search_contact("NATASHA")

print("\n--- Deleting 'MOUSAM' ---")
delete_contact("MOUSAM")

print("\n--- Updated Contact Book ---")
view_contacts()

print("\n" + "=" * 55)
print("   Contact Book — Done!")
print("=" * 55)
