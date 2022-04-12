from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()

#Output
"""
0.57535828626024577
0.54962537085770791
"""