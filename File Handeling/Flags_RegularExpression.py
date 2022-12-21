import re

string="""Site name is itvougers it is an education 
site blog for it and cs students."""

regex2 = re.findall(r"Site",string,flags=re.IGNORECASE)

print("With multiline ",regex2)