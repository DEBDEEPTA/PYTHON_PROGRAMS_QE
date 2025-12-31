import re
pattern = re.compile("\\d+")
val = pattern.findall("a12 b34")
print(val)