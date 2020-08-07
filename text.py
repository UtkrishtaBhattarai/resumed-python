myfile=open("test.txt")

myfile.seek(0)
contents=myfile.read()
print(contents)
myfile.seek(0)
print(myfile.readlines())
