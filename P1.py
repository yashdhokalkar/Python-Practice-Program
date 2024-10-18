#Q1).write a Python program to swap the first and last element of the list using Python.

#code:

#define the list for input value
list=["Jitesh", "Ramesh", "Rakesh", "Yogesh"]
#Swapping the value of first element and last element with the help of index numbers
list[0], list[-1] = list[3], list[0]
#print the list for final output
print("The swapping value are:", list)
