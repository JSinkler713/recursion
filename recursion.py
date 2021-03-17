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

# Palindrome Function
"""
Input: A string
Output: Boolean
Purpose: Is the input string a palindrome?
"""
def is_palindrome(ss):
	# base case
	if len(ss) < 2:
		return True
	if ss[0] != ss[-1]:
		return False
	# recursive case
	return is_palindrome(ss[1:-1])
# print(is_palindrome("hannah"))
x = "hannah"
print(is_palindrom(x))
# print(x[1:-1])



# PRACTICE_PROBLEMS
def is_palindrome(string):
    if (len(string) < 2):
        return True
    # recursive case
    if (string[0] != string[-1]):
        #break out of loop if false along the way
        return False
    # have the function call itself without
    # the first and last char we just checked
    return is_palindrome(string[1:-1])

print(is_palindrome('abba')) # True
print(is_palindrome('TOMATO')) # False


def reverse(string):
    # base case
    if (len(string) <= 0):
        return ""
    # do some logic
    character = string[-1]
    # call the function again getting closer to base case
    return character + reverse(string[:-1])

print(reverse('tomato')) # otamot


def pretty_print(dictionary, indent=""):
    # iterate through every key in the dictionary
    for key in dictionary:
        # get the value associated with the key
        val = dictionary[key]
        # check the type of the key to see if it's another dict
        if isinstance(val, dict):
            print(f"{indent}{key}:")
            pretty_print(dictionary[key], indent + "  ")
        else:
          # it's the val isn't a dict then just print out they key and val
            print(f"{indent}{key}: {val}")

o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

pretty_print(o3)
