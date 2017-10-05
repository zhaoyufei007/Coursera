Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.


score = input("Enter Score: ")
try:
    sco = float(score)
except:
    sco = 2.0
if sco > 1:
    print("error!")
elif sco >= 0.9:
    print("A")
elif sco >= 0.8:
    print("B")
elif sco >= 0.7:
    print("C")
elif sco >= 0.6:
    print("D")
elif sco >= 0.0:
    print("F")
else:
    print("error!")
