print("\033c", end="")
print('********************************')
print('********** WELCOME TO **********')
print('******** ODD-EVEN MAKER ********')
print('********************************')
print('*** Press enter to continue ****')
input('********************************')
print("\033c", end="")
print('********************************')
print('********* INSTRUCTIONS *********')
print('1. This program will produce a')
print('another program that will')
print('determine if a number in a given')
print('range is even or odd.')
print('2. The user specifies the range')
print('the program can calculate.')
print('*** Press enter to continue ****')
input('********************************')
print("\033c", end="")

print("\033c", end="")
print('********************************')
print('********************************')
minv = int(input('Enter minimum value: '))
print("\033c", end="")
print('********************************')
print('********************************')
maxv = int(input('Enter a maximum value: '))
print("\033c", end="")

# customize filename at some point

while (minv > maxv):
    print("\033c", end="")
    print("Make sure your minimum is less than or equal to your maximum!")
    minv = int(input('Enter minimum value: '))
    maxv = int(input('Enter a maximum value: '))

f = open("odd-even-calc.py", "w")
f.write("myNum = int(input('Enter a number between "+str(minv)+" and "+
str(maxv)+": '))\n")
f.write("minv = "+str(minv)+"\n")
f.write("maxv = "+str(maxv)+"\n")
f.write("while (myNum < minv or myNum > maxv):\n")
f.write("\tprint('Enter a value within the provided range!')\n")
f.write("\tmyNum = int(input('Enter a number between "+str(minv)+" and "+
str(maxv)+": '))\n")

for i in range(minv, maxv+1):
    if i%2==0:
        f.write("if myNum == "+str(i)+":\n")
        f.write("\tprint('"+str(i)+" is even!')\n")
    else:
        f.write("if myNum == "+str(i)+":\n")
        f.write("\tprint('"+str(i)+" is odd!')\n")


f.close()

print('********************************')
print('********************************')
print('* YOUR FILE HAS BEEN GENERATED *')
print('**  Run the following command **')
print('*** to run your calculator:  ***')
print('    python3 odd-even-calc.py    ')
print('** Make sure you are in the   **')
print('****** correct directory! ******')
print('********************************')
print('********************************')
print('** ENJOY YOUR NEW CALCULATOR! **')
print('********************************')
print('********************************')



# f = open("myfile.py", "r")
# print(f.read())
