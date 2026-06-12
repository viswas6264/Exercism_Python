def line_up(name, number):
    suffix="th"
    if number%10==1:
        suffix="st"
    if number%10==2:
        suffix="nd"
    if number%10==3:
        suffix="rd"
    if number%100 in (11,12,13):
        suffix="th"
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!" 