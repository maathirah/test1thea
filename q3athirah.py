//temperature measurement must times 1.8 and then add with 32//
//random number of temperature chosen was 3 values//

import numpy as np

temper = np.random.rand(3,)
fahrenheit = (temper * 1.8) + 32

print("Degree Celsius = ", temper)
print("Fahrenheit Celsius = ", fahrenheit)
