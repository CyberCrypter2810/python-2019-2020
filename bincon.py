# bincon.py gbpm
# Convert a base 10 number to binary
# Use 191 base 10 equal to 1011 1111 base 2
# q(quotient) d(divisor) r(remainder) n(integer input)

# divide by 128
n = int(input("Input an integer less than 256 : "))
d = 128
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remander by 64
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remander by 32
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remander by 16
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remander by 8
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remander by 4
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remainder by 2
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)

# divide remainder by 1
n = r
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
