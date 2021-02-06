def get_count(num):
    if num == str(int(num)):
        return Count(num)
    else:
        return 'Not a valid number'

def is_aphabet(num):
    if num>0 and num<27:
        return 1
    else:
        return 0

def Count(code):
    if len(code) == 1:
        count = 1
    elif len(code) == 2:
        count = 1 + is_aphabet(int(code))
    else:
        count = Count(code[1:])
        if is_aphabet(int(code[:2])):
            count += Count(code[2:])
    return count

print(get_count('111')) #3

