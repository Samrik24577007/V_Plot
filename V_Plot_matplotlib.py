
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
data=pd.read_table(r"C:/Users/sr19m/.spyder-py3/V_Plot_out.tsv")

Distance=data['Distance']
Length=data['Length']
freq=data['Frequency']
plt.scatter(Distance,Length,c=freq,cmap='Blues')

cbar=plt.colorbar()
cbar.set_label("Frequency of fragment")
plt.xlabel("Fragment Distance (bp)")
plt.xticks(np.arange(-600,700,100),labels=[str(100*i) for i in range(-6,7,1)])
plt.yticks(np.arange(0,600,100),labels=[str(100*i) for i in range(6)])
plt.ylabel("Fragment length (bp)")
plt.title("Heatmap of DNA fragments")
plt.tight_layout()

plt.show()

