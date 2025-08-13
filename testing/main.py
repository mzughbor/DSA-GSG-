# fib using dict to not recalculate the existence one

def fib(n, my_dict={}):

    #return it if exist 
    if n in my_dict:
        return my_dict[n]
    if n == 0 or n == 1: 
        return 1 

    # pass the dictionary again to search on it 
    my_dict[n] = fib(n - 1, my_dict) + fib(n - 2, my_dict) 
    last_key = list(my_dict.keys())[-1]
    print(last_key, my_dict[last_key])
    return my_dict[n]

print("answer",fib(4))

print("answer",fib(50))
