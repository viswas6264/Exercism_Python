EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    '''The actual time required for our lasagna to bake is 40 Minutes when we look at the clock after a few minutes say., 30 Minutes; Then this function starts its operation by returning the remaining time to bake it (40-30=10 Minutes)'''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
print(bake_time_remaining.__doc__)
print(bake_time_remaining(30))

def preparation_time_in_minutes(layers):
    '''Suppose there were 3 layers and each layer takes 2 Minutes to bake then we just multiply to find the time taken by all the layers (3*2=6 Minutes)'''
    return layers*PREPARATION_TIME
print(preparation_time_in_minutes.__doc__)
print(preparation_time_in_minutes(3))

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    '''Here we can know the time taken by the layers and baking time; Here we are just calling our defined function rather than just writing the same code again (6+10= 16 Minutes)'''
    return preparation_time_in_minutes(layers)+elapsed_bake_time
print(elapsed_time_in_minutes.__doc__)
print(elapsed_time_in_minutes(3, 10))