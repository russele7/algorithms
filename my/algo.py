reader = open('input.txt', 'r')
a, b = [int(n) for n in reader.readline().split(" ")]
reader.close()

writer = open('output.txt', 'w')
# writer.write("%d" % (a+b))
writer.write(f'{a+b}')
writer.close()