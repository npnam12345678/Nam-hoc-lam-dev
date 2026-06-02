fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "n" in x:
       newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "n" in x]
print(newlist)


newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 2]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["nam ne" for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "nam ne" for x in fruits]
print(newlist)

#sắp xếp tăng dần theo mặc định
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sắp xếp giảm dần
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#Sắp xếp danh sách dựa trên độ gần của số đó với 50:
def dayso(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = dayso)
print(thislist)

#sắp xếp như dưới đây không phân biệt được chữ hoa chữ thường gây ra kết quả không đúng đó nha
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#như này sẽ là sắp xếp không phân biệt chữ hoa chữ thường, hãy sử dụng str.lower làm hàm khóa:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#đảo ngược 1 danh sách
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 

i = 1
while i < 6:
  print(i)
  if (i == 2):
    break
  i += 1

#Một hàm với một đối số (fname). Khi hàm được gọi, chúng ta truyền vào tên, tên này được sử dụng bên trong hàm để in ra họ tên đầy đủ:
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#hàm này mong đợi 2 đối số và nhận được 2 đối số::
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#có thể gán giá trị mặc định cho các tham số. Nếu hàm được gọi mà không có đối số, nó sẽ sử dụng giá trị mặc định:
def my_function(name = "friend"):
  print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#truyền các tham số bằng cú pháp key = value
def nam_function(animal, name):
  print("toi co mot con", animal)
  print("con", animal + " ten la", name)
nam_function(animal = "dog", name = "Buddy")

#neu ko su dung tu khoa thi phai dusng so thu tu
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")

#Gửi một danh sách làm đối số:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Gửi một từ điển làm đối số:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)