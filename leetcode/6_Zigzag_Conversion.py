def convert(s: str, numRows: int) -> str:
    buckets = ['' for i in range(numRows)]

    length = len(s)
    if length == 1 or numRows == 1:
        return s
    rounds = (length - 1) // (numRows - 1)

    buckets[0] += s[0]
    sindex = 0
    cursor = 0
    switch = 1
    for _ in range(rounds):
        for _ in range(numRows-1):
            sindex += 1
            cursor += switch
            buckets[cursor] += s[sindex]
        switch *= -1

    ostatok = (length - 1) % (numRows - 1)
    if ostatok != 0:
        for _ in range(ostatok):
            sindex += 1
            cursor += switch
            buckets[cursor] += s[sindex]

    answer = ''.join(buckets)
    return answer


s = "PAYPALISHIRING"
numRows = 1

print(convert(s, numRows))