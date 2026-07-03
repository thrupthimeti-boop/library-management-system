import csv

print("================================")
print("Library Management System")
print("================================")

while True:
    print("\nMenu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        with open("books.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_name, author])

        print("Book added successfully!")

    elif choice == "2":
        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                print("\nLibrary Books")
                print("--------------------------")

                for row in reader:
                    print("Book ID:", row[0])
                    print("Book Name:", row[1])
                    print("Author:", row[2])
                    print("--------------------------")

        except FileNotFoundError:
            print("No books found.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
