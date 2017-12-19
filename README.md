# bognar-buvos-golyok
solver for the puzzle bognar-buvos-golyok (instant insanity)

There was a time, before I became a mathematician, when I was fascinated by puzzles and could spend inordinate amounts of time trying to figure them out.
I still enjoy playing with a good puzzle and attempting to organize it in my head, but time is a precious commodity and I can't lose myself in this activity the way I used to.

Anyway, I was visiting acquaintances who had a good collection of puzzles and encountered Bognar Buvos Golyok for the first time.
After a while, I decided to turn it into a TDD exercise.
It worked pretty well, although I did not manage to stick to TDD exclusively.

### How to use it

Here is a sample ipython session:

```
In [1]: from cube import Cube, CubeTower
In [2]: c0 = Cube([['Y', 'Y'], ['B', 'G'], ['R', 'G']])
In [3]: c1 = Cube([['G', 'B'], ['Y', 'B'], ['Y', 'R']])
In [4]: c2 = Cube([['R', 'R'], ['R', 'Y'], ['G', 'B']])
In [5]: c3 = Cube([['B', 'R'], ['G', 'R'], ['B', 'Y']])
In [6]: tower = CubeTower([c0, c1, c2, c3])
In [7]: tower
Out[7]:
 Y     G     R     B
BRGG  YYBR  RGYB  GBRY
 Y     B     R     R

In [9]: for s in tower.solutions():
    ...:     print(s)
    ...:     print()
    ...:        
 Y     B     R     R
BGGR  YRBY  RBYG  GYRB
 Y     G     R     B

 Y     G     R     B
BRGG  YYBR  RGYB  GBRY
 Y     B     R     R

 Y     G     R     B
GGBR  BRYY  YBRG  RYGB
 Y     B     R     R

 Y     B     R     R
GRBG  BYYR  YGRB  RBGY
 Y     G     R     B

 Y     G     R     B
GBRG  RYYB  BRGY  YGBR
 Y     B     R     R

 Y     B     R     R
GGRB  RBYY  BYGR  YRBG
 Y     G     R     B

 Y     B     R     R
RBGG  YYRB  GRBY  BGYR
 Y     G     R     B

 Y     G     R     B
RGGB  YBRY  GYBR  BRYG
 Y     B     R     R
```
