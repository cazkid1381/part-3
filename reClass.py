import re
txt = "raiin in Spain"
x = re.search("ra.{1}n", txt)
if x:
    print(True)
else:
    print(False)
    