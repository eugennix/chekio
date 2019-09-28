fcc = {ord(x):'_'+x.lower() for x in __import__('string').ascii_uppercase}

def from_camel_case(name):
    return  name[0].lower() + name[1:].translate(fcc)
