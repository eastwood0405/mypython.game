# for x in range(1,11):
#     for y in range(x):
#         print("*",end = "")
#     print("\n",end = "")
# for x in range(1,11):
#     print("*"*x)
x = int(input("?"))
def is_sosu(x):
    if x == 1:
        return(1)
    for y in range(2,x):
        if x % y== 0 and x != 1:
            
            return ("합성수")
    else:
        return("소수")
print(is_sosu(x))
for i in range(1,51):
    if is_sosu(i) == "합성수" or is_sosu(i) == 1:
        continue

    print(i)


        



