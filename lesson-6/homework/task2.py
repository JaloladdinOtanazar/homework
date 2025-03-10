import os  

def add():
    with open("employees.txt", "a") as file:  
        id = input("Enter Employee ID: ")  
        name = input("Enter Name: ")  
        position = input("Enter Position: ") 
        salary = input("Enter Salary: ") 
        file.write(f"{id}, {name}, {position}, {salary}\n")  
        print("Done!\n")
def view():
    try:
        file = open("employees.txt", "r")
        records = file.readlines()
        if records :
            for record in records:
                print(record.strip())
        else:
            print("record is not available\n")
    except FileNotFoundError:
        print("no record found\n")
def search():
    id = input("Enter Employee ID: ") 
    try:
        file = open("employees.txt", "r")
        found = False
        for record in file:
            if record.startswith(id + ","):  
                print("Employee found", record.strip())
                found = True
                break
        file.close()
        if not found:
            print("Employee not found\n")

    except FileNotFoundError:
        print("record not found\n")
def update():
    id = input("Enter Employee ID: ") 
    try:
        file = open("employees.txt", "r")
        records = file.readlines()
        file.close()
        found = False
        updated_records = []
        for record in records:
            if record.startswith(id + ","):
                name_new = input("Enter new Name: ")  
                position_new = input("Enter new Position: ") 
                salary_new = input("Enter new Salary: ") 
                updated_records.append(f"{id}, {name_new}, {position_new}, {salary_new}\n")  
                found = True
            else:
                updated_records.append(record)
        if found:
            file = open("employees.txt", "w")
            file.writelines(updated_records)
            file.close()
            print("Done\n")
        else:
            print("Employee not found\n")
    except FileNotFoundError:
        print("no record found\n")
def delete():
    id = input("Enter Employee ID: ") 
    try:
        file = open("employees.txt", "r")
        records = file.readlines()
        file.close()
        found = False
        updated_records = []
        for record in records:
            if record.startswith(id + ","):
                found = True
            else:
                updated_records.append(record)
        if found:
            file = open("employees.txt", "w")
            file.writelines(updated_records)
            file.close()
            print("Done\n")
        else:
            print("Employee not found\n")
    except FileNotFoundError:
        print("no record found\n")
def main():
    while True:
        print("\nEmployee Management System") 
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            print("exiting...")
            break
        else:
            print("please choose a valid number")

if __name__ == "__main__":
    main()

