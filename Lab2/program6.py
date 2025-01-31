def outer_function():
    global a
    a = 20
    print("a =", a)
outer_function()
print("global value of a =", a)
a = 20
global value of a = 20
