#using division 
-----------------------------------------------------
def product_lst(lst):
    product = 1;
    for i in range(len(lst)):
        product *= lst[i];
    return [product//a for a in lst]

print(product_lst([1,2,3,4,5]))


#Without using division
----------------------------------------------------
def product_lst(lst):
    tmp_lst = []
    for i in range(len(lst)):
        product = 1
        for j in range(i):
            product *= lst[j]
        for k in range(i+1, len(lst)):
            product *= lst[k]
        tmp_lst.append(product)
        product=1
    return tmp_lst

print(product_lst([1,2,3,4,5]))
