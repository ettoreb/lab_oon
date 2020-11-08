#
# Data Structures
#
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = []
odd_elements = list1[1::2]
print("Element at odd - index positions from list 1")
print(odd_elements)
even_element = list2[0::2]
print("Element at odd - index positions from list 2")
print(even_element)
print("Printing final list 3")
list3.extend(odd_elements)
list3.extend(even_element)
print(list3)

sample_list = [34, 54, 67, 89, 11, 43, 94]
print("Original list: ", sample_list)
element = sample_list.pop(4)
print("list after removing element at index 4", sample_list)
sample_list.insert(1, element)
print("list after adding element at index 2", sample_list)
sample_list.append(element)
print("list after adding element at the end", sample_list)

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size
for i in range(1, chunk_size + 1):
    indexes = slice(start, end, 1)
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    print("After reversing it ", list(reversed(list_chunk)))
    start = end
    if i < chunk_size:
        end += chunk_size
    else:
        end += length - chunk_size

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("printing count of each item ", count_dict)

firstList = [2, 3, 4, 5, 6, 7, 8]
secondList = [4, 9, 16, 25, 36, 49, 64]
print("fist list", firstList)
print("second list", secondList)
result = zip(firstList, secondList)
result_set = set(result)
print(result_set)

set1 = {23, 42, 65, 57, 78, 83, 29}
print("First set ", set1)
set2 = {57, 83, 29, 67, 73, 43, 48}
print("Second set ", set2)
intersection = set1.intersection(set2)
print("Intersection is ", intersection)
for item in intersection:
    set1.remove(item)

set1 = {57, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print("set1: ", set1, "\nset2: ", set2)
print("set1 is subset of set2", set1.issubset(set2))
print("set2 is subset of set1", set2.issubset(set1))
print("First set is Super set of second set -", set1.issuperset(set2))
print("Second set is Super set of First set -", set2.issuperset(set1))
if set1.issubset(set2):
    set1.clear()
if set2.issubset(set1):
    set2.clear()
print("First set ", set1)
print("Second set ", set2)

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={"Jhon":47, "Emma":69, "Kelly":76, "Jason":97}
roll_number = [47 , 64 , 69 , 37 , 76 , 83 , 95 , 97]
sample_dict = {"Jhon ": 47 , "Emma ": 69 , "Kelly ": 76 , "Jason ": 97}
print("List -", roll_number)
print("Dictionary -", sample_dict)
roll_number [:] = [ item for item in roll_number if item in sample_dict.values()]
print ("After removing unwanted elements from list ", roll_number)

speed = {"Jan":47, "Feb":52, "March":47, "April":44, "May":52, "June":53, "July":54, "Aug":44, "Sept":54}
print("Dictionary\'s values -", speed.values())
speed_list = []
for item in speed.values():
    if item not in speed_list:
        speed_list.append(item)
print("Unique list", speed_list)

sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
sample_list = [87 , 52 , 44 , 53 , 54 , 87 , 52 , 53]
print("Original list ", sample_list)
sample_list = list(set(sample_list))
print("Unique list ", sample_list)
tup = tuple(sample_list)
print("Tuple ", tup)
print("Minimum number is:", min(tup))
print("Maximum number is:", max(tup))

