def add_a(a):
    def add_a_b(b):
        def add_a_b_c(c):
            return a++b+c
        return add_a_b_c
    return add_a_b

ans=add_a(1)(2)(3)

print('Sum: ',ans)

ans1=add_a(1)
ans12=ans1(2)
ans123=ans12(3)

print('SUM: ',ans123)
