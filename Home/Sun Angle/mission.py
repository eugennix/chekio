def sun_angle(t):
    #replace this for solution
    
    h, m = int(t[:2]), int(t[3:])
    
    if h < 6 or h >= 18 and m:
        return "I don't see the sun!"
    
    mins_from_6am = (h-6)*60 + m
    
    return round(180 * mins_from_6am / (12 * 60), 2)
    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")