class Student:
    sleep = 'all day long'
    study = 'a little bit'

    def rebirth(self):
        self.study = 'never'
        return self.study

a = input('What\'s your name? : ')
print(a + ', hi there.\n')

x = input('Are u Student? Please say yes or no : ')
if x == 'yes':
    a = Student()
    print('\nyour sleeping hours : ' + a.sleep, '\nyour study hours : ' + a.study)
    if input('\nDo you wanna rebirth? Please say yes. : ') == 'yes':
        print('\nyour sleeping hours : ' + a.sleep, '\nyour study hours : ' + a.rebirth())
        print('good luck.\n')

else:
    print('ok, bye.\n')




