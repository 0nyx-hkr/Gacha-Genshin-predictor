import random
import numpy
import matplotlib.pyplot as plt
############       GACHA - MODEL WITH RANDOM   #################
set = {
    '5-star' : 0.7,
    '4-star': 6,
    '3-star': 93.3
}
def summons():
    rotating_prob = 1
    five_pity = 0
    four_pity = 0
    max_pity = 90
    wishes=[]
    population = list(key for key in set.keys())
    while five_pity < max_pity:
        four_pity = four_pity+1
        five_pity = five_pity +1
        prob_4 = rotating_prob*set['4-star']
        prob_5 = rotating_prob*set['5-star']
        prob_3 = rotating_prob*set['3-star']
        if four_pity<10:
            i = random.choices(population=population,weights=[prob_5,prob_4,prob_3])
            print(i)
            if i[0] == '4-star': four_pity = 0 
        else:
            i = ['4-star']
            four_pity=0
        rotating_prob = rotating_prob*(set[i[0]])
        wishes.append(i[0]) 
        if i[0]== '5-star':
            break
        else:
            continue 
    if '5-star' not in wishes:
        wishes.pop(-1)
        wishes.append('5-star')
    return wishes
##########     GACHA - MODEL WITH NUMPY RANDOM     ############
def recruits():
    rotating_prob = 1
    five_pity = 0
    four_pity = 0
    max_pity = 90 
    wishes=[]
    population = list(key for key in set.keys())
    while five_pity < max_pity:
        four_pity = four_pity+1
        five_pity = five_pity +1
        prob_4 = rotating_prob*set['4-star']
        prob_5 = rotating_prob*set['5-star']
        prob_3 = rotating_prob*set['3-star']
        prob = prob_3+prob_4+prob_5
        if four_pity<10:
            i = numpy.random.choice(a=population,size=1,p=[prob_5/prob,prob_4/prob,prob_3/prob])
            if i[0] == '4-star': four_pity = 0 
        else:
            i = ['4-star']
            four_pity=0
        rotating_prob = rotating_prob*(set[i[0]])
        wishes.append(i[0]) 
        if i[0]== '5-star':
            break
        else:
            continue
    if '5-star' not in wishes:
        wishes.pop(-1)
        wishes.append('5-star')
    return wishes
rolls = recruits()
print(rolls)