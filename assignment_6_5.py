text = "X-DSPAM-Confidence:    0.8475";
start = text.find("0")
int = float(text[start:])
print(int)
