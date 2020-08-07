import re

#Return a list containing every occurrence of "ai":

txt = "T87878he rain in Spain"
x = re.findall("^T[0-9]{6}", txt)
print(x)


y="lai29832lailai8238laLLLlai"
z=re.findall("\D",y)
print(z)

