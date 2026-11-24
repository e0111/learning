'In order to understand recursion, you msut first understand recursion.'
'Recursion is the act of calling a function from inside the function itself.'


def double(x):
    y = x*2
    print(y)
    double(y)
# double(1)
'This would keep going on till infinity.'
'To fix this issue, we use IF statement.'
'This IF statement is what is represented as a "base case"'

def double(x):
    y = x*2
    if y < 600: 
        print(y)
        double(y)
    else:
        return y 
# double(1)

'Count backwards from a number that user passes till 0.'
def countDown(num):
    if num >= 0:
        print(num)
        num -= 1
        countDown(num)
    else:
        return -1
# num = int(input("Enter Number: "))
# countDown(num)

'Factorial Calculator'
def factorial(n):
    if n < 0:
        print("Negative numbers don't have factorials and " \
        "we are sadly not considering the gamma function for now.")
    elif n == 0:
        return 1 
    else:
        return(n* factorial(n -1))

# print(factorial(7))