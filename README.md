# odd-even-calc-generator
Thanks for taking the time to view this project.
To sum it up, this project allows a user to generate a python file which will determine if a number (within a specified range) is odd or even.
* The user will first run 'python3 odd-even-calc-generator.py' which will ask the user to enter a minimum and a maximum value.
* After these values are provided, a new file 'odd-even-calc.py' will be added to the present working directory.
* The user can run 'python3 odd-even-calc.py' and enter in a value within the range they previously entered.
* The output will determine whether or not the entered value is odd or even.

## Purpose
I think we can get caught up in efficiency which can lead to a difficult to understand solution. A great example of this is how 
we determine whether or not a number is odd or even. We usually just run (num % 2 == 0) or (num % 2 == 1) to see if a number is
odd or even. The (%) operator is sometimes difficult to understand. If-statements, on the other hand, are about as simple as it
gets. This software is incredibly easy to understand, and it is decently efficient (linear (O(n) runtime). While you can save
millions, billions, or even trillions of lines of code using (%), sometimes it's just easier to brute force it with
if-statements.
