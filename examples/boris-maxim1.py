
integer = 1
string = "ABC True or False"
boolean = True
float =0.5
none = None


lists = [1,2,3,45,56,64,2,2,3]
#lists.append("ABC")

print(lists)
tupl = ("A","A")

set = set(lists)
set2 = {23,34,2,3}

print(tupl)
i = 0
# max = len(lists)
# while i<max:
#     print(lists[i])
#     i+=1

# for i in range(0,20,2):
#     if i==10:
#         continue
#     print(i)

def max_value(l:list)->integer:
    max =0
    for i in l:
        if i>max:
            max=i
    return max

def min_value(l:list)->integer:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min
max_value(lists)

i = 4
s = 0
l = []
# while s < i:
#     l.append(int(input("Enter x:")))
#     s+=1

#a = map(int,input("ABC:").split(' '))

class Human:

    number = 0

    def __init__(self, name, age):
        self.__name = name
        self._name = name
        self.age = age
        Human.number+=1
        print("i am created")

    def __private(self):
        print("I am private")

    def get_name(self):
        return self.__name

    def _protected(self):
        print("sasas")

    def set_name(self,name):
        self.__name = name

    def go(self):
        print(f"{self.__name} i go")
        self.__private()

    @staticmethod
    def static():
        print(Human.number)

class Woman(Human):
    pass

h = Human("Mark",22)
h2 = Human("Alice",22)

h.static()
h.go()
h._name = "ASAAS"
h.set_name("Mark2")
h.go()
h._protected()
h.__private()

w = Woman("alice",444)
w.go()
