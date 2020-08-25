# print("enter the no")
# int(input())
# def fibincur(n):
#
#     prev=0
#     current =1
#     for i in range(1,n):
#         i=prev+current
#      #   i=prevprev+current
#         i = i + 1
#         print (i)
#
# fibincur(9)

#    please make a program to wish my mom and dad with one morning image of salam and dua and post on their no



# def fibincur(n):
#
#     prev=0
#     current =1
#     for i in range(1,n):
#          prevprev=prev
#          prev=current
#          current=prev+ prevprev
#     return current, prev, prevprev,i
#
# print(fibincur(7))

def fibincur(n):

    #prev=0
    current =1
    for i in range(1,n):
         prevprev=prev
         prev=current
         current=prev+ prevprev
    return current, prev, prevprev,i

print(fibincur(7))