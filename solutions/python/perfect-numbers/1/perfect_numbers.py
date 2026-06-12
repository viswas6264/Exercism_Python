def classify(number):
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    divisors=[]
    for divisor in range(1,number):
        if number%divisor==0:
            divisors.append(divisor)
    aliquot_sum=sum(divisors)
    if aliquot_sum==number:
        return "perfect"
    if aliquot_sum>number:
        return "abundant"
    if aliquot_sum<number:
        return "deficient"
    