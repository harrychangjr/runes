from runes import *
from math import *

def egyptian_black(pic, n):
    while n >= 3:
        return beside_frac(1/n,stackn(n,black_bb),beside_frac((n-2)/(n-1),stack_frac(1/n,nx1(n-2,black_bb),stack_frac((n-2)/(n-1),pic,nx1(n-2,black_bb))),stackn(n,black_bb)))

def egyptian_white(pic, n):
    while n >= 3:
        return beside_frac(1/n,stackn(n,blank_bb),beside_frac((n-2)/(n-1),stack_frac(1/n,nx1(n-2,blank_bb),stack_frac((n-2)/(n-1),pic,nx1(n-2,blank_bb))),stackn(n,blank_bb)))
    
def beside_frac(frac, pic1, pic2):
    return quarter_turn_left(stack_frac(frac,quarter_turn_right(pic1),quarter_turn_right(pic2)))



def nxn(n,pic):
    return stackn(n,quarter_turn_right(stackn(n,quarter_turn_left(pic))))

def nx1(n,pic):
    return stackn(1,quarter_turn_right(stackn(n,quarter_turn_left(pic))))


base1 = egyptian_black(scale(1/2,black_bb),6)

base2 = egyptian_white(egyptian_black(blank_bb,4),6)

finalbase = stack(beside(base1,base2),beside(base2,base1))

#tile art display
anaglyph(scale(2.25,rotate(math.pi/4,(nxn(8,finalbase)))))
