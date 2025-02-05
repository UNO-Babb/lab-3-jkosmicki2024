#TempConvert.py
#Name:Jacob Kosmicki
#Date:2/5/2025
#Assignment: Temp. converstion


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempf = input("Enter a degree in farenheit")
  tempf = int(tempf)
  tempc = (tempf - 32) * 5/9
  tempc = round(tempc , 2)

  print(tempf, "is ", tempc, "in degrees celsius.")
if __name__ == '__main__':
  main()
