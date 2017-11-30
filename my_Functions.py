#Creates a main function that rins when this file is executed
def main():
  print("hello")
  print("This program will ask you for a fahreneight temperature")
  print("_______________________________________________")
  val = int(input("Please enter a value: "))
  print("{0} fahrenheight = {1} celcius".format(val,ftoc(val)))

#Create a function to convert fahrenheight to clesius
def ftoc(fah):
     cel = (fah - 32) * 5/9
     return cel



main()