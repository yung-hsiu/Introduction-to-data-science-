# -*- coding: utf-8 -*-
"""0417week7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ATqn0CmubYpzfuhPbdPyZGMzFDpvCqxe
"""

last_id_disit=input("請輸入身分字號的尾數")
last_id_disit=int(last_id_disit)  #文字換成整數
remainder=last_id_disit%2
#條件判斷(begin)
if remainder ==0:
  ans ="偶數"
else:
  ans="奇數"
#條件判斷(and)
print("身分字號尾數除2的餘數為:{},因此為:{}".format(remainder,ans))

#while迴圈(begin)
i=65
while i <=90:  #bool
  print("character:{},order:{},binary:()".format(chr(i),i,bin(i)))
  i+=1

if True:
  print(123)
print(321)

if False:
  print(123)
print(321)

movie_title=input("輸入電影名稱")
movie_rating=input("輸入電影評等")
movie_rating=float(movie_rating)

if movie_rating>7:
  print("{}的評分為{}分值得去看".format(movie_title,movie_rating))

movie_title=input("輸入電影名稱")
movie_rating=input("輸入電影評等")
movie_rating=float(movie_rating)

if movie_rating>7:
  print("{}的評分為{}分值得去看".format(movie_title,movie_rating))
if movie_rating<=7:    #此行換成else的結果是一樣的
   print("{}的評分為{}分不值得去看，浪費時間".format(movie_title,movie_rating))

#隨堂練習
#(1)月薪超過 4 萬或存款超過 50 萬就發信用卡
#法一

monthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")

monthly_income=int(monthly_income)   #文字轉整數
saving_account=int(saving_account)

if (monthly_income>=40000 or saving_account>=500000):
  print("發信用卡")

#法二

monthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")

monthly_income=int(monthly_income)   #文字轉整數
saving_account=int(saving_account)
ans=""
#條件判斷(begin)
if monthly_income>40000:
  ans="發信用卡"
if saving_account>500000:
  ans="發信用卡"
#條件判斷(end)
print(ans)

#(2)判斷基偶數

user_int = input("請輸入一個正整數：")
user_int=int(user_int)   #文字轉整數

if user_int%2 ==0:
  ans="偶數"
else:
  ans="基數"
print(ans)

#(3)依身分證字號尾數決定星期幾可以購買口罩

id_last_digit = input("請輸入您身分證字號的尾數：")
id_last_digit =int(id_last_digit)

if id_last_digit %2==0:
  ans="星期二四六日領口罩"
else:
  ans="星期一三五日領口罩"
print(ans)

#補充_用身分證字號辨別甚麼時候買口罩
id_number=input("請輸入身分證字號")
id_last_digit=id_number[-1]
id_last_digit=int(id_last_digit)
if id_last_digit %2==0:
  ans="星期二四六日領口罩"
else:
  ans="星期一三五日領口罩"
print(ans)

#(4)判斷 BMI 的類別標籤

input_height = float(input("請輸入身高（公分）："))
input_weight = float(input("請輸入體重（公斤）："))
bmi=input_weight/(input_height*0.01)**2
if bmi>30:
  label="Obese"
elif bmi>25:
  label="Normal weight"
elif bmi<=18.5:
  label="Under weight"
print(label)

