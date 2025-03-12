import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                pass
    
    def add(self):
        with open(self.filename, "a") as file:
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
            print("Employee added successfully!\n")
    

    def view(self):
        try:
            file = open(self.filename, "r")
            records = file.readlines()
            if records :
                for record in records:
                    print(record.strip())
            else:
                print("record is not available\n")
        except FileNotFoundError:
            print("no record found\n")
    def search(self):
        employee_id = input("Enter Employee ID: ") 
        try:
            file = open(self.filename, "r")
            found = False
            for record in file:
                if record.startswith(employee_id + ","):  
                    print("Employee found", record.strip())
                    found = True
                    break
            file.close()
            if not found:
                print("Employee not found\n")

        except FileNotFoundError:
            print("record not found\n")
    def update(self):
        employee_id = input("Enter Employee ID: ") 
        try:
            file = open(self.filename, "r")
            records = file.readlines()
            file.close()
            found = False
            updated_records = []
            for record in records:
                if record.startswith(employee_id + ","):
                    name_new = input("Enter new Name: ")  
                    position_new = input("Enter new Position: ") 
                    salary_new = input("Enter new Salary: ") 
                    updated_records.append(f"{employee_id}, {name_new}, {position_new}, {salary_new}\n")  
                    found = True
                else:
                    updated_records.append(record)
            if found:
                file = open(self.filename, "w")
                file.writelines(updated_records)
                file.close()
                print("Done\n")
            else:
                print("Employee not found\n")
        except FileNotFoundError:
            print("no record found\n")
    def delete(self):
        employee_id = input("Enter Employee ID: ") 
        try:
            file = open(self.filename, "r")
            records = file.readlines()
            file.close()
            found = False
            updated_records = []
            for record in records:
                if record.startswith(employee_id + ","):
                    found = True
                else:
                    updated_records.append(record)
            if found:
                file = open(self.filename, "w")
                file.writelines(updated_records)
                file.close()
                print("Done\n")
            else:
                print("Employee not found\n")
        except FileNotFoundError:
            print("no record found\n")
    def main(self):
        while True:
            print("""
            \nEmployee Management System 
            1. Add new employee record
            2. View all employee records
            3. Search for an employee by Employee ID
            4. Update an employee's information
            5. Delete an employee record
            6. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add()
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                print("exiting...")
                break
            else:
                print("please choose a valid number")

if __name__ == "__main__":
 manager = EmployeeManager()
 manager.main()

    

    