#Write a program to read through a file and print the contents of the
#file (line by line) all in upper case. Executing the program will look as follows:

inp=input('Enter a file name:')
fh=open(inp)
for line in fh:
    print(line.strip().upper())
