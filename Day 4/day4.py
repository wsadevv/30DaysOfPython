

a = "Justin" == "Justin"

list_a = [1,2,3,"X"]
list_b = [1,2,3]

print(list_a == list_b)
print('Justin eq Justin is: ',a)
print(not a)

print(len('test') >= 2)

print('5 != 5:', 5 != 5)
print('50 % 2 == 0 -> ',50 % 2 ==0)
print('! 50 % 2 == 0 ->',not 50 % 2 ==0)


for i in list_a:
	try:
		if(not isinstance(i,str)):
			print(i**2)
		else:
			print(i)
		pass
	except Exception as e:
		raise e


myList = ["Avocado", "Watermelon","Mango",1,2,88,77,26,55,99,'Mail','tango','oscar','PF',9999,'Gold']

list_int = []
list_str = []

for item in myList:
	if isinstance(item,int):
		list_int.append(item)
		myList.remove(item)
	elif isinstance(item,str):
		list_str.append(item)
		myList.remove(item)
print("Itens retirados de myList que são inteiros: ",len(list_int))

print("Itens retirados de myList que são strings: ",len(list_str))