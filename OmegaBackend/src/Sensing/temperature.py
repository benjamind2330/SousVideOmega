from random import randrange

# Q = mcΔT
# Therefore ΔT = Q/mc
# Q = J = Watts * S
# ΔT/s = Watts/mc
# Water has Specific heat (c) of 4.186
WATER_SPECIFIC_HEAT = 4.186
# We will assume a variable size of water.
WATER_AMOUNT_L = 10.0 #L
# we will assume a variable rate of heating.
HEATER_POWER = 1000.0 #Watts


def getTemperatureChange(time_to_calc):
    return time_to_calc * HEATER_POWER/(WATER_SPECIFIC_HEAT * (WATER_AMOUNT_L * 1000))
