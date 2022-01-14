import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("final_data.csv")
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        


G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)
        


df["Gravity"] = gravity
df


df2 = pd.read_csv("star_with_gravity.csv")

planet_radiuses = [ ]
planet_masses = [ ]
planet_gravity = [ ]


planet_radiuses.append(radius)
planet_masses.append(mass)
planet_gravity.append(gravity)


planet_radiuses.sort()
planet_masses.sort()
planet_gravity.sort()

#Plotting Figure 1
plt.figure(figsize=(10,5))
sns.lineplot(planet_masses,planet_radiuses,marker='o',color='red') #planet mass  on x axis, radius is y axis, marker is the dot, and color is red
plt.title('Mass and Radius')
plt.xlabel('Mass') #x axis is number of clusters
plt.ylabel('Radius')
plt.show()


#Plotting Figure 2
plt.figure(figsize=(10,5))
sns.lineplot(planet_masses,planet_gravity,marker='o',color='red') #planet mass  on x axis, gravity is y axis, marker is the dot, and color is red
plt.title('Mass and Gravity')
plt.xlabel('Mass') #x axis is number of clusters
plt.ylabel('Gravity')
plt.show()



