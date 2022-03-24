s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it)

#output
"""
<str_iterator object at 0x10c90e650>
'a'
'b'
'c'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
"""