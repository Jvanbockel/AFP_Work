
def main():
    print("Hi, this is a program where you can convert Km/h,\n "
          "inches and micrometers to m/s, meters and millimters\n "
          "respectively\n")
    selection()


def selection():
    print("Please select a conversion by typing in the corresopnding number")
    print("If you would like to exit, enter 5")
    print("1. Kilometers per hour to Metres per second\n"
          "2. Inches to Meters\n"
          "3. Micrometers to Millimeters\n"
          "4. Fahrenheight to Celcius")
    select = int(input(": "))
    print("-------------------------------------------------------------------")

    if select == 1:
        one()

    elif select == 2:
        two()

    elif select == 3:
        three()

    elif select == 4:
        four()

    elif select == 5:
        print("Quiting...")

    elif select > 5:
        print("Please enter a valid number")
        print("\n")
        selection()

    elif select < 1:
        print("Please enter a valid number")
        print("\n")
        selection()


def one():
    print("Hi, this is a program that will convert Km/h to m/s")
    msval = int(input("Please enter a value: "))
    print("{0} km/h = {1} m/s".format(msval,kmh_ms(msval)))
    print("\n")
    selection()

def kmh_ms(km):
    ms = km * 3.6
    return ms


def two():
    print("Hi, this is a program that will convert inches to meters")
    mval = int(input("Please enter a value: "))
    print("{0} inches = {1} meters".format(mval,i_m(mval)))
    print("\n")
    selection()

def i_m(m):
    i = m * 0.0254
    return i



def three():
    print("Hi, this is a program that will convert micrometers to millimeters")
    microval = int(input("Please enter a value: "))
    print("{0} micrometers = {1} millimeters".format(microval,micrometers_millimeters(microval)))
    print("\n")
    selection()

def micrometers_millimeters(micrometers):
    millimeters = micrometers / 1000
    return millimeters

def four():
  print("Hi, this is program a program that will convert fahreneight to celcius")
  val = int(input("Please enter a value: "))
  print("{0} fahrenheight = {1} celcius".format(val,ftoc(val)))
  print("\n")
  selection()

def ftoc(fah):
     cel = (fah - 32) * 5/9
     return cel


main()