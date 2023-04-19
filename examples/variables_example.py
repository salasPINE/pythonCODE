#variables
zero = 0
eight = 8
stringvar = 'String Variable'
zerostring = "0"

print(zero)
print(stringvar)

# combining variables - use same type
# won't work
# print(zero + stringvar)
# will work
print(zero + eight)
print(stringvar + zerostring)

# embedding variables in strings
message = "What did the number %s say to the number %s? nice belt!"

print(f"What did the number {zero} say to the number {eight}? nice belt!")

print(message % (zero,eight))