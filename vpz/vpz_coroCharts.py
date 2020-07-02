import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('case_time_series.csv')
Y = data.iloc[61:,1].values 
R = data.iloc[61:,3].values 
D = data.iloc[61:,5].values 
X = data.iloc[61:,0] 
plt.figure(figsize=(25,8))
ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f') 
ax.set_facecolor("black") 
ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
ax.set_ylabel('Number of Confirmed Cases\n',
              size=25,color='#4bb4f2')
plt.xticks(rotation='vertical',size='20',color='white')
plt.yticks(size=20,color='white')
plt.tick_params(size=20,color='white')
for i,j in zip(X,Y):
    ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
ax.annotate('Second Lockdown 15th April',
            xy=(15.2, 860),
            xytext=(19.9,500),
            color='white',
            size='25',
            arrowprops=dict(color='white',
                            linewidth=0.025))
plt.title("COVID-19 IN : Daily Confrimed\n",
          size=50,color='#28a9ff')
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035E9B')

slices = [62, 142, 195]
activities = ['Travel', 'Place Visit', 'Unknown']
cols=['#4C8BE2','#00e061','#fe073a']
exp = [0.2,0.02,0.02]
plt.pie(slices,labels=activities,
        textprops=dict(size=25,color='black'),
        radius=3,
        colors=cols,
        autopct='%2.2f%%',
        explode=exp,
        shadow=True,
        startangle=90)
plt.title('Transmission\n\n\n\n',color='#4fb4f2',size=40)
plt.show()