#commented code to test variables and methods
#print("Hello World! This is a test!");

#The value the algorithm will be working with. Using strings to mix it up.
lookup = "";

#The array the the algorithm will be working with.
food = ["hot dog", "cheeseburger", "pizza", "sushi", "gyoza"];

#Search through the array. If the value is found, tell us and include where it was found. Otherwise say nothing.
if lookup in food:
    print("Found it! It's in index", food.index(lookup));