def upper(a):
    if a in a.upper():
        return print('최소한 하나의 알파벳 소문자가 포함되어야 합니다.')
    else:
        return print(a.upper())

i=0      
while i<100:
    upper(input("\n알파벳 소문자를 입력해보세요 : "))
    print('프로그램을 종료하려면 exit를 입력하세요. \n계속하려면 엔터를 치세요.')
    if input() == "exit":
        break
    
       

  


