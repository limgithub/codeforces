import re

sequence = raw_input()
pattern = raw_input() + ".*" + raw_input()

print ['fantasy','forward','backward','both'][(type(re.search(pattern,sequence))
    != type(None))+ (type(re.search(pattern,sequence[::-1])) != type(None)) * 2]
