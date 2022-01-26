class Dog():
    def __init__(self, name, age, breed, price):
        self.name = name
        self.age  = age
        self.breed = breed
        self.price = price

class Cat():
    def __init__(self, name, age, breed, price):
        self.name = name
        self.age = age
        self.breed= breed
        self.price = price

class Bird():
    def __init__(self, name, age, breed, price):
        self.name = name
        self.age = age
        self.breed= breed
        self.price= price
        
class Snake():
    def __init__(self, name, age, breed, price):
        self.name = name
        self.age = age
        self.breed = breed
        self.price = price
        
class Customer():
    def __init__(self, id, name, age, tell):
        self.id = id
        self.name = name
        self.age = age
        self.tell= tell
        
class Staff():
    def __init__(self, id,name, age):
        self.id = id
        self.name = name
        self.age = age


dog1 = Dog("มด","1","Pug","15000")
cat1 = Cat("ยีน","2","Munchkin","40000")
bird1 = Bird("ติ้ง","4","Eagle","300000")
snake1 = Snake("ชะอม","3","Rat Snake","20000")
customer1 = Customer("CT01","ภูมิ","22","08888888")
staff1 = Staff("ST01","อาร์ม","20")

print("\n                     รายการสัตว์ที่ขาย            ") 
print("    |  ประเภท  |   ชื่อ  |   อายุ   |     สายพันธุ์    |   ราคา  |")
print("    |   สุนัข    |"+"   "+dog1.name+"  |"+"  "+dog1.age+" เดือน |"+"      "+dog1.breed+"      |"+"  "+dog1.price+"  |")
print("    |   แมว    |"+"   "+cat1.name+"  |"+"  "+cat1.age+" เดือน |"+"    "+cat1.breed+"   |"+"  "+cat1.price+"  |")
print("    |   นก     |"+"   "+bird1.name+"  |"+"  "+bird1.age+" เดือน |"+"     "+bird1.breed+"     |"+"  "+bird1.price+" |")
print("    |    งู     |"+" "+snake1.name+"  |"+"  "+snake1.age+" เดือน |"+"   "+snake1.breed+"   |"+"  "+snake1.price+"  |")

print("\n                      ข้อมูลพนักงาน            ") 
print("              |  ID  |   ชื่อ  |   อายุ   |")
print("              | "+staff1.id+" |  "+staff1.name+" |   "+staff1.age+"ปี   |")

print("\n                      ข้อมูลลูกค้า            ") 
print("         |  ID  |   ชื่อ  |   อายุ   |  เบอร์โทร  |")
print("         | "+customer1.id+" |  "+customer1.name+"   |   "+customer1.age+"ปี   | "+customer1.tell+"  |")


dog1.age = "3"
cat1.price = "45000"
bird1.breed = "owl"
bird1.price = "100000"
snake1.name = "มะยม"
customer1.tell="09818928"
staff1.age = "22"
print("\n Update ข้อมูล .....")
print("\n                     รายการสัตว์ที่ขาย            ") 
print("    |  ประเภท  |   ชื่อ  |   อายุ   |     สายพันธุ์    |   ราคา  |")
print("    |   สุนัข    |"+"   "+dog1.name+"  |"+"  "+dog1.age+" เดือน |"+"      "+dog1.breed+"      |"+"  "+dog1.price+"  |")
print("    |   แมว    |"+"   "+cat1.name+"  |"+"  "+cat1.age+" เดือน |"+"    "+cat1.breed+"   |"+"  "+cat1.price+"  |")
print("    |   นก     |"+"   "+bird1.name+"  |"+"  "+bird1.age+" เดือน |"+"      "+bird1.breed+"      |"+"  "+bird1.price+" |")
print("    |    งู     |"+" "+snake1.name+"  |"+"  "+snake1.age+" เดือน |"+"    "+snake1.breed+"  |"+"  "+snake1.price+"  |")

print("\n                      ข้อมูลพนักงาน            ") 
print("              |  ID  |   ชื่อ  |   อายุ   |")
print("              | "+staff1.id+" |  "+staff1.name+" |   "+staff1.age+"ปี   |")

print("\n                      ข้อมูลลูกค้า            ") 
print("         |  ID  |   ชื่อ  |   อายุ   |  เบอร์โทร  |")
print("         | "+customer1.id+" |  "+customer1.name+"   |   "+customer1.age+"ปี   | "+customer1.tell+"  |")
