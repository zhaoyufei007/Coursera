Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


#input file
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
#open file
handle = open(name)
#create a dictionary
counts = dict()
#deal with data
names = list()
for line in handle:
    if len(line) < 2:
        continue
    else:
        line = line.strip().split()
        if line[0] == 'From':
            names.append(line[1])
for key in names:
    counts[key] = counts.get(key,0) + 1
#find the maximum
maximum = 0
for key,value in counts.items():
    if value > maximum:
        maximum = value
        address = key
    else:
        continue
print(address,maximum)
