# PNG, JPEG, MP3, WAV, ASCII, UTF-8 etc are different forms of encodings.
#  An encoding is a format to represent audio, images, text, etc in bytes


# Converting Strings to byte objects is termed as encoding
# This is necessary so that the text can be stored on disk using mapping using ASCII or UTF-8 encoding techniques

# string object
strobj = 'Geeksforgeeks'
byteobj = b'Geeksforgeeks'
print(strobj, byteobj, sep="--")


# using encode() to encode the String
# encoded version of a is stored in d
c = strobj.encode()
print(c)

# encoding using ASCII mapping
d = strobj.encode('ASCII')
print(d)

#decoding
cdecode = c.decode()
print(cdecode)
ddecode = d.decode('ASCII')
print(ddecode)



