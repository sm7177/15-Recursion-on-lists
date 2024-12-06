# list=["apple","banana", "mango","pineapple","orange"]

# print(list[0])
# print(list[-1])
# print(len(list))

# print(list[1:3])
# list.append("cherry")
# print(list)

# list.remove("banana")

# list.pop(3)

# list.sort()
# list.reverse()
# list.clear()











# def check(a):
#     length = len(a)
    
#     if length==1 or length==0:
#         return True
    
#     return a[0]<=a[1] and check (a[1:])

# a=[1,2,3,4,5]

# if check(a):
#     print("Yes, it is sorted.")
# else:
#     print("No, it is not sorted.")






# def ar(a):
#     length = len(a)
#     if length == 1:
#         return a[0]
        
#     return a[0]+sum(a[1:])

# a=[2,4,6,5,3,1]

# print(sum(a))






def maxno(a):
    length = len(a)
    
    if length==1:
        return a[0]
    
    return max(a[0], maxno(a[1:]))

a=[45,55,65,75,85,98]

print("largest number",maxno(a))
