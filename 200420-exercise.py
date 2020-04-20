print('나가고 싶다면 exit를 입력하세요. \n궁금하면 엔터를 두 번 쳐보세요.')

star=0
while True:
    if input() == 'exit':
        break
    if input() == '':
        star=star+1
        print('*'*star)
        print('더 궁금하면 엔터를 두 번 쳐보세요. 싫다면 exit를 입력하세요.')





    


