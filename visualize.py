# Short script to plot tones for troubleshooting.

import numpy as np
import matplotlib.pyplot as plt
from music import *

x = np.arange(0,800)
tone = generateTone('a')[0:800]

plt.plot(x,tone)
plt.show()
