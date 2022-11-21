name=input("名前を教えて下さい")
Hungrylevel=float(input("お腹すいてる度は？"))
age=int(input("年齢は？"))

print(name, "さんはお腹すいてる度", Hungrylevel, "%で年齢は",age, "才ですね。")

if Hungrylevel<=85 and age<=10000:
    print(name,"さん、お腹すきすぎです")
    
else:
    print(name,"さん、いっぱいたべましたね！")