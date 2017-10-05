Write a program that prompts for a file name, 
then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values 
and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at 
http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Wrong file name')
    quit()
count = 0
tol = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        number = line[int(line.find(":"))+1:]
        tol = tol + float(number)
        count = count + 1
average = tol/count
print("Average spam confidence:", average)
