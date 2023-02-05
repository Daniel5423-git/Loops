# Loops


Loops
Range
Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by loops. We will look at two types of loops, for loops and while loops.

Before we discuss loops lets discuss the range object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate a sequence that contains three elements ordered from 0 to 2 we simply use the following command:

(
# Use the range
​
range(3)
range(0, 3)
Image
What is for loop?
The for loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.
Let's try to use a for loop to print all the years presented in the list dates:

This can be done as follows:

# For loop example
​
dates = [1982,1980,1973]
N = len(dates)
​
for i in range(N):
    print(dates[i])     
1982
1980
1973
The code in the indent is executed N times, each time the value of i is increased by 1 for every execution. The statement executed is to print out the value in the list at index i as shown here:

Image
In this example we can print out a sequence of numbers from 0 to 7:

# Example of for loop
​
for i in range(8):
    print(i)
0
1
2
3
4
5
6
7
In Python we can directly access the elements in the list as follows:

)
# Exmaple of for loop, loop through list
​
for year in dates:  
    print (year)  
1982
1980
1973
For each iteration, the value of the variable years behaves like the value of dates[i] in the first example:

Image
We can change the elements in a list:

# Use for loop to change the elements in list
​
squares = ['red', 'yellow', 'green', 'purple', 'blue']
​
for i in range(5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
Before square  0 is red
After square  0 is white
Before square  1 is yellow
After square  1 is white
Before square  2 is green
After square  2 is white
Before square  3 is purple
After square  3 is white
Before square  4 is blue
After square  4 is white
We can access the index and the elements of a list as follows:

# Loop through the list and iterate on both index and element value
​
squares=['red', 'yellow', 'green', 'purple', 'blue']
​
for i, square in enumerate(squares):
    print(i, square)
0 red
1 yellow
2 green
3 purple
4 blue
What is while loop?
As you can see, the for loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.

Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
# While Loop Example
​
dates = [1982, 1980, 1973, 2000]
​
i = 0
year = 0
​
while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
​
print("It took ", i ,"repetitions to get out of loop.")
1982
1980
1973
It took  3 repetitions to get out of loop.
A while loop iterates merely until the condition in the argument is not met, as shown in the following figure:

Image
Quiz on Loops
Write a for loop the prints out all the element between -5 and 5 using the range function.

(
# Write your code below and press Shift+Enter to execute
for i in range(-5, 6):
    print(i)
-5
-4
-3
-2
-1
0
1
2
3
4
5
Double-click __here__ for the solution.
<!-- 
for i in range(-5, 6):
    print(i)
-->
Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.

i
# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in (Genres):
    print(i)
rock
R&B
Soundtrack
R&B
soul
pop
Double-click __here__ for the solution.
<!-- 
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)
-->
Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']

i)
# Write your code below and press Shift+Enter to execute
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i in (squares):
    print(i)
red
yellow
green
purple
blue
Double-click __here__ for the solution.
<!-- 
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)
 -->
Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = (10, 9.5, 10, 8, 7.5, 5, 10, 10)
while(i < 6):
    i = i + 1
    print(i)
# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1
10
9.5
10
8
7.5
Double-click __here__ for the solution.
<!-- 
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1
 -->
Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
# Write your code below and press Shift+Enter to execute
​
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
['orange', 'orange']
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
Double-click __here__ for the solution.
<!-- 
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
 -->
