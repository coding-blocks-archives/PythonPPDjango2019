
class A(object):
    x = 'wwwaaaattt'
class B(A):
    pass
class C(A):
    x = 2
class D(B):
    pass
class E(D, C):
    pass

e = E()
print(e.x)
