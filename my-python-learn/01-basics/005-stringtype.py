s = "Hello World"
print(s)

s1 = """This is fun
multiline option
is goot to write"""
print(s1)

s2 = '''This is fun
multiline option
is goot to write'''
print(s2)


print(s2[3])


print(s*3)

print(len(s1))

print(s[5:8])
print(s[:8])
print(s[5:])

print(s[-3:-1])


print(s[5:15:2])

print(s[-10:-1:2])

# reverse the strinbg
print(s[::-1])


s = "   hello world  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())


print(s.find("worl"))
print(s.find("worl",1,5))
print(s.count("wor"))
print(s.replace("world", "man"))


