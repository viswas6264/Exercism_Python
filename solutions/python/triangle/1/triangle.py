def equilateral(sides):
    a,b,c=sorted(sides)
    if a==b==c and a>0:
        return True
    return False

def isosceles(sides):
    a,b,c=sorted(sides)
    if (a==b or a==c or b==c) and a>0 and a+b>=c:
        return True
    return False
    
def scalene(sides):
    a,b,c=sorted(sides)
    if (a!=b and b!=c and a!=c) and a>0 and a+b>=c:
        return True
    return False
    