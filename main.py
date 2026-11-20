def  main():
    print("1: Create the expense file")
    print("2: load the expense file")
    print("3: Export the expense file to csv")
    print("4: Edit the expense categories")
    print("5: Add the expenses")
    print("6: Exit")
    choice = input("enter your choice:")
    if choice == "1":
        file_name=input("type a new expense file name:")
        create_file(file_name)
if __name__ == "__main__":
    main()
