"""
    adding 'SSC' to the front of the SSC code, to be able to join another table with the code as P.K.
"""

import sys

headers = sys.stdin.readline()
i = headers.split(",").index("SSC_CODE_2016")
if i == -1:
    sys.exit(1)

print(headers,end="")
for line in sys.stdin.readlines():
    split = line.split(",")
    split[i] = "".join(["SSC",split[i]])
    print(",".join(split), end="")
