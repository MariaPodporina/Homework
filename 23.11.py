list=[["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
def santa(list):
    right_list={}
    for user in list:
        name=user[0]
        if len(user)>1:
            index=user[1]
        else:
            index=None
        right_list[name]=index
    return right_list
print(santa(list))