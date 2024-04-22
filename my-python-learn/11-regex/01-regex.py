import re
str = "Take up one idea.one idea at a time"

result = re.search(r'o\w\w', str)

print(result.group())

result = re.findall(r'o\w\w', str)

print(result)

result = re.match(r'T\w\w', str)

print(result.group())

result = re.sub(r'one', 'two', str)
print(result)

result = re.split(r'one', str)
print(result)

