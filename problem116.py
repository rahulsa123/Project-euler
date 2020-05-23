limit = 50
import functools
total = 0
for red in range(1, limit//2+1):
    up = functools.reduce(lambda x,y:x*y,[limit-2*red+x for x in range(1,red+1)])
    down = functools.reduce(lambda x,y:x*y,[x for x in range(1, red+1)])
    total += up/down

for green in range(1,limit//3+1):
    up = functools.reduce(lambda x,y:x*y,[limit-3*green+x for x in range(1,green+1)])
    down = functools.reduce(lambda x,y:x*y,[x for x in range(1, green+1)])
    total += up/down

for blue in range(1, limit//4+1):
    up = functools.reduce(lambda x,y:x*y,[limit-4*blue+x for x in range(1,blue+1)])
    down = functools.reduce(lambda x,y:x*y,[x for x in range(1, blue+1)])
    total += up/down
print(total)