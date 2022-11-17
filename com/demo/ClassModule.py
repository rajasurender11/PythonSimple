
class City:
    id = 10

def add():
    global id
    print("This is city method")
    id =id+20

obj = City()
print(obj.id)
add()
print(obj.id)


