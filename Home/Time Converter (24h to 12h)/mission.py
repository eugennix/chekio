def time_converter(t):
    h = int(t[:2])
    
    # 12 -> 12 pm
    ampm = ' p.m.' if h > 11 else ' a.m.'
    
    # 00 -> 12 am
    h = h if 0 < h < 13 else abs(h - 12)
    
    return str(h) + t[2:] + ampm
    

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    print(time_converter("00:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")