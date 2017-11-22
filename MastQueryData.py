import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

import datetime


df = pd.read_csv('MyResult_20171120.csv')

nuv_mag = []
nuv_magerr = []
minPhotoObsDate = []
dtArray = []
dmagArray = []
nameArray = []
tempDate1 = ""
tempDate2 = ""
tempMag1 = 0
tempMag2 = 0
aNum = 0
temp = 0
ekDraMag = []
ekDraTime = []
for name in df.name.unique():
    aNum = aNum + 1
    for k in range (len(df)):
        if (name == df['name'][k] and (df['nuv_mag'][k] > -99)):
            # print(df['name'][k])
            nuv_mag.append(df['nuv_mag'][k])
            nuv_magerr.append(df['nuv_magerr'][k])
            minPhotoObsDate.append(df['minPhotoObsDate'][k])

    x = pd.to_datetime(minPhotoObsDate)
    y = nuv_mag

    #--------------Calculate all the 2 point differences for nuv_mag and time------------#
    if len(y) >= 2:
        for i in range(len(y)):
            tempMag1 = y[i]
            tempDate1 = x[i]
            for p in range(len(y)):
                temp = p + i + 1
                if temp < len(y):
                    tempMag2 = y[temp]
                    tempDate2 = x[p]
                    dtArray.append((np.absolute(tempDate2 - tempDate1).total_seconds()))
                    dmagArray.append(np.absolute(tempMag1 - tempMag2))
                    nameArray.append(name)
                    if (name == 'HD_129333'):
                        ekDraMag.append(np.absolute(tempMag1 - tempMag2))
                        ekDraTime.append((np.absolute(tempDate2 - tempDate1).total_seconds()))



    #-----Testing-----#
    # print(name)
    # print(nuv_mag)
    # print(nuv_magerr)
    # print(minPhotoObsDate)
    #-----------------#

    ###############################################################################
    #--------------------nuv_mag vs time (individual plots)-----------------------#
    # if len(y) >= 2:
    #     plt.figure(figsize=(9,4)) ###
    #     # plt.scatter(x, y)
    #     plt.errorbar(x, y, yerr = nuv_magerr, linestyle = 'none', marker='o')
    #     plt.xlabel('Date')
    #     plt.ylabel('nuv_mag')
    #     plt.title(name)
    #     plt.gca().invert_yaxis()
    #     # plt.show()
    #     plt.savefig(name+'.png', dpi=150, bbox_inches='tight', pad_inches=0.25)
    #     # plt.close() ###
    #     plt.show()

    ###############################################################################

    #---reset arrays---#
    nuv_mag = []
    nuv_magerr = []
    minPhotoObsDate = []
    #------------------#

    # if aNum == 3:
    #     break



####################################################################################
#---------------------------2 point difference graphing ---------------------------#
#-----Testing-----#
# print(dmagArray)
# print(nameArray)
# print(dtArray)
#-----------------#
# x = ekDraMag
# y = ekDraTime

x = dmagArray
y = dtArray

plt.figure(figsize=(9,4)) ###
plt.scatter(x, y)
plt.xlabel(r'$\Delta$' + 'Date')
plt.ylabel(r'$\Delta$' + 'nuv_mag')
plt.title('2 point difference')
plt.show()
plt.savefig('All_2pointdif'+'.png', dpi=150, bbox_inches='tight', pad_inches=0.25)
# plt.close() ###
# plt.show()

####################################################################################
