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

""" Sum all the numbers in the list xs, and return the total. """
def mysum(xs):   
   running_total = 0
   for x in xs:
       running_total = running_total + x
   return running_total

""" Return the sum of 1+2+3 ... n """
def sum_to(n):
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

""" Collatz 3n+1 Sequence
    Print the 3n+1 sequence from n,
        terminating when it reaches 1.
"""
def seq3np1(n):

    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")
    
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
