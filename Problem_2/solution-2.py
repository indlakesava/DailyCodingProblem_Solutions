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
