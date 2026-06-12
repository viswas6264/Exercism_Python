def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted < 500000:
        return True
    return False
        
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power=voltage*current
    efficiency=(generated_power/theoretical_max_power)*100
    if efficiency>=80:
        return "green"
    if efficiency >=60:
        return "orange"
    if efficiency >=30:
        return "red"
    return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    threshold_percent=threshold/100
    if temperature*neutrons_produced_per_second<(90*threshold_percent):
        return "LOW"
    if temperature*neutrons_produced_per_second <= (110*threshold_percent):
        return "NORMAL"
    return "DANGER"