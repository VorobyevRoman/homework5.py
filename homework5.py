immutable_var = tuple #2.Создайте переменную immutable_var
tuple = (6, 7, 8, 9, 10.5, "колбаса") #Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.\
print(tuple) #Выполните операции вывода кортежа immutable_var на экран.
#3.Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#tuple[-1] = "мясо"
#print(tuple[-1])
#не удастся изменить последний элемент(в данном случае) и вообще элементы кортежа по причине того, что элементы в кортеже не могут быть заменены.
mutable_list = [6, 7, 8, 9, 10, "cb1"] #Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
print(mutable_list)
mutable_list [3] = 22 #Измените элементы списка mutable_list.
mutable_list [4] = 33 #Измените элементы списка mutable_list.
mutable_list [5] = 'CB2' #Измените элементы списка mutable_list.
print(mutable_list) #Выведите на экран измененный список mutable_list.