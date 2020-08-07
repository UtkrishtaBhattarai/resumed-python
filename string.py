name="ramram"

#len helps in finding the number of alphabets 
print(len(name))

mystr="Hello World"
print(mystr)

#if i want single character
print(mystr[0])

#reverse indexing
print(mystr[-2])

#slicing
mystr="abcdefghijk"
print(mystr[0:3])
print(mystr[::2])

#immutability, concadination
name="SAM"
print("R"+name[1:3])

#MULTIPLICATION USING LETTER
letter="z"
print(10*letter)

#string object function
x="Hello World"
print(x.upper())
print(x.lower())
print(x.split()) #split the string 

y="Hi this is a string"
print(y.split("i")) #split on any letter i want
print(y)

#string formatting 
print("Hello")
print("This is a string {}".format("Inserted"))
print("This is a string {} {} {}".format("Inserted", "INTO","THE"))
print("ihi ihi {2} {2} {1} {0}".format("fox","hen","dog"))

#assigning key words
print("The {b} {f} {q}".format(f="fox", b="brown", q="quick")) 

#formatted string literal
name1="Hose"
print(f"hello {name1}")

age=3
print(f"Name is {name1} and age is {age}")



