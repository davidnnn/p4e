# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lc = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    lc = lc + 1
    line.find("0")
    print(line)
print("Done")
print(lc)
