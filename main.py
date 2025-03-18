def segment_a():
    a = 1
    b = 2
    c = 5
    while a < c:
        a = a + 1
        b = b + c
    print(a, b, c)

def segment_b():
    d = 4
    e = 6
    f = 7
    while d > f:
        d = d + 1
        e = e - 1
    print(d, e, f)

def segment_c():
    g = 4
    h = 6
    while g < h:
        g = g + 1
    print(g, h)

def segment_d():
    j = 2
    k = 5
    n = 9
    while j < k:
        m = 6
        while m < n:
            print("Goodbye")
            m = m + 1
        j = j + 1

def segment_e():
    j = 2
    k = 5
    m = 6
    n = 9
    while j < k:
        while m < n:
            print("Hello")
            m = m + 1
        j = j + 1
    
def segment_f():
    p = 2
    q = 4
    while p < q:
        print("Adios")
        r = 1
        while r < q:
            print("Adios")
            r = r + 1
        p = p + 1

#call the functions to their outputs
segment_a()
segment_b()
segment_c()
segment_d()
segment_e()
segment_f()
