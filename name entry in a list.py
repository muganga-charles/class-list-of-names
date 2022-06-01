# a program that allows a user to add names to a list, print the list, and replace a name in the list.
names=[]
for i in range(0,5):
    name=input("enter name")
    names.append(name)
print(names)
name=input("enter a name")
n=names.index(name)
name=input("do you want to replace the name\n")
if name=="yes":
    name=input("enter a new name")
    names.remove(names[n])
    names.append(name)
    print(names)
else:
    print(names)

