#Testing Truth Table

def truth1(a, b, c):
    if (a and (b or c)):
        return True
    return False

#1
print(truth1(False, False, False))
#2
