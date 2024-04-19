# Alias for mymodule
import mymodule as ma
# Ignore the sufix
from mymodule import *

print(ma.sum(10,5))

print(diff(10,5))

# get all member funtions
print(dir())

# get all member funtions from math module
print(dir("math"))

# Infor on every funtion
help("math")
help("random.choice")