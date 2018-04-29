#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#print(pos)
text = "X-DSPAM-Confidence:    0.8475";
start = text.find("0")
int = float(text[start:])
print(int)
