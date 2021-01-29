def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def c(x,y):
        return x
    return f(c)

def cdr(f):
    def d(x,y):
        return y
    return f(d)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
