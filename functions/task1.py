#task1
def GramToOunces(grams):
    return 28.3495231 * grams
#task2
def FahrenheitToCelcius(fahrenheit):
    return ((5/9)*(fahrenheit-32))
#task3
def solve(numheads,numlegs):
    for rabbit in range(0,numheads):
        chickens = numheads - rabbit
        if((rabbit*4)+(chickens*2)==numlegs):
            print(f"Chickens: {chickens}, Rabbits: {rabbit}")
            break

# solve(35,94)
#task4
def filter_prime(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    
                    break
            else:
                return num
            
#task5
from itertools import permutations

def allperm(str):
    perm = permutations(str)
    for i in list(perm):
        return i
    
#task6

def reversedSentence(str):
    splitted = str.split(" ")
    splitted[::-1]
    for i in splitted:
        return i

#task7
    
def has_33(nums):
    for i in range(0,len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3):
            return True
            break
        else: return False

print(has_33([1, 3, 3]))

#task8
def spy_game(nums):
    myString = ""
    for i in nums:
        if int(i)==0:
            myString+="0"
        elif int(i)==7:
            myString+="7"
    x=myString.find("007")
    if x==-1:
        return False
    else:
        return True
inp = input("Введите числа: ")
nums=inp.split()
if spy_game(nums)==True:
    print("True")
else:
    print("False")

#task9

def volume(R):
    V = (4*3.14*float(R)**3)/3
    return V
r = input("Введите радиус сферы: ")
print(volume(r))

#task10
def volume(R):
    V = (4*3.14*float(R)**3)/3
    return V
r = input("Введите радиус сферы: ")
print(volume(r))