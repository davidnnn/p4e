hrs = input("Enter Hours:")
rate = input("Enter Rate:")
ot = 40
otr = 1.5
try:
    h = float(hrs)
    r = float(rate)
except Exception as e:
    print("Please enter a number")
else:
    if h > ot:
        e = h - ot #e = extra hours
        pay = (h - e) * r
        otpayr = r * otr #overtime pay rate rate times ot rate 1.5x
        otpay = otpayr * e #ot pay is otpayr x extra hours
        pay = otpay + pay
    else:
        pay = r * h
    print(pay)
