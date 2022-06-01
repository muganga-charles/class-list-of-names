
class names:#class of names
    def __init__(self):#constructor
        self.names=[]#list of names
    def add_names(self):#add names
        for i in range(0,5):#allows input of five names
            name=input("enter name : ")
            self.names.append(name)#adds name to list
    def print_names(self):#prints  all  the names
        print(self.names)
    def replace_names(self):#replaces names
        name=input("enter a name in the list")#selects a name from the list
        n=self.names.index(name)#finds the index of the name
        choice=input("do you want to replace the name \n")
        if choice=="yes":#if the choice is right then changes the name
            name=input("enter a new name : ")
            self.names[n]=name#changes the name
            print(self.names)
        else:
            print(self.names)
#allowing a user to access the program
def main():
    name=names()#creates an object of the class
    name.add_names()#calls the add_names method
    name.print_names()#calls the print_names method
    name.replace_names()#calls the replace_names method
main()
