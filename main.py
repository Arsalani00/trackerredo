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
from files import create_file, load_file
elif choice=="2":
    file_name=input ("enter the expense file name:")
    data=load_file(file_name)
print(data)
if __name__ == "__main__":
    main()
