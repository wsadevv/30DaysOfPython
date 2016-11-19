#LISTS

abc = "Heel"
print(abc)

#list

myList = ['some string', 'second thing',123,"test"]
#add new item
myList.append("new object")
#remove last item

print("Before pop: ",len(myList))

#i can set the index at pop method
myList.pop(0)
print(myList)
#list size
print(len(myList))
myList.append("Cooool")
print(myList)
print(myList[len(myList)-1])

#DICTIONARIES and TUPLES

#<K,V> -> keys and values

myDictionary = {
"abcd" : "First four letters",
"1234"   : "First four numbers"}

print(myDictionary["1234"])

#TUPLES

#tup = ("abc","abc")

tup = (("abcd","abcd"),("more","more"),("yet","yet"))

print(tup[0])

#end of script

