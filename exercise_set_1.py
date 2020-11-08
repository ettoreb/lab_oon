#
# Python Basics
#

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
product = num1 * num2

if product <= 1000:
    result = product
else:
    result = num1 + num2

    print("The result is ", result)

num = 10
print(" Printing current and previous number sum in a given range ")
prev = 0
for curr in range(num):
    tot = curr + prev
print("Sum: ", tot)
prev = curr

num_list = [10, 20, 30, 40, 10]  # Arbitrary list
print(f"Are the first and the last elements of the list {num_list} the same ?")
first_element = num_list[0]
last_element = num_list[-1]
if first_element == last_element:
    result = True
else:
    result = False
print(result)

num_list = [10, 20, 33, 46, 55]
print(f"Finding numbers divisible by 5 in the list {num_list}...")
for num in num_list:
    if num % 5 == 0:
        print(num)

statement = "Emma is a designer. Emma is also an homeless."
count = 0
for i in range(len(statement)-1):
    count += statement[i:i+4] == "Emma"
print("Emma appeared ", count, "times")

list1 = [10 , 20 , 23 , 11 , 17]
list2 = [13 , 43 , 24 , 36 , 12]
list3 = []
for num in list1 :
    if num % 2 != 0:
        list3.append(num)
for num in list2 :
    if num % 2 == 0:
        list3.append(num)
print ("The merged list is ", list3)

s1 = "OpenNets"
s2 = "Optical"
middle_index = int (len (s1) / 2)
print ("Original strings are ", s1 , s2)
middle_three = s1 [: middle_index ] + s2 + s1[ middle_index :]
print ("\ nAfter appending the new string in the middle ", middle_three)

s1 = "America"
s2 = "Japan"
s3 = s1 [:1] + s2 [:1] + s1[ int( len(s1) / 2): int( len(s1) / 2) + 1] + s2[ int( len(s2) / 2): int( len(s2) / 2) + 1] + s1[ len(s1) - 1] + s2[ len(s2) - 1]
print ("Mix string is ", s3)

print ("Total counts of chars, digits, and symbols.")
input_string ="P@# yn26at ^& i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in input_string :
    if char.islower() or char.isupper():
        char_count += 1
    elif char . isnumeric ():
        digit_count += 1
    else:
        symbol_count += 1
print (f"Chars = { char_count }\ tDigits = { digit_count }\t Symbols = { symbol_count }")

input_string = "Welcome to USA. Awesome usa , isn\ ’t it?"
substring = "USA"
temp_string = input_string.lower()
count = temp_string.count(substring.lower())
print (f"The { substring } count is: ", count)

input_str = "English = 78 Science = 83 Math = 68 History = 65"
words = input_str.split ()
mark_list = [int(num) for num in words if num.isnumeric()]
total_marks = sum(mark_list)
percentage = total_marks / len(mark_list)
print (f"Mark total is { total_marks }\ tAverage is { percentage }")

input_str = "ynativepynvepynative"
count_dict = dict ()
for char in input_str:
    count = input_str.count(char)
    count_dict[char] = count
    print(count_dict)

