import re

pattern = r" [A-Z]+ one" 
text = ''' Hello everyone ,Noone is with you till 
your life end you shold onlyone who stands for you 
in your life .Everyone come for a reason  ''' 

matches = re.findall(pattern,text)
print(re.match(pattern,text))
print(matches)