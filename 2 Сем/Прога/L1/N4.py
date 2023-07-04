class Tree:
 def __init__(self, name =" ", age=2000, height=200, e = 0, p = 0):
     self.name = name
     self.age = age
     self.height = height
     self.e = e
     self.p = p

 def peres(self):
     if(self.e==0):
         self.e=1
         print("Дерево пересадили")
     else:
         print("Дерево уже было пересажено")
 def vir(self):
     if(self.p==0):
         self.p=1
         print("Дерево вырубили")
     else:
         print('Дерево уже было вырублено')

 def set_name(self, a):
     self.name = a
 def set_age(self, b):
     self.age = b
 def set_height(self, c):
    self.height = c
 def set_e(self, e):
    self.e = e
 def set_e(self, p):
    self.p = p

 def show(self):
     print(self.name)
     print(self.age)
     print(self.height)

a = input('Имя: ')
b = int(input('Возраст: '))
c = int(input("Высота: "))
e = 0
p = 0
Tree1 = Tree(a, b, c)

Tree1.set_name(a)
Tree1.set_age(b)
Tree1.set_height(c)
Tree1.peres()
Tree1.vir()
Tree1.show()