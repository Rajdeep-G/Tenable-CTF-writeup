Description:
Below is some code that reads integers from stdin and pases a list of them to a function named "**AreNumbersEven**". Implement the "**AreNumbersEven**" function. 

```
def AreNumbersEven(numbers):
  #impliment here

# Read space delimited integers from stdin and 
# pass a list of them to AreNumbersEven()
numbers = raw_input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print even_odd_boolean_list 
```

This function takes a list of integers and returns a boolean list: True if number was even, and False if odd.

If implemented right, the attached code will print the answer returned from your function.

stdin example:
```
66  0 -47
```
stdout example:
```
[True, True, False]
```

*You can ignore default code below and instead use code from attached file. **Ensure not to print anything else during your code execution!****
Hints:
