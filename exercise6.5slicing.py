str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
print(colon)
print(str[18])

# the colon is found at index 18 so want everything upwards

digits = str[18+1:]
digits = float(digits)
print(digits)
print(type(digits))
