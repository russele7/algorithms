# j, s = open("input.txt").readlines()
# j = set(j)

# result = len([elem for elem in s if elem in j])

# writer = open('output.txt', 'w')
# writer.write("%d" % (result))
# writer.close()

import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
 
result = 0
for ch in s:
    if ch in j:
        result += 1
 
print(result)