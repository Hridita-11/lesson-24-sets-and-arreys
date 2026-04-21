import array as arr
array_num = arr.array("i",[1,3,5,3,7,3,])
print("Original arrey:"+str(array_num))
print("Number of the occurences of the number 3 in said arrey:"+str (array_num.count(3)))
array_num.reverse()
print("Reverse the orders on the items:")
print(str(array_num))

