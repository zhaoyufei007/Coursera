Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#input file
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
#open file
handle = open(name)
#create a dictionary
counts = dict()
#deal with data
times = list()
for line in handle:
    if len(line) < 2:
        continue
    else:
        line = line.strip().split()
        if line[0] == 'From':
            times.append(line[5])
hour = list()
for index in times:
    time = index.split(':')
    hour.append(time[0])
data = dict()
for element in hour:
    data[element] = data.get(element, 0) + 1
data = sorted(data.items())
for k, v in data:
    print(k,v)

