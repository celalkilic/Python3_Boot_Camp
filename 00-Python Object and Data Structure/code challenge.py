#Challenge1
#create an application. get 3 numbers from the user and multiply them
#print the result on the console using format
#hint: int(input('x: '))

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
multiply = a*b*c
print("{}*{}*{}={}".format(a,b,c,multiply))
#challenge2
#get inpu height and weight from user. then calculate the BMI
#hint: weight/(height**2)

height = float(input('height: '))
weight = float(input('weight: '))
BMI = weight/(height**2)
print("your weight is {}\nyour heigh is {}\n your BMI is {}".format(weight,height,BMI))