x=int(input("Podaj rok z przedziału 1900 - 2099: "))
a=x%19
b=x%4
c=x%7
d=(a*19+24)%30
e=(2*b+4*c+6*d+5)%7
if d+e<10:
      print("Wielkanoc jest", d+e+22, "marca")
else:
      print("Wielkanoc jest", d+e-9, "kwietnia")
