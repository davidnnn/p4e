def computepay(h,r):
    ot = 40
    otr = 1.5
    try:
        hrs = float(h)
        rate = float(r)
    except Exception as e:
        print("Please enter a number")
    else:
        if hrs > ot:
            e = hrs - ot #e = extra hours
            pay = (hrs - e) * rate
            otpayr = rate * otr #overtime pay rate rate times ot rate 1.5x
            otpay = otpayr * e #ot pay is otpayr x extra hours
            pay = otpay + pay
        else:
            pay = hrs * rate
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

pay = computepay(h,r)
print(pay)
