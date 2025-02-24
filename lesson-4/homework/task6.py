for num in range(1, 100):  
    prime_num = True  
    for i in range(2, num): 
        if num % i == 0: 
            prime_num = False
            break 
    if prime_num:
        print(num)
