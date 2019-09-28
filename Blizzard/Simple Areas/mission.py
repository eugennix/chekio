def simple_areas(*args):
    if (L:=len(args)) == 1:
        # 'circle'
        d = args[0]
        return round(__import__('math').pi * d * d / 4, 2)
    elif L == 2:
        # 'rectangle'
        a, b = args
        return round(a * b, 2)
    elif L == 3:
        # 'triangle'
        a, b, c = args
        p = (a + b + c) / 2
        return round((p*(p-a)*(p-b)*(p-c))**0.5, 2)
    else:
        # 'wrong input'
        return None
