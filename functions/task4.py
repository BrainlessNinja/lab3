def filter_prime(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    
                    break
            else:
                return num