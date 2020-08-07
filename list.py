my_list=[1,2,3]
my_list=["String", 100, 23.2]
my_list=[1,2,3]
another_list=[4,5]
print(my_list[0]) #indexing
newlist=my_list+another_list #list concadination
print(newlist)

#prints element or things
print(len(my_list)+"I")

#change list element and value
newlist[0]="1.1" 


##adds item at the end of list
newlist.append("6") 
print(newlist)


#deletes the last item
newlist.pop()


#removes at specific index
newlist.pop(2)
print(newlist)


#sort by numbering order
numbers=[1,3,2,4,6,7,5]
numbers.sort() #helps in sorting
print(numbers)


#reverse everything in list
numbers.reverse()
print(numbers)