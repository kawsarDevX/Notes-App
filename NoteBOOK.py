while True:
    print("""
    ===== NOTE BOOK =====

    1. New Note
    2. View Note
    3. Delete All Notes
    4. Exit
    """)
    try:       
        user = int(input("CHOSE: "))
        if user == 1:
            with open("notes.txt","a") as note:
                w_note = note.write(input("Write your new note: ") + "\n")
                print("your note successfuly created..")
                continue
        elif user == 2:
            try:
                with open("notes.txt","r") as note:
                    file = note.read()
                    if len(file) == 0:
                        print("You don't have any notes..")
                        continue
                    else:
                        print(file)
                        continue
            except FileNotFoundError:
                print("You don't have any notes yet.")
                continue
        elif user == 3:
            with open("notes.txt","w") as file:
                pass
            print("Your All Notes successfuly Deleted")
        elif user == 4:
            print("Thank you.....")
            exit()
    except ValueError:
        print("Please chose right option 1/2/3....")
        continue