str = 'X-DSPAM-Confidence: 0.8475'
ipos=str.find(':')
value=str[ipos+1:]
print(value)
fvalue=float(value)
print(fvalue)
