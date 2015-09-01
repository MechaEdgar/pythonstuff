some_dict = {'a':1,'b':2,'c':3}

key_list = ['a','b','d']

def members (some_dict,key_list):
    counts = 0

    for item in key_list:
        if item in some_dict.keys():
            counts += 1
    return counts
    print(counts)
