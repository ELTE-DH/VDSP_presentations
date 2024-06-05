from matplotlib import pyplot as plt
import pandas as pd

"""
Dataset head:
,Year,Month,Day,Date In Fraction Of Year,Number of Sunspots,Standard Deviation,Observations,Indicator
0,1818,1,1,1818.001,-1,-1.0,0,1
1,1818,1,2,1818.004,-1,-1.0,0,1
2,1818,1,3,1818.007,-1,-1.0,0,1
"""


# Load the CSV file
data = pd.read_csv('./sunspot_data.csv')

df_many_obs = data[data['Observations'] > 5]

# Rows with std < 20% of spot number
df_std = data[data['Standard Deviation'] < 0.2 * data['Number of Sunspots']]

# avg by year

df_avg = df_std.groupby('Year').mean()

plt.plot(df_avg.index, df_avg['Number of Sunspots'])

# Save

plt.savefig('./sunspot_avg.png')

# 
