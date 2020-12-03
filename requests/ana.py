import re
from collections import Counter
import pprint
import operator

mylines=[]
ip_list=[]
with open ('C:\\access.log.txt') as myfile:
    for line in myfile:
        mylines.append(line)
for element in mylines:
 #   print(element)
    info=re.findall(r'[0-9]+(?:\.[0-9]+){3}', element)[0]
    ip_list.append(info)
#pprint.pprint(Counter(ip_list))
c=Counter(ip_list)
print(c.most_common(10))