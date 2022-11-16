

n1 = 10
emp_name = "surender"
n2 = 9.8
#mutable
list_num = [5,6,8]
list_str = ["surender","raja","ajay"]

print(list_num)
list_num[1] = 7
print(list_num)
list_num.append(9)
print(list_num)
list_num.insert(1,6)
print(list_num)
list_num.remove(9)
print(list_num)
list_num.pop(0)
print(list_num)

tuple_num = (1,2,3)
tuple_str = ("hadoop","spark")
#immutable

t_list = list(tuple_num)

t_list.append(4)

t_tuple = tuple(t_list)
print(t_tuple)


list_combination = [10,"surender",2.5]
print(list_combination)

n1 =10
if 10 > 50:
    print("trueee")
else:
    print("falseee")

if (n1>=0 and  n1<=10):
    print(f"{n1}  is lesser thn 10")
elif(n1 >=10 and n1<20):
    print(f"{n1}  is greater than 10, but lesser than 20")
elif(n1 >=20 and n1<30):
    print(f"{n1}  is  lesser than 30")
else:
    print(f"{n1}  is  greater than 30")


print("*******************************")
list_num = [1,2,3,4]
sum =0
for i in list_num:
    print(i)
    if(i<=3):
     sum = sum +i
print(sum)

length_of_list = len(list_num)
print(length_of_list)

j=0
total = 0
while(j<length_of_list): #0<7
    print(list_num[j])
    print(j)
    total = total +list_num[j]
    j=j+1

print(total)

m=0
while(m <=3):
    print(m)
    m =m +1