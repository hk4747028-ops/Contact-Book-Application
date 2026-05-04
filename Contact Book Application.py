class contactBook:
    
    global contact_List
    global contact_name
    contact_List=[]
    contact_name=[]
    def __init__(self,name,number):
        self.isname=name
        self.isnumber=number

    def add_number(self):
        contact_List.append(self.isnumber)
        return "your number added successfully"
    def add_name(self):
        contact_name.append(self.isname)
        return "your name added successfully"
    
    def view(self):
        print("choose 1 to find name through number")
        print("choose 2 to find number through name")
        num=int(input("enter your choosen number"))

        if num==1 :
            if self.isname in contact_name:
                print (f"{self.isname}")
        elif num==2:
            if self.isnumber in contact_List:
                print (f"{self.isnumber}")
        else:
            print("not found")

    def delete(self):
        contact_List.clear() and contact_name.clear()
        return  "your contact deleted successfully"
    print(contact_List)
    print(contact_name)
    
    def search(self):
        
        return contact_List and contact_name
        
    
contact1=contactBook("karan",26738954)
print(contact1.add_name())
print(contact1.add_number())
print(contact1.view())
print(contact1.delete())
print(contact1.search())





























