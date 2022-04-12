import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

#Output
"""
41
37
b'witch which has which witches wrist watch'
226805979
"""