# ms=[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# sum=0
# while i<len(ms):
#     j=0
#     sum=0
#     sum1=0
#     sum2=0
#     while j<len(ms[i]):
#         sum+=ms[i][j]
#         j+=1
#     i+=1
# print(sum)
# i=0
# while i<len(ms):
#     j=0
#     sum1=0
#     while j<len(ms[i]):
#         sum1+=ms[j][i]
#         j+=1
#     i+=1
# print(sum1)
# i=0
# sum2=0
# while i<len(ms):
#     j=0
#     while j<len(ms[i]):
#         if j==i:
#             sum2+=ms[i][j]
#         j+=1
#     i+=1
# print(sum2)
# if sum==sum1==sum2:
#     print("it is a magic square")
# else:
#     print("is is not a magic square")