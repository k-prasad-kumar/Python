#recursion

#fibonacci numbers

def fib(num):
    if num <= 1:
        return num

    return fib(num-1) + fib(num-2)

print(fib(6))


#simple recursion to find sum 
#ex: (5) = 5+4+3+2+1 = 15

def find_sum(num):
    if num == 1:
        return num
    return num + find_sum(num - 1)

print(find_sum(5))


#even numbers
#ex: (8) = 8 -> 4 -> 6 -> 2 

def even_num(num):
    if num  % 2 != 0:
        print("Enter Even Number Only")
    else:
        print(num)
        if num == 2:
            return num
        return even_num(num-2)

even_num(9)


#factorial nums

def fact(num):
    if num == 1:
        return num

    return num * fact(num-1)

print(fact(6))