R=input()
list_str = R.split('], [')
list1_str = list_str[0] + ']'
list2_str = '[' + list_str[1]
def p(list_str):
    return [int(x) for x in list_str.strip('[]').split(', ')]
list1 = p(list1_str)
list2 = p(list2_str)
def function(list1,list2):
    list1=set(list1)
    list2=set(list2)
    num1=list1&list2
    num2=list1^list2
    num3=list1-list2
    num4=list2-list1
    return (len(num1),list(num1),len(num2),list(num2),len(num3),list(num3),len(num4),list(num4))
print(function(list1,list2))