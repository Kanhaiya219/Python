#Calculate Compound interest

"""
    CI = P (1 + R/100)**T - P
    CI : Compund interest
    P : Principal Amount
    R : Rate Of Interest
    T : Time
"""

P = float(input("Enter Principal Amount : "))
R = float(input("Enter Rate Of Interest : "))
T = float(input("Enter Time ( Years ) : "))

CI = P * (1 + R/100)**T - P

print("\nPrincipal Amount : ",P)
print("Rate Of Interest : ",R)
print("Time Given ",T,"Years")
print("\nCompound Interest : ",CI)
