list1=[1,1,2]
list2=[2,3,4]


set1=set(list1)
set2=set(list2)

uncommon=list((set1-set2)|(set2-set1))
print(uncommon)

list3=[1,2,3]
list4=[4,5,6]

set3=set(list3)
set4=set(list4)

uncommon1=list((set3-set4)|(set4-set3))
print(uncommon1)


list5=[1,1,2,3,4,2]
list6=[1,3,4,5]

set5=set(list5)
set6=set(list6)

uncommon2=list((set5-set6)|(set6-set5))
print(uncommon2)
def underscore(txt):
    result=""
    vowels="aeiou"
    i=0
    while i < len(txt):
        result+=txt[i]
        if(i+1)%3==0:
            if i+1 < len(txt):
                if txt[i] not in vowels:
                    result+="_"
        i+=1
    return result

print(underscore(input("enter a word:")))           
