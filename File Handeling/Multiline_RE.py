import re
string = """String name is itvougers
it is an education blog for 
it and cs lerners."""
"""regex1 = re.findall(r"^\w",string)
regex2 = re.findall(r"^\w",string,flags = re.MULTILINE)

print(regex1)
print(regex2)"""

regex1 = re.findall(r".+",string)
regex2 = re.findall(r".+",string,re.DOTALL)
print(regex1)
print(regex2)