def variable():
    airtime_remaining = 15 + 3
    print(airtime_remaining)
    airtime_remaining = 7
    print(airtime_remaining)

    #loop variable
    # it should only be visible inside the loop
    for i in ['red', 'blue', 'yellow']:
        print(i)

    #python is kind in allowing access to the
    #last value of the loop variable, i.
    print("printing outside the loop")
    print(i)

    a = 5    # the value 5 is assigned to the variable a
    b = a    # After executing this line, a and b are now equal
    a = 3    # After executing this line, a and b are no longer equal

    print(a, b)

def mysum(xs):
   """ Sum all the numbers in the list xs, and return the total. """
   running_total = 0
   for x in xs:
       running_total = running_total + x
   return running_total

 def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

#TESTING AREA
def test(pass_fail):
    if pass_fail:
        return True
    else:
        return False

def testsuite():
    # Add tests like these to your test suite ...
    print(test(mysum([1, 2, 3, 4]) == 10))
    print(test(mysum([1.25, 2.5, 1.75]) == 5.5))
    print(test(mysum([1, -2, 3]) == 2))
    print(test(mysum([ ]) == 0))
    print(test(mysum(range(11)) == 55))  # 11 is not included in the list.
    print(test(sum_to(4) == 10))
    print(test(sum_to(1000) == 500500))

testsuite()
