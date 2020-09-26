from runes import *


def beside_frac(frac, pic1, pic2):
    return quarter_turn_left(stack_frac(frac,quarter_turn_right(pic1),quarter_turn_right(pic2)))


#10 segments of picture
row1 = stack_frac(10/27,stack_frac(9/10,blank_bb,black_bb),blank_bb)
row2 = stack_frac(20/27,stack_frac(15/20,stack_frac(11/15,stack_frac(10/11,blank_bb,black_bb),blank_bb),black_bb),blank_bb)
row3 = stack_frac(15/27,stack_frac(11/15,blank_bb,black_bb),blank_bb)
row4 = stack_frac(10/27,stack_frac(8/10,stack_frac(4/8,blank_bb,black_bb),blank_bb),black_bb)
row5 = stack_frac(20/27,stack_frac(3/20,blank_bb,black_bb),blank_bb)
row6 = stack_frac(20/27,stack_frac(8/20,stack_frac(5/8,stack_frac(3/5,blank_bb,black_bb),blank_bb),black_bb),blank_bb)
row7 = stack_frac(8/27,stack_frac(7/8,stack_frac(6/7,stack_frac(5/6,stack_frac(3/5,blank_bb,black_bb),blank_bb),black_bb),blank_bb),black_bb)
row8 = stack_frac(15/27,stack_frac(12/15,stack_frac(10/12,stack_frac(8/10,stack_frac(5/8,stack_frac(3/5,blank_bb,black_bb),blank_bb),black_bb),blank_bb),black_bb),blank_bb)
row9 = stack_frac(19/27,stack_frac(15/19,stack_frac(10/15,stack_frac(8/10,stack_frac(7/8,stack_frac(6/7,stack_frac(5/6,stack_frac(4/5,blank_bb,black_bb),blank_bb),black_bb),blank_bb),black_bb),blank_bb),black_bb),blank_bb)
row10 = stack_frac(9/27,stack_frac(7/9,stack_frac(5/7,stack_frac(4/5,blank_bb,black_bb),blank_bb),black_bb),blank_bb)


ninja = beside_frac(9/10,beside_frac(8/9,beside_frac(7/8,beside_frac(6/7,beside_frac(5/6,beside_frac(4/5,beside_frac(3/4,beside_frac(2/3,beside_frac(1/2,row1,row2),row3),row4),row5),row6),row7),row8),row9),row10)

#show pixel ninja
#stack frac with black_bb for black flooring
show(stack_frac(25/26,scale_independent(0.55,1.3,ninja),black_bb))
