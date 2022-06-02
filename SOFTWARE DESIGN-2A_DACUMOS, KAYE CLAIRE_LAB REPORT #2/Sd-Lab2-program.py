#User's input of kilometers value
kilometers = float(input("Input value in kilometers: "))

#Conversion factor
conv_fac = 0.621371

#Calculation of miles
miles = kilometers + conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles))

