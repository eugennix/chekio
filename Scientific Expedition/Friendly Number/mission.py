def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    
    # solve in positive numbers
    sign, number = ('-', -number) if number < 0 else ('', number)

    power, fraction_part, rest = 0, 0, 0    
    while number and power < len(powers) - 1:
        # cuting number by base
        number, rest = divmod(number, base)
        if number:
            # we can use next bigger power
            power += 1
            fraction_part = rest
    
    # result = number if number else rest
    result = number or rest
    
    if decimals:
        result = float(str(result) + '.' + str(fraction_part))
        res_i, res_f = f'{round(result, decimals)}'.split('.')
        res_f = res_f.rjust(decimals, '0')
        result = res_i + '.' + res_f
    else:
        result = str(result)

    power_part = powers[power] if powers else ''

    return sign + result + power_part + suffix
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    print(friendly_number(-1024000000, base=1024, suffix='iB'))
    print(friendly_number(12000000, decimals=3))
    print(friendly_number(255000000000, powers=["","k","M"]))
