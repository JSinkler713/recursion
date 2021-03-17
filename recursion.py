# Base Case is where it's gonna stop

# Recursion it is a way to loop
# let i = 200
# while( i > 0) {
#     console.log(i)
#     // increment down
#     i--
# }

def navel_gazer(i=1):
    # base case so we don't go beyon 100
    if (i == 100):
        # do not call the function in the base case
        return
    print('hmm')
    print(i)
    # need a base case or we continue our loop
    return navel_gazer(i+1)

# navel_gazer()

# sum of all the integers from 0 to n where n is our input
def get_sum(n=0):
    # base case where we don't call our function
    if (n == 0):
        return 0
    # recursive case we call our function in the return
    return n + get_sum(n - 1)
    # moving towars our base case


get_sum() # 0
print(get_sum(5)) # 1+2+3+4+5