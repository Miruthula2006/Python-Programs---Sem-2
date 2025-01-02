import re
word="Simple regular epression example"
result=re.findall("gula",word)
print(result)

space= re.search("\s",word)
print("\nThe space is at ",space.start())
