#Calculate simple interest

"""
    Simple_interst(si) =
        Principal_amount(p) * Rate_of_interst(r) * Time(t) / 100
"""

pi = float(input("Enter Principal Amount : "))
r = float(input("Enter  Rate Of Interest : "))
t = float(input("Enter Time (Years) : "))

si = ( pi * r * t)/100

print("\nPrincipal Amount :",pi)
print("Rate Of Interest :  :",r)
print("Time (Years) :",t)
print("\nSimple Interest : ",si)
