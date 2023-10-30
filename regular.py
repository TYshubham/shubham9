# regular expression

import re

s = "this is the python program portal"
Match = re.search('portal',s)
print('start index',Match.start())
print('end index',Match.end())
print(Match)
