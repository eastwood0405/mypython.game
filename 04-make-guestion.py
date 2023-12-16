# import random
# def make_Question():
#     a=random.randint(1,40)
#     b=random.randint(1,20)
#     op=random.randint(1,4)
#     q=str(a)
#     if op==1:
#         q=q+"+"
#     if op==2:
#         q=q+"-"
#     if op==3:
#         q=q+"*"
#     if op==4:
#         q=q+"/"
#     q=q+str(b)
#     return q
# sc1=0
# sc2=0
# for x in range(5):
#     q=make_Question()
#     print(q)
#     ans=input("=")
#     r=float(ans)
#     if eval(q)==r:
#         print("정답")
#         sc1=sc1+1
#     else:
#         print("오답")
#         print("정답:",eval(q))
#         sc2=sc2+1
# print("정답:",sc1,"오답",sc2)
# if sc2==0:
#     print("천재")
# if sc2==5:
#     print("바보")
# m = 10
# for  i in range(m,0,-1):
#     print(" "*(i-1)+"*"*((m-i)*2+1))
# for i in range(m-1,0,-1):
#     print(" "*(m-i)+"*"*(i*2-1))

# for  i in range(m,0,-1):
#     print(" "*(i-1)+"*"*((m-i)+1))
# for i in range(m-1,0,-1):
#     print(" "*(m-i)+"*"*i)

# for  i in range(m,0,-1):
#     print("*"*i+" "*(m-i))
# for i in range(m-1,0,-1):
#     print("*"*(m-i+1)+" "*(i-1))

# for i in range(m,0,-1):
#     print("*"*(m-i+1)+" "*((i-1)*2)+"*"*(m-i+1))
int =str(input("?"))
int = list(int)
str = ""
for idx,val in enumerate(int):
    if val == "1" :
        if idx == len(int)-1:
            str= str+"일"
        
    if val == "2" :
        str= str+"이"
    if val == "3" :
        str= str+"삼"
    if val == "4" :
        str= str+"사"
    if val == "5" :
        str= str+"오"
    if val == "6" :
        str+= str+"육"
    if val == "7" :
        str= str+"칠"
    if val == "8" :
        str= str+"팔"
    if val == "9" :
        str= str+"구"
    if len(int) - idx %4 == 2:
        if not val == "0":
            str  = str+"십"  

    if len(int) - idx %4== 3:
        if not val == "0":
            str  = str+"백"
    if len(int) - idx %4== 4:
        if not val == "0":
            str  = str+"천"
print(str)                                                                        








                                                        
                                                             