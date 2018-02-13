import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
from astropy.time import Time

df = pd.read_csv('MyResult_20171120.csv')
df2 = pd.read_table('table7.dat.txt', delim_whitespace=True, usecols=(0,1,2,3,4),names = ['Epoch','JD0','JD1','N','Vmag'])

nuv_mag = []
v_mag = []
avgPhotoObsDate_Bal = []
avgPhotoObsDate_MG = []


for k in range (len(df)):
    if ('HD_129333' == df['name'][k] and (df['nuv_mag'][k] > -99) and (df['tilenum'][k] != 50098)):
        nuv_mag.append(df['nuv_mag'][k])
        t = Time(((pd.to_datetime(df['minPhotoObsDate'][k]).to_julian_date() +
                   pd.to_datetime(df['maxPhotoObsDate'][k]).to_julian_date())/2),format = 'jd', scale ='utc')
        avgPhotoObsDate_Bal.append(t.jyear)


for k in range(len(df2)):
    t = Time(((df2['JD0'][k] + df2['JD1'][k])/2),format='jd',scale='utc')
    avgPhotoObsDate_MG.append(t.jyear)
    v_mag.append(df2['Vmag'][k])


nuv_mag = np.array(nuv_mag, dtype='float')
v_mag = np.array(v_mag, dtype='float')
avgPhotoObsDate_Bal = np.array(avgPhotoObsDate_Bal)
avgPhotoObsDate_MG = np.array(avgPhotoObsDate_MG)


# print(avgPhotoObsDate_MG)
# print(avgPhotoObsDate_Bal)


plt.figure(figsize=(9,4))
plt.scatter(avgPhotoObsDate_MG, v_mag - np.median(v_mag), label = 'VMag')
plt.scatter(avgPhotoObsDate_Bal, nuv_mag - np.median(nuv_mag), label = 'NUV_Mag')
plt.xlabel('Date [jyear]')
plt.ylabel(r'$\Delta$' + 'Mag')
plt.title('HD_129333')
plt.gca().invert_yaxis()
plt.legend(bbox_to_anchor=(.7, .95), loc=2, borderaxespad=0.)
plt.show()
plt.savefig('Composite_plot.png', dpi=150, bbox_inches='tight', pad_inches=0.25)
plt.close()
plt.show()
