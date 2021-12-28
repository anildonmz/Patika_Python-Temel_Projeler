flat_list=[]

def flatten(list_):

    for i in list_:
        if type(i) == list:
            flatten(i)
        else:
            flat_list.append(i)

    return flat_list

x=flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(x)
