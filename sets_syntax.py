
set1 = {23,56,"hello","benz", 89}
set2 = {89,"benz", "cricket", "this", 90}

print("set1 is : ",set1)
print("set2 is : ", set2)

#intersection
print("intersection of set1 and set2 is :", set1.intersection(set2))
print("intersection of set1 and set2 is :", set1 & set2)

#union
print("union of set1 and set2 is :", set1.union(set2))
print("union of set1 and set2 is :", set1 | set2)

#difference   A-B
print("difference of set1 and set2 is :", set1.difference(set2))
print("difference of set1 and set2 is :", set1 - set2)

#symmetric differnce    (A-B) UNION (B-A)
print("symmetric difference of set1 and set2 is :", set1.symmetric_difference(set2))
print("symmetric difference of set1 and set2 is :", set1 ^ set2)

#issuperset   return true or false
print("is set1 superset wrt to set2", set1.issuperset(set2))
print("is set1 superset wrt to set2", set1 >= set2)

#issubset   return true or false
print("is set1 subset of set2", set1.issubset(set2))
print("is set1 subset of set2", set1 <= set2)

#isdisjoint   return true or false
print("is set1 and set2 disjoint :", set1.isdisjoint(set2))

#existence of element in set check
print("is element 'benz' in set1", "benz" in set1)

#add element to a set
set1.add("ball")
print("set1 after addition of one element is", set1)

#discard and remove
#if key with discard is  not in set then no error will be issued but with remove   KeyError will be issued
set1.discard("bena")
print("set1 after removal of 'bena'  is :", set1)
# set1.remove("bena")
# print("set1 after removal of 'bena'  is :", set1)


#set operations inplace versions for union,intersection, difference, symmetric difference
set1 |= set2
print("set1 after inplace union is ", set1)
set1.update(set2)
print("set1 after inplace union is ", set1)


#inplace intersection
set1 &= set2
print("set1 after inplace intersection is ", set1)
set1.intersection_update(set2)
print("set1 after inplace intersection is ", set1)


#inplace difference
set1 -= set2
print("set1 after inplace difference is ", set1)
set1.difference_update(set2)
print("set1 after inplace difference is ", set1)

#inplace symmetric difference

set1 ^= set2
print("set1 after inplace symmetric difference is ", set1)
set1.symmetric_difference_update(set2)
print("set1 after inplace symmetric difference is ", set1)


#use frozen set for set of sets  eg:  {{1,2,3 }, {56,57}}
print({frozenset({1,2,3}), frozenset({56,57})})


#set vs multisets     in set {'1', 'b' , 'c' , 'b' }  is not possible to keep b twice

list1= [ '1','b','c','b']
from collections import Counter
counter1 = Counter(list1)
print(counter1)




