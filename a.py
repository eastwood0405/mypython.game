# # # x = input('?')
# # # x= list(x)

# # # num_list = []

# # # for idx,val in enumerate(x):
# # #     if val == "(":
# # #         num_list.append(idx)
# # #     if val == ")":
# # #         num_list.append(idx)
# # #     if len(num_list) == 2:
# # #         del(x[num_list[0]:num_list[1]+1])
# # #         num_list.clear()
# # # a = ""

# # # for y in x:
# # #     a += y


# # # print(a)


# # def delete_parentheses(x):

# #     x= list(x)

# #     num_list = []



# #     for idx,val in enumerate(x):
# #         if val == "(":
# #             num_list.append(idx)
# #         if val == ")":
# #             num_list.append(idx)
# #     for val1,val2 in range(0,len(num_list),2):

    
# #     a = ""

# #     for val in x:
#         a += val


#     return a

# print(delete_parentheses("11(11)11(11)11"))