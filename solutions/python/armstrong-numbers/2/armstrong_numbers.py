'''Version using in this program'''
import sys
def print_python_version():
    print(sys.version)
def is_armstrong_number(number):
    total=0
    for digit in str(number):
        total+=int(digit)**len(str(number))
    if total==number:
        return True
    return False