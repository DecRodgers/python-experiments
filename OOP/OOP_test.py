class Dude:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        dudestring = str("Name:"+self.name+"\nAge:"+str(self.age))
        return dudestring

    def compareDudesAge(self, other):
        if self.age == other.age:
            print(self.name+' and '+other.name+' are the same age')
        elif self.age > other.age:
            print(self.name+' is older than '+other.name)
        else:
            print(other.name+' is older than '+self.name)


dude1 = Dude('Kieran', 28)
dude2 = Dude('Nairnbot',32)
dude3 = Dude('Jopo',28)
dude4 = Dude('Scamp', 25)

dudeList = [dude1,dude2,dude3,dude4]


def main_function():
    print('hello friends!')
    print()
    print(dude1)
    print()
    print(dude2)
    print()
    print(dude3)
    print()
    print(dude4)
    print()
    print('Compare Dude Ages:')
    dude1.compareDudesAge(dude2)
    dude1.compareDudesAge(dude3)
    dude4.compareDudesAge(dude1)
    print()
    print('Sorted Dude List by age:')
    dudeList.sort(key=lambda x: x.age, reverse=True)
    for Dude in dudeList:
	    print("Name: " +str(Dude.name) + "  Age: " +str(Dude.age))


if __name__ == '__main__':
    main_function()