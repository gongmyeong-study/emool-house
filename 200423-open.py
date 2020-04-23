f = open('C:/users/palpi/desktop/hello.txt', 'w')
for i in range(1, 24):
    data = '%d시 입니다.\n' % i
    f.write(data)
f.write('잠을 잡니다.')

f.close()