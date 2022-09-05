while 1:

 year=int(input("请输入一个年份"))
 if year%4==0 and year%100!=0:
    print("该年是闰年")
 else :
    print("该年不是闰年")
