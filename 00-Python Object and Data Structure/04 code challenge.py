#create an employee management system
#get information from user
#use list and format concept

employee_name = input(" please enter your user name ")
employee_lastname = input("please enter your last name ")
employee_department = input("please write your department")
information = [employee_name, employee_lastname, employee_department]
print("your information is saving....")
print("employee name is {}\nemployee last name is {}\nemployee department is {}" .format(information[0],information[1],information[2]))