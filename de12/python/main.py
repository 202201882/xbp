from re import A
from unicodedata import name


name="こんにちわ"
#\^-^/
waist=70
age=10000
Hungrylevel=100
power=10

print(name,"さんは腹囲",waist,"cmで年齢は",age,"才ですyo",Hungrylevel,"%お腹すいてる度",power,"%自分のlevel",)

if waist>=85:
    print(name,"さん、内臓脂肪注意")
else:
    print(name,"さん、腹囲に問題はないです")
name=input("you name?")
waist a=input("you waist?")
age=input("you age?")
