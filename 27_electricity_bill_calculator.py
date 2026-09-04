# Electricity Bill Calculator using Slabs

# Taking total units consumed from the user
units = int(input("Enter total units consumed: "))

# Slab rates:
# 0-100 units    -> Rs 3 per unit
# 101-200 units  -> Rs 4.5 per unit
# 201-300 units  -> Rs 6 per unit
# 300+ units     -> Rs 7 per unit

if units <= 100:
    # If total units are 100 or less, entire amount is charged at first slab rate
    bill = units * 3

elif units <= 200:
    # First 100 units charged at slab 1 rate (3)
    # Remaining units (units - 100) charged at slab 2 rate (4.5)
    bill = (100 * 3) + (units - 100) * 4.5

elif units <= 300:
    # First 100 units -> slab 1 charge
    # Next 100 units -> slab 2 charge
    # Remaining units (units - 200) -> charged at slab 3 rate (6)
    bill = (100 * 3) + (100 * 4.5) + (units - 200) * 6

else:
    # Full charge for all three previous slabs (100+100+100 units)
    # Remaining units (units - 300) charged at slab 4 rate (7)
    bill = (100 * 3) + (100 * 4.5) + (100 * 6) + (units - 300) * 7

# Print the final bill amount
print(f"Total Electricity Bill for {units} units = Rs {bill}")
