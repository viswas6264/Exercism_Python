def equilateral(sides):
    side_one, side_two, side_three=sorted(sides)
    if side_one==side_two==side_three and side_one>0:
        return True
    return False

def isosceles(sides):
    side_one, side_two, side_three=sorted(sides)
    if (side_one==side_two or side_two==side_three or side_one==side_three) and side_one>0 and side_one+side_two>=side_three:
        return True
    return False
    
def scalene(sides):
    side_one, side_two, side_three=sorted(sides)
    if (side_one!=side_two and side_two!=side_three and side_one!=side_three) and side_one>0 and side_one+side_two>=side_three:
        return True
    return False
    