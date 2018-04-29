fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
print(type(words))
#if word not in words:
#    continue
#else:
#    lst.append(word)
