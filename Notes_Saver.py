FILE = "notes.txt"

def add_note():
    note = input("Write your note: ")
    with open(FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open(FILE, "r") as f:
            notes = f.readlines()
            if not notes:
                print("No notes found.")
            else:
                for i, n in enumerate(notes, 1):
                    print(i, n.strip())
    except FileNotFoundError:
        print("No notes file yet.")

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
