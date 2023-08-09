"""
Given a string with ones and twos separated by either - or +,
return the result of the string
"""
s = 'one+two-one+two'.replace('one', '1')
s = s.replace('two', '2')
print(eval(s))
