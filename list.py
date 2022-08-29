list1 = [12,13,14,18,15,8,16,7,9,10]
# last 5 number list 
print(list1[-5:-1])
print(list1[-5:])
#  excluding last 3 numbers
print(list1[0:7])
print(list1[-3:])
# 4th last element 
print(list1[-4])
# reverse list 
print(list1[10::-1])

fruits = ['apple', 'banana','cherry','banana','mango',"banana"]
fruits.remove("banana")
print(fruits)
fruits.append("grapes")
print(fruits)
x=fruits.index("banana")
print(x)

n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
j=0
m=0
while i<len(n):
  if n[i]>m:
    m=n[i]
  i+=1
m2=0
while j<len(n):
  if n[j]>m2 and n[j]!=m:
    m2=n[j]
  j+=1
print(m2)

# Write a code, that counts the numbers between 20 and 40 and then print its count.

n=[50,34,23,13,27,21,45,36]
i=0
c=0
while i<len(n):
    if n[i]>20 and n[i]<40:
       c+=1
    i+=1
print(c)

# Write a code that prints the maximum in this list.
n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
m=0
while i<len(n):
    if n[i]>m:
        m=n[i]
    i+=1
print(m)


#  Write a code that the reverses the order of the items means in opposite order.
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i=-1
while i<len(places):
    print(places[i])
    i+=-1

# Write a code that prints the second maximum number in this list.
n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
j=0
m=0
while i<len(n):
  if n[i]>m:
    m=n[i]
  i+=1
m2=0
while j<len(n):
  if n[j]>m2 and n[j]!=m:
    m2=n[j]
  j+=1
print(m2)


# print odd number from the list.
n=[23,45,32,25,46,33,71,90]
i=0
while i<len(n):
    if n[i]%2==1:
        print(n[i])
    i+=1

# check if list is palindrome or not 
k=['n','i','t','i','n']
m=k
i=-1
j=[]
while i<len(k):
    j+=k[i]
    i-=1
    if j==m:
        print(k,"is palindrome")
    else:
         (k,"is not palindrome")

# to split a word without using split method
a=input("write it   ")
b=list(a)
print(b)

# to split a sentense in words
a=input("enter a sentense: ")
b=a.split(" ")
print(b)


# binary to decimal
b=[1,0,0,1,1,0,1,1]
i=-1
j=0
l=0
while j<len(b):
    k=(b[i]*2**j)
    l+=k
    i+=-1
    j+=1
print(l)

# # magic square

ms=[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
sum=0
while i<len(ms):
    j=0
    sum=0
    sum1=0
    sum2=0
    while j<len(ms[i]):
        sum+=ms[i][j]
        j+=1
    i+=1
print(sum)
i=0
while i<len(ms):
    j=0
    sum1=0
    while j<len(ms[i]):
        sum1+=ms[j][i]
        j+=1
    i+=1
print(sum1)
i=0
sum2=0
while i<len(ms):
    j=0
    while j<len(ms[i]):
        if j==i:
            sum2+=ms[i][j]
        j+=1
    i+=1
print(sum2)
if sum==sum1==sum2:
    print("it is a magic square")
else:
    print("is is not a magic square")

# Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# while i<len(list1):
#     if list1[i] in list2:
#         i+=1
#     else:
#         print(list1[i])
#         i+=1

# These are the marks of any student for the last three years. You have to calculate total marks for all the three years.
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum+=marks[i][j]
        j+=1
    i+=1
print(sum)

# This is the list of marks of a student for the last three years. You have to calculate the average marks for each year.
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
while i<len(marks):
    sum=0
    j=0
    while j<len(marks[i]):
        sum+=marks[i][j]
        average=sum//len(marks[i])
        j+=1
    print(average)
    i+=1


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]+n[j]==number:
            print(n[i],n[j])
            j+=1
        i+=1

# How to find all pairs in an array of integers whose sum is equal to the given number?
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
while i<len(n):
    j=0
    while j<i:
        if n[i]+n[j]==number:
            print(n[i],n[j])
        j+=1
    i+=1

# How to iterate on two lists together
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
while i<len(students):
    print(students[i]+str(marks[i]))
#     i+=1

# Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
counto=0
counte=0
while i<len(elements):
    if elements[i]%2==1:
        counto+=1
    else:
        counte+=1
    i+=1
print("no. of odd no.",counto)
print("number of even no.",counte)

# Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum1=0
sum2=0
i=0
while i<len(elements):
    if elements[i]%2==1:
        sum1+=elements[i]
    else:
        sum2+=elements[i]
    i+=1
print("sum of odd numbers",sum1)
print("sum of even numbers",sum2)

# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum1=0
count1=0
sum2=0
count2=0
while i<len(elements):
    if elements[i]%2==1:
        sum1+=elements[i]
        count1+=1
    else:
        sum2+=elements[i]
        count2+=1
    i+=1
averageo=sum1/count1
averagee=sum2/count2
print("number of odd numbers:",count1)
print("number of even numbers:",count2)
print("sum of odd numbers:",sum1)
print("sum of even numbers:",sum2)
print("average of odd numbers:",averageo)
print("average of even numbers:",averagee)

# How many Crorepati?
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count1=0
count2=0
count3=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        count1+=1
    elif kitna_paisa_hai[i]>=100000:
        count2+=1
    else:
        count3+=1
    i+=1
print(count1,"Crorepati")
print(count2,"Lakhpati")
print(count3,"Dilwale")

# Count Occurences
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
list1=[]
while i<len(char_list):
    list=[]
    list.append(char_list[i])
    b=char_list.count(char_list[i])
    list.append(b)
    if list not in list1:
        list1.append(list)
    b=0
    i+=1
print(list1)

# Duplicates
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list=[]
n.sort()
while i<len(n):
    if n.count(n[i])>1:
        if n[i] not in list:
            list.append(n[i])
    i+=1
print(list)

# Remove Substring
mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
a=mainStr.replace(subStr,"")
print(a)

mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
a=mainStr.replace(subStr,"on")
print(a)



