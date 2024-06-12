#Function will call itself and decrease given number by 1 so long as said number is greater than 0.
#Just like JS and PHP, it doesn't seem like you need a return statement for every condition.
def countdown(number):
    if number < 0:
        print("I can't do a countdown with this number!");
        #return 0;
    elif number > 0:
        print(number);
        return countdown(number - 1);
    else:
        print("Liftoff!");
        #return 0;

#Calling the countdown function.
countdown(10);