t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
t.safe_substitute(d)

#Output
"""
Traceback (most recent call last):
  ...
KeyError: 'owner'

'Return the unladen swallow to $owner.'
"""