book = input()
i=0

while True:
    book_insert = input()
    if book_insert == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {i} books.")
        break
    if book == book_insert:
        print(f"You checked {i} books and found it.")
        break
    i += 1

