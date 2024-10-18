#Q3)Python | Sort a List according to the Length of the Elements.

#code:

#define the sort function
def sort_function(list):
    list = sorted(list, key=len) # key=len to calculate length of characters
    return list

#input value to display in the sorted list
list=["Apple","Banana","Mango","Pineapple","Watermelon","Kiwi"]

#print list to get final output
print(sort_function(list))
