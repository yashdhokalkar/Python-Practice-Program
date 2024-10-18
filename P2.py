#Q2).Interchange first and last elements using Temporary Value.

#code:
# define the list for input
list = ["Devansh","Punit","Akash","Jagannath"]
#Using temp value for interchange the element
temp = list[0]
list[0] = list[-1]
list[-1] = temp
# print the list to check the output
print(list)
