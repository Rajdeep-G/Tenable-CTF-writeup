```py
def AreNumbersEven(numbers):
	ans=list()
  #impliment here
  	for i in range(len(numbers)):
		if numbers[i]%2==0:
      		ans.append(True)
		else:
        	ans.append(False)
	return ans

# Read space delimited integers from stdin and 
# pass a list of them to AreNumbersEven()
numbers = raw_input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print even_odd_boolean_list
```