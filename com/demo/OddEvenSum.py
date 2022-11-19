
list_num = [2,5,8,3,9,9,8,67,5]
even_sum =0
odd_sum =0
list_city = ["chennai","bangalore","mumbai","delhi"]

def add_even(n):
    global even_sum
    even_sum = even_sum +n


def add_odd(n):
    global odd_sum
    odd_sum = odd_sum +n


for i in list_num:
    if(i%2 == 0):
        print("HI")
        add_even(i)
    else:
        print("HELLO")
        add_odd(i)

print(f"sum of odd numbers  is : {odd_sum} and sum of even numbers {even_sum}")

