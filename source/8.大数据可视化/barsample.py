#encoding=utf-8
'''
Created on 2019年8月16日

@author: zhangxiao
'''

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

province=['广东','山东','河南','四川','江苏','河北','湖南','安徽','湖北','浙江','广西','云南','江西','辽宁','福建','陕西','黑龙江','山西','贵州','重庆','吉林','甘肃','内蒙古','新疆','上海','台湾','北京','天津','海南','香港','宁夏','青海','西藏','澳门']
population=[11346,10047.24,9605,8341,8029.3,7556.3,6860.2,6323.6,5917,5737,4885,4800.5,4622.1,4359.3,3941,3835.44,3788.7,3702.35,3580,3048.43,2717.43,2625.71,2534,2444.67,2423.78,2369,2170.7,1559.6,925.76,748.25,681.79,598.38,337.15,63.2]

#orientation指方向，水平条形图的纵坐标应该是bottom=x5,横坐标是width=y5.
#plt.bar(0,bottom=range(len(province)),width=population,height=0.7,orientation='horizontal') 
plt.barh(range(len(province)),population,height=0.7)
plt.yticks(range(len(province)),province)
plt.tick_params(labelsize=8)
plt.xlabel("人口(万人)") 



plt.show()

