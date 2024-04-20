#Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart #the line to extract the floating-point number
#on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you
#reach the end of the file, print out the average spam confidence

flist=[]

inp=input('Enter a file name:')
fhand=open(inp,'r')
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):

        ipos=line.find(':')
        value1=line[ipos+2:]
        value2=float(value1)

        flist.append(value2)

for i in flist:
    print(i)

avg=sum(flist)/len(flist)
print('Average spam confidence:',avg)
