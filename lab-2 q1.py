# Original string
S1 = "Maha Bharat"

# 1. Generate "mAHA bHARAT"
string1 = S1.lower().capitalize() + ' ' + S1[5:].upper()
print(string1)

# 2. Generate "Bharat"
string2 = S1[5:]
print(string2)

# 3. Generate "BharatBharatBharat"
string3 = S1[5:] * 3
print(string3)

# 4. Generate "Mera Bharat"
string4 = "Mera" + S1[4:]
print(string4)

# 5. Generate "Mera Bharat Mahan"
string5 = "Mera Bharat Mahan"
print(string5)
