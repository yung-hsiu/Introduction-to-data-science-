# -*- coding: utf-8 -*-
"""0515week11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CTaz_VSDau5DrtTOX6o2bh3sWth64yDa
"""

#法一
living_area=input("請輸入你所居住的地區:")
living_cost=None
if living_area =="台北市":
  living_cost = 17005
elif living_cost =="新北市":
  living_cost = 15500
elif living_cost =="桃園市":
  living_cost = 15281
elif living_cost =="台中市":
  living_cost = 14596
elif living_cost =="台南市":
  living_cost = 12388
elif living_cost =="高雄市":
  living_cost = 13099
elif living_cost =="非六都縣市":
  living_cost = 12388
elif living_cost =="金門連江縣":
  living_cost = 11684

if living_cost is None:
  print("請重新輸入居住的縣市")
else:
  print("{}的每人每月最低生活費為{:,}".format(living_area,living_cost))

living_cost_dict={
    "台北市":17005,
    "新北市":15500,
    "桃園市":15281,
    "台中市":14596,
    "台南市":12388,
    "高雄市":13099,
    "非六都城市":12388,
    "金門連江縣":11684
}

living_area=input("請輸入居住城市:")
living_cost=living_cost_dict[living_area]
print("{}的每人每月最低生活費為{:,}".format(living_area,living_cost))

#處理keyError，像是輸入"花蓮市"時
living_cost_dict={
    "台北市":17005,
    "新北市":15500,
    "桃園市":15281,
    "台中市":14596,
    "台南市":12388,
    "高雄市":13099,
    "非六都城市":12388,
    "金門連江縣":11684
}
living_area=input("請輸入你居住的縣市:")
try:
  living_cost=living_cost_dict[living_area]
  print("{}的每人每月最低生活費為{:,}".format(living_area,living_cost))
except KeyError:
  print("!!!請重新輸入你的居住城市!!!")

primes_list=[2,3,3,5,5]

print(primes_list)
set(primes_list)  #set的特性刪減掉重複的字

primes={2,3,5,7,11}
odds={2,4,6,8,12}

#原生的資料結構
#交集
# (1)&
primes&odds
# (2).intersection
primes.intersation(odds)
#聯集
# (1)|
# (2).union
#差異
#(1) -
print(primes - odds)
print(odds - primes)
#(2).differnce
#對稱差異
(primes - odds) | (odds - primes)
#(1) ^
#(2) .symmetric_difference