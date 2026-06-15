def get_rounds(number):
    return [number,number+1,number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    middle_card=int(len(hand)/2)
    median=sum(hand)/len(hand)
    return (((hand[0]+hand[-1])/2)==median) or ((hand[middle_card])==median)

def average_even_is_average_odd(hand):
    odd_index=hand[1::2]
    even_index=hand[0::2]
    if len(odd_index)==0 or len(even_index)==0:
        return False
    odd_average=sum(odd_index)/len(odd_index)
    even_average=sum(even_index)/len(even_index)
    return odd_average==even_average
     
def maybe_double_last(hand):
    if 11 not in hand:
        return hand
    if hand[-1]==11:
        hand[-1]=22
    return hand