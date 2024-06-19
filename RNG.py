#Importing the random module.
#Apparently there is no random function.
import random

print("Computer! What day of the month is it?");

#Using the random module to assign a variable a value between 1 and 30.
#Apparently the max value is excluded from the range, so 31 is used instead of 30.
day_of_month = random.randrange(1, 31);

#Printed the generated value.
print(day_of_month);