Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at 
http://www.py4e.com/code3/romeo.txt
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
