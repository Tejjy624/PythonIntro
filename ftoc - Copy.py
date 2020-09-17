#Homework 1
#Tejvir Sohi
#ECS 36A Winter 2019

#The problem in the original code is that 1st: The user input must be changed
#into int or float. Float would be the best choice since there are decimals to
#work with. The 2nd problem arised due to an extra slash when defining ctemp.
#Instead of 5//9, it should be 5/9 to show 5 divided by 9


#User enters temp in fahrenheit
ftemp = float(input("Enter degrees in Fahrenheit:"))
#Formula calculates the temp in degrees C
ctemp = (5/9)*(ftemp - 32)
#Summarizes what the temps are
print(ftemp, "degrees Fahrenheit is", ctemp, "degrees centigrade")
