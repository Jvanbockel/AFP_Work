
name = input("You?: ")
age = input("Age?: ")

#Comma simply outputs the result
print("Hello", name , age)

#The + tries to construst a string to display
#and it will only work with int if they are
#converted to string first
print("Hello"+ name + str(age))

print("Hello {0} you are {1} years old".format(name,age))
