# exercise_1
s = input()
print(''.join(sorted(s)))


# exercise_2

a = int(input())
b = int(input())

print(f'{a} + {b} is {a+b}')
print(f'{a} - {b} is {a-b}')
print(f'{a} * {b} is {a * b}')
print(f'{a} / {b} is {float(a / b)}')
print(f'{a} % {b} is {a % b}')
print(f'{a} ^ {b} is {a**b}')


# exercise_3

num = int(input())

result = {}
for i in range(1, num+1):
    result[i] = i * i
    
print(result)


# exercise_4

n = int(input())
sum = n*(n+1)/2
print(f'The sum of the first {n} positive integers is {int(sum)}')

# exercise_5

s = input()

vowels = 'aeiou'
count = 0

for ch in s.lower():
    if ch in vowels:
        count+=1
print(f'Number of vowels: {count}')


# exercise_6

total = 0.0

while True:
    num = input()
    
    
    try:
        num = int(num)
        
        if num ==0:
            
            print(f"The grand total is {float(total)}")
            break
        else:
            total+=num
            print(f"The total is now {float(total)}")
    except ValueError:
        print("That wasn’t a number.")
            

# exercise_7

def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    
    result = []
    for chr in text.lower():
        if chr in reference_string:
            result.append(reference_string.index(chr))
            
        else:
            result.append(-1)
    return result

# exercise_8

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")


# exercise_9

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")
        

# exercise_10

class User:
    def __init__(self, first_name, last_name,username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        
    def describe_user(self):
        
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    
    def greet_user(self):
        print(f"Welcome back {self.username}!" )


# exercise_11

def combine_lists(list1, list2):
    combined = []
    i = 0  # pointer for list1
    j = 0  # pointer for list2
    
    # merge the two lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # add any remaining elements from list1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    # add any remaining elements from list2
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined