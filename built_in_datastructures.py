#create an empty list
my_list = []

#Appending elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the second position
my_list.insert(1, 15)

#Creating another list
my_list2 = [50, 60, 70]

my_list.extend(my_list2)

#removing the last element
my_list.pop()

#sorting in ascending order
my_list.sort()

#find and print the index of value 30
index_30 = my_list.index(30)
print("Index of value 30 :", index_30)
# for confirmation
print("Final List :", my_list)