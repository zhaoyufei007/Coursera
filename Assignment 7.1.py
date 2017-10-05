Write a program that prompts for a file name, 
then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt


# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Wrong file name')
    quit()
for word in fh:
    word = word.strip()
    print(word.upper())
