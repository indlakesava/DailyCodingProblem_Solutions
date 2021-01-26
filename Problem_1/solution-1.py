supplements=set()

def check_pair(lst, sum):
    for i in range(len(lst)):
        if((sum-lst[i]) in supplements):
            return True
        supplements.add(lst[i])
    return False

print(check_pair([10, 15, 3, 7], 17))
