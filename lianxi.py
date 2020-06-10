# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[-2])
# print(players[1:4])
# print(players[:4])
# print(players[1:])
# print(players[-3:])
# 遍历列表
# print('here first in play')
# for i in players[:3]:
#     print(i.title())
#
#
# my_food=['pizz','fal','carr']
# p_food=my_food[:]
#
# my_food.append('ice')
# p_food.append('cake')
#
# print(my_food,p_food)


# my_li = ['set', 'up', 'down', 'pp']
# for i in my_li[0:3]:
#     print(i + ' \twelcome')
#
# for i in my_li[1:4]:
#     print(i + ' \twelcome')
#
# for i in my_li[-3:]:
#     print(i + ' \twelcome')
# for i in my_li[:]:
#     print(i + ' \twelcome')
# for i in my_li[::]:
# print(i + ' \t\nwelcome')


# my_pz=['q','w','e']
# f_pz=my_pz[:]
#
#
# f_pz.append('a')
# my_pz.append('b')
# print(my_pz,f_pz)

# for mp in my_pz:
#     print(mp+' \t is my pz')
# for fp in f_pz:
#     print(fp+' \tis fr pz')
# 元组
# yuanzu=(200,50,100,30)
# print(yuanzu[0])
# print(yuanzu[1])
# # yuanzu[0]=210
# for i in yuanzu:
#     print(i)
# yuanzu=(1,2)
# for c in yuanzu:
#     print(c)

# cai=('cc','bb','dd','ee','rr')
# for ca in cai :
#     print(ca)
#
#
# # cai[0]=2
#
# cai=('cc','bb','dd','nn','mm')
# for c in cai:
#     print(c)
# cars = ['audi', 'bmw', 'suba', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# car='audi'
# print(car == 'bmw')
# car ='Audi'
# print(car.lower()=='audi')
# resques='cc'
# if resques!='cc':
#     print('dhajh')
# else:
#     print('dee')
# age=18
# print(age==18)
# ace=17
# if ace>=12:
#     print('no')
# else:
#     print('yes')
# age1=22
# age2=1
# if age1>23 or age2>1:
#     print('yes')
# else:
#     print('no')
# li12=['a','c','d']
# print('d' not in li12)
# game_active=True
# can_edit=False
# food='ear'
# print(food=='ear')
# print(food=='rae')
#
# a='aa'
# b='aa'
# c='bb'
# print(a==b)
# print(b==c)
# a='AA'
# b='aa'
# c='cc'
# print(a==b)
# print(a.lower()==b)
# print(c==b)
# num_1=1
# num_2=10
# print(num_1==num_2)
# print(num_1>=num_2)
# print(num_1<=num_2)
# print(num_1>num_2)
# print(num_1<num_2)
# print(num_1>1  and num_2 <100)
# print(num_1==1 and num_2 >100)
# print(num_1==1 and num_2==10)
# print(num_1==1 or num_2>100)
# print(num_1==10 or num_2>100)
# li2=['11','22','33']
# print('11'  not i

# age = input('please you age ')
# age=18
# if age < 4:
#     price = 0
# elif age <= 18:
#     price = 5
# elif age <= 65:
#     price = 10
# else:
#     price = 5
# print('you price= ' + str(price) + '.')
#
#
# li2=['cc','bb','dd']
# if 'cc' in li2:
#     print('cc')
# if 'bb' in li2:
#     print('bb')
# if 'ee' in li2:
#     print('aa')
# alien_color='yello'
# if alien_color=='green':
#     print('you have 5')
# alien_color = 'green'
# if alien_color == 'green':
#     print('you have 5')
# age = 100
# if age < 2:
#     print('kidd')
# elif 2 <= age <= 4:
#     print('kids')
# elif 4 < age <= 13:
#     print('kid')
# elif 13 < age <= 20:
#     print('young')
# elif 20 < age <= 65:
#     print('peo')
# elif age > 65:
#     print('old')
# cequea=['musgrooms','green peppers','rxita']
# for cc in cequea:
#     if cc=='green peppers':
#             print('add1\t'+cc+'.')
#     else:
#         print('add'+cc+'.')
# print('\nfinishing')

# ceshi=[]
# if ceshi:
#     for cc in ceshi:
#         print('add'+cc+'.')
#     print('djdjskj')
# else:
#     print('if you want ,i can')
# ceshi_1=['zicai','baicai','baocai','qingjiao','lvdou','baicha']
# ceshi_2=['baicai','hongcha','baitang']
#
# for cc in ceshi_1:
#     if cc in ceshi_2:
#         print('2个都包含了'+cc)
#     else:
#         print('抱歉我不知道'+cc)
# wang='whjdhkj'
# for c in wang:
#     print(c)
# un=['xia','zhi','feng','de','ceshi','admin']
# for user1 in un:
#     if un:
#         if user1=='admin':
#             print(user1+' would you like tosee a status report?')
#         else:
#             print(user1+'hello thank you for logging in again')
#     else:
#         print('we need to find some users')
# current_users=['xia','zhi','feng','de','dian','nao']
# new_user=['xia','zhi','ce','shi','cc']
# for xin in new_user:
#     if xin in current_users or xin.lower() in current_users or xin.upper() in current_users:
#         print(xin+'该用户名已经被使用')
#     else:
#         print('该用户名可以使用')
# alien_0={'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points=alien_0['points']
# print('you just aerend '+str(new_points)+' points!')
# print(alien_0)
# alien_0['x_postion']=0
# alien_0['y_postion']=25
# print(alien_0)
# alien_0={}
# alien_0['color']='green'
# alien_0['points']=5
# print(alien_0)
#
# alien_0['color']='yellow'
# print(alien_0)
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print('origin x-position' + str(alien_0['x_position']))
# # 向右移动
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print('new x-position: ' + str(alien_0['x_position']))
# alien_0={'color':'green','points':5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# fav_language={
#     'jen':'python',
#     'sarqah':'c',
#     'ed':'ruby',
#     'phil':'python'
# }
# # print('sarah is like language is '+fav_language['sarqah'].title())
# my_xinxi={'first_name':'xia','last_name':'zhifeng','age':25,'city':'hefei'}
# print(my_xinxi)
# zidian={'city':'城市','age':'岁数','speed':'速度','fat':'胖'}
# print(zidian['city']+'是city含义\n')
# print(zidian['age']+'是age含义\n')
# print(zidian['speed']+'是speed含义\n')
# print(zidian['fat']+'s是fat含义\n')
# user_0={'username':'efermi',
#         'first':'enrico',
#         'last':'fermi'}
#
# for key,value in user_0.items():
#     print('\nkey '+key)
#     print('value '+value)


# for name,language in fav_language.items():
#     print(name.title()+'for languages langusges is '+language.title())
# if 'erin' not in fav_language.keys():
#     print('erin.pleae')

# for name in fav_language.keys():
#     print(name.title())
#
# friends=['phil','sarah']
# for name in fav_language.keys():
#     print(name.title())
#     if name in friends:
#         print('hi'+name.title()+
#               ' i see you fav lag is '+
#               fav_language[name].title())

# fav_language={
#     'jen':'python',
#     'sarah':'c',
#     'ed':'ruby',
#     'phil':'python'
# }
# for name in sorted(fav_language.keys()):
#     print(name.title()+'  tjhank you for taling the poll')
# for language in fav_language.values():
#     print(language.title())

# for language in set(fav_language.values()):
#     print(language.title())

# py_shuyu={'list':'列表','key':'键','value':'值','tup':'元组','set':'设置',}
# for key,value in py_shuyu.items():
#     print('输出 key '+key+' value ' + value)
# print('value ' + value)
# alien_0={'color':'green','points':5}
# alien_1={'color':'yellow','points':10}
# alien_2={'color':'red','points':15}
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
# #     print(alien)
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # for alien in aliens[:5]:
# #     print(alien)
# # print('...')
# # print('总共'+str(len(aliens)))
#
# for alien in aliens[0:3]:
#     if alien['color']=='green':
#         alien['color']='yellow'
#         alien['speed']='medium'
#         alien['points']=10
#     elif alien['color']=='yellow':
#         alien['color']='red'
#         alien['speed']='fast'
#         alien['points']=15
#
#
#         # 显示前5个外星人
# for alien in aliens[0:5]:
#     print(alien)
# print(...)
# pizza={'crust':'thick',
#        'toppings':['mushrooms','extra cheers'],}
# print('you orders a '+pizza['crust']+'-crust pizza'+
#       'with the')
# for topping in pizza['toppings']:
#     print('\t'+topping)

# fav_languages={
#     'jen':['python','ruby'],
#     'sarah':['c'],
#     'edward':['ruby','go'],
#     'phil':['python','haskell'],
# }
# for name,languages in fav_languages.items():
#     print('\n'+name.title()+'favorite languages are')
#     for language in languages:
#         print('\t'+language.title())
# users = {
#     'aeunstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         }
#     }
# }
# for username,user_info in users.items():
#     print('\n username: '+username)
#     full_name=user_info['first']+user_info['last']
#     location=user_info['location']
#
#     print('\t full name: '+ full_name.title())
#     print('\t location : '+location)
# kailun={
#     'first':'xia',
#     'last':'zhi',
#     'city':'hefei',
# }
# juses={
#     'first': 'jioshu',
#     'last': 'juses',
#     'city': 'paris',
# }
# liu={
#     'first': 'liu',
#     'last': 'yong',
#     'city': 'anhui',
# }
# people=[liu,juses,kailun]
#
# for cc in people:
#     print(cc)
#     print(people)
# case=input('please input name')
# print(case)
# name=input('please enter your name: ')
# print('hello ,'+name+'!')
# prompt='if you tell us who you are ,we can personalize the message you see'
# prompt+='\nwhat is you first name'
# name=input(prompt)
# print('\nhello ,'+name+'!')
# age = input('how old are you?')
# age = int(age)
# print(age >= 18)
# print(age)
# heigh=input('please input your heigh:')
# heigh=int(heigh)
# if heigh>=36:
#     print('\nyou are tall enough to ride')
# else:
#     print("\nyou'll be able to ride when you are a little older.")
# numebr=input('inpurt number: ')
# numebr=int(numebr)
# if numebr%2==0:
#     print('oushu')
# else:
#     print('jishu')
# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1
# prompt='\ntell me something , and i will repeat it back to you '
# prompt+='\nenter "quit" to end the program'
# message =''
# # while message!='quit':
# #     message=input(prompt)
# #     if message!='quit':
# #         print(message)
# active=True
# while active:
#     message=input(prompt)
#
#     if message=='quit':
#         active=False
#     else:
#         print(message)
# prompt = '\nplease enter the aname of a city you have visited'
# prompt += "\n(enter 'quit' when you are finished)"
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print('l d love to go to' + city.title() + '!')
# current_mumber = 0
# while current_mumber < 10:
#     current_mumber += 1
#     if current_mumber % 2 == 0:
#         continue
#
#     print(current_mumber)
# cc=('请输入配料')
# cc+=("当输入'quit'时退出")
# while True:
#     peiliao=input(cc)
#
#     if peiliao=='quit':
#         break
#     else:
#         print('我们会添加'+cc.title())
# tihi = ('请输入岁数')
# active=True
# while active:
#     age = input(tihi)
#     age=int(age)
#     if age < 3:
#         continue
#         print('0')
#     elif 3 <= age < 12:
#         print('10')
#         active=False
#     else:
#         print('15')
# un_usernames=['alice','brian','candace']
# info_usernames=[]
# while un_usernames:
#     current_user=un_usernames.pop()
#
#     print('verifying usder :'+current_user.title())
#     info_usernames.append(current_user)
#
#     print('\nthe following users have been confrined')
#     for info_username in info_usernames:
#         print(info_username.title())
# pets =['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# # 设置标志，标志不变循环继续
# poll_active = True
# while poll_active:
#     name = input('\nwhat is you name')
#     response = input('what are you doing?')
#     responses[name] = response
#
#     repeat = input('would you like to let another person response?(yes/no)')
#     if repeat == 'no':
#         poll_active = False
# print('\n----------poll results-----------')
# for name, response in responses.items():
#     print(name + 'would like to climb ' + response)

# jieguo={}
# poll_jieguo=True
# while poll_jieguo:
#     name=input('请输入name')
#     mudidi=input('请输入目的地')
#     jieguo[name]=mudidi
#
#     ceshi=input('you yuanyi zou me ? yes/no')
#     if ceshi == 'no':
#         poll_jieguo=False
# print('-----------------------')
# for name,mudidi in jieguo.items():
#     print(name+'iiii'+mudidi)
# san_orders=['jidan','jirou','yu']
# # unord=[]
# # while san_orders:
# #     cc=san_orders.pop()
# #     print('jiancha'+cc.title())
# #     unord.append(cc)
# #     print('gaoding')
# #     for un in unord:
# #         print(un.title())
#
# niurou=['pastami','jirou','niurou','zhurou','pastami','pastami']
# print(niurou)
# while 'pastami' in niurou:
#     niurou.remove('pastami')
#
# print(niurou)
# def greet_user(username):
#     print('hello '+username.title()+'!')
# greet_user('jj')
# def book(cc):
#     print('please '+cc
# book('ceshi')
# def decire_pet(pet_name, animal_type=' dog '):
#     print('\ni have a ' + animal_type + '.')
#     print('my' + animal_type + 'name is ' + pet_name.title())
#
#
# decire_pet('xia')
# decire_pet(pet_name='zing')
# decire_pet('cc','dd')
# decire_pet(animal_type='cat',pet_name='aaa')
# def make_shirt(size, ziyang='i love python'):
#     print('size  is ' + size + ' ziyang   wei ' + ziyang)
#
#
# make_shirt('xL')
# make_shirt(size='m')
# make_shirt('s','ziyang')
# def get_formatted_name(first_name, last_name,middle_name=''):
#     if middle_name:
#         full_name=first_name+' '+middle_name+' '+last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# name_1 = get_formatted_name('xia', 'zhifeng','cc')
# name_2=get_formatted_name('xia','zhifeng')
# print(name_1,name_2)
# def build_person(first_name, last_name,age=''):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age']=age
#
#     return person
#
#
# musio = build_person(first_name='jj', last_name='xai',age='cc')
# print(musio)

# def get_formatted_name(first_name, last_name):
# #     full_name = first_name + ' ' + last_name
# #     return  full_name.title()
# # while True:
# #     print('\ntell me you name')
# #     print('\n 按 q 退出')
# #     f_name=input('first_name ')
# #     if f_name=='q':
# #         break
# #
# #     l_name=input('last_name ')
# #     if l_name=='q':
# #         break
# #     formatted_name=get_formatted_name(f_name,l_name)
# #     print('\nhello '+formatted_name)
# def city_country(city,country):
#     jiji=city+' ,'+country
#     return jiji
#     print(jiji)
#
# ceshi=city_country(city='11',country='222')
# print(ceshi)

# def make_album(zhuanji, geshou, gequshu=''):
#     if gequshu:
#         zjj=zhuanji+gequshu+geshou
#     else:
#         zjj=zhuanji+geshou
#     return zjj
#
# while True:
#     print('qingshuru1name')
#
#     zj = input('zhuaanji')
#     if zj == 'q':
#         break
#     gs = input('geshou')
#     if gs == 'q':
#         break
#     gq=input('gequ')
#     if gq=='q':
#         break
#     zjj=make_album(zj, gs, gq)
#     print('hello'+zjj)

# cc = make_album('稻花', 'zhou')
# dd = make_album('稻花', 'wang', '10
# chuangjian = ['iphones case', 'robot pendant', 'dodecahearon']
# modes = []
#
# while chuangjian:
#     curr_des = chuangjian.pop()
#
#     print('printing model: ' + curr_des)
#     modes.append(curr_des)
#
# print('\nthe following modes have been printed:')
# for mode in modes:
#     print(mode)
# def print_models(unprintes_designs, completed_models):
#     while unprintes_designs:
#         current_design = unprintes_designs.pop()
#
#         print('printing model: ' + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print('\nthe following models have been printed')
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphones case', 'robot pendant', 'dodecahearon']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# function_name(list_name[:])

# def show_magicians(list_name):
#     for liat_va in list_name:
#         print(liat_va)
# def make_great(list_c,ee):
#     while list_c:
#         list_1=list_c.pop()
#         print('the great ：'+list_1)
#         ee.append(list_c)
#
#
#
# aa=['11','22','333']
# dd=[]
# make_great(aa[:],dd)
# def make_pizza(size, *toppings):
#     print('\nmaking a ' + str(size) +
#           ' pizz ')
#     for toped in toppings:
#         print(toped + ' cv')
#
#
# make_pizza(12, 'pepperoni')
# make_pizza(16, 'mushrooms', 'green peppers', 'extra chees')


# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile=build_profile('xia','zhifeng',
#                                  add='hefei',home='shushan',love='dog')
# print(user_profile)

# user_profile = build_profile('albert', 'einstein', location='princetion', field='physics')
# print(user_profile)
# def sanweiji(name, *tianjia):
#     print(name)
#     for tian in tianjia:
#         print(tian + ' jiashang ')
# cc = sanweiji('jirou', 'cc', 'd')
# dd = sanweiji('zhurou')

# def cars(zhizao,xinhao,**test):
#     cc={}
#     cc['zhizao']=zhizao
#     cc[xinhao]=xinhao
#     for key,value in test.items():
#         cc[key]=value
#     return cc
# car=cars('haima','tesksk',color='red',peijian='chelun')
# print(car)
# import pizza
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'ma','green','red')
# from model_name import fuction_name
# from model_name import fuction_name1,fuction_name2

# import pizza as p
# p.make_pizza(15,'pepperoni')
# p.make_pizza(11,'sksk','sjdk','sjakjd')
# from model import *

# from pizza import *
#
# make_pizza(11,'jkkdd')
# make_pizza(19,'shjd','hjkh','shjk')
#
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + 'is now sit')
#
#     def roll_over(self):
#         print(self.name.title() + 'rolled over')
#
#
# my_dog = Dog('silll', 6)
# print('my dogs name is ' + my_dog.name.title())
# print('my dogs ' + str(my_dog.age) + 'years old')
# my_dog.sit()
# my_dog.roll_over()


# class car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading=0
#
#     def read_odometer(self):
#         print(str(self.odometer_reading))
#
#     def update_odometer(self,mileage):
#         if mileage>=self.odometer_reading:
#             self.odometer_reading=mileage
#         else:
#             print('you can back minles')
#     def increment_odometer(self,miles):
#         self.odometer_reading+=miles
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_use_car=car('subar','outback',2013)
# print(my_use_car.get_descriptive_name())
# my_use_car.update_odometer(23500)
# my_use_car.read_odometer()
# my_use_car.increment_odometer(100)
# my_use_car.read_odometer()
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def xianshi(self):
#         print(str(self.number_served))
#
#     def describe_restaurant(self):
#         shijian = self.restaurant_name + ' ' + self.cuisine_type
#         return shijian
#     def set_number_serves(self, sero):
#         self.number_served = sero
#     def increment_number_served(self, ceshi):
#         self.number_served += ceshi
#     def open_restaurant(self):
#         print('zhengzaiyingye')
# cc = Restaurant('xia', 'zhifeng')
# # print(cc.describe_restaurant())
# # cc.open_restaurant()
# # cc.xianshi()
# cc.set_number_serves(20)
# cc.xianshi()
# cc.increment_number_served(100)
# cc.xianshi()
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#
#
#     def describe_user(self):
#         ur=self.first_name+' '+self.last_name
#         print(ur)
#     def greet_user(self):
#         print('hello+'+self.first_name+' '+self.last_name)
#
#
# cc=User('xai','zhifeng')
# cc.describe_user()
# cc.greet_user()
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print('this car has ' + str(self.odometer_reading))
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('you can not roll back an odometer')
#
#     def incremeter_odometer(self, miles):
#         self.odometer_reading += miles


# class Battery():
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print('this is car has a ' + str(self.battery_size) + ' k  m')
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = 'this car can go approxmately' + str(range)
#         message += 'miles on a full charge'
#         print(message)
# class ElectricCar(Car):
#
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#         self.battery_size = 70
#
#     def describe_battery(self):
#         print('this is car has a ' + str(self.battery_size) + ' k  m')
#
# def fill_gas_tank():
#     print('this car doesnt need a gas tahk')
#
#
# my_tesla = ElectricCar('tesla', 'model', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# from car import Car
# my_new_car=Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()
#
# from car import ElectricCar
# my_tes=ElectricCar('tes','model',2016)
# print(my_tes.get_descriptive_name())
# my_tes.battery.describe_battery()
# my_tes.battery.describe_battery()
# my_tes.battery.get_range()

# from car import Car,ElectricCar
#
# my_beetle=Car('volkswagen','beetle',2016)
# print(my_beetle.get_descriptive_name())
# my_tesla=ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())


# import car
# my_bettle=car.Car('volkswang','beetle',2016)
# print(my_bettle.get_descriptive_name())
# my_tesla=car.ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())
# coding=utf-8

# 读取文件
# with open('pi.txt')as file_object:
#     contents=file_object.read()
#     print(contents.rstrip())


# 文件路径，r为不转义
# with open(r'tesxt_file\filename.txt')as file_object:


# filename = 'pi.txt'
# with open(filename)as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))
#
# birthday=input('enter your birthday ,in the form mmddyy')
# if birthday in pi_string:
#     print('your birthday in pi')
# else:
#     print('your birthday does not in pi')
# filename='pi.txt'
# with open(filename,encoding='utf-8') as file_object:
#     lines=file_object.readlines()
# pi_string=[]
# for line in lines:
#     pi_string+=line.rstrip()
#     print(pi_string)
#
#     print(lines)
#     for line in lines:
#         print(line.strip())
# #写入文件
# filename='programing.txt'
# with open(filename,'w',encoding='utf-8') as file_object:
#     file_object.write('i love programing  1')
#     file_object.write('\n加换行\n')
# #问价追加内容
# with open(filename,'a')as file_object:
#     file_object.write('i love finding meaning in lang datasets\n')
#     file_object.write('i love createing apps that can run in a browser.\n')
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('you can not divide by zero')

# print('give metwo numbers,and i will divide them')
# print("enter 'q' to quit")
# while True:
#     first_number=input('\nfirst number')
#     if first_number=='q':
#         break
#     second_number=input('second_number')
#     try:
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print('you can not divide by 0')
#     else:
#         print(answer)
#
# def count_words(filename):
#     try:
#         with open(filename,'r',encoding='utf-8') as f_obj:
#             contents=f_obj.read()
#     except FileNotFoundError:
#         pass
#         # msg='sorry ,the file '+filename+' does'
#         # print(msg)
#     # else:
#     #     words=contents.split()
#     #     num_words=len(words)
#     #     print('the file '+filename+' has about '+str(num_words)
#     #           +' words')
# filename='cats.txt'
# count_words(filename)
# filenames=['programing.txt','pi.txt','c.txt','d.txt']
# for filename in filenames:
#     count_words(filename)

#
# def shuzi(shuzi1,shuzi2):
#     print('please')
#
#     shuzi2=input('please input 2 number')
# try:
#     shuzi1 = input('please input 1 number')
#     ishuzi1=int(shuzi1)
#
# except:
#     msg='qingshuru '+shuzi1
#     print(msg)
# try:
#     shuzi2 = input('please input 2 number')
#     ishuzi2 = int(shuzi2)
#
# except:
#     msg='qingshuru '+shuzi2
#     print(msg)
# else:
#     count_shuzi=ishuzi1+ishuzi2
# #     print(count_shuzi)
# def ceshi(ceshi1):
#     try:
#         with open(ceshi1,'r',encoding='utf-8') as f_ob:
#             red= f_ob.read()
#             print(red)
#     except FileNotFoundError:
#         print('文件不存在' + ceshi1)
#
# # with open('cats.txt','r',encoding='utf-8') as f_ob:
# #     red= f_ob.read()
# #     print(red)
# ceshi1222 = 'cats.txt'
# ceshi(ceshi1222)

import json
import numbers


# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename)as f_obj:
#             username=json.load(f_obj)
#     except FileNotFoundError:
#         username=input('what is you name ')
#         with open(filename,'w')as f_obj:
#             json.dump(username,f_obj)
#             print('we will remeber you when you come back '+ username)
#     else:
#         print('welcome back, '+username)
# greet_user()
# username=input('what is you name?')
#
# numbers=[2,3,5,7,9,11,13]
# filename='username.json'
# with open(filename,'w')as f_obj:
#     json.dump(username,f_obj)
#     print('we will remeber you when you come back '+ username+' !')
#
#
# filename='username.json'
# with open(filename)as f_obj:
#     username=json.load(f_obj)
#     print('welcome bac '+username+'!')



# filename='numbers.json'

# with open(filename)as f_obj:
#     numbers=json.load(f_obj)
# print(numbers)

# def get_formatted_name(first,last):
#     full_name=first+last
#     return full_name.title()

from name_function import get_formatted_name
print('enter "q" at any time to quit')
while True:
    first=input('\n please give me a first name: ')
    if first=='q':
        break
    last=input('\n please give me a last name: ')
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print("\t neatly formatted name: "+ formatted_name+ '.')

# import unittest
# from name_function import get_formatted_name
#
# class NameTestCase(unittest.TestCase):
#     '''测试name_function.py'''
#
#     def test_first_last_name(self):
#         '''能否正确处理John philiph这类名'''
#         formatted_name=get_formatted_name('xia','zhifeng')
#         self.assertEqual(formatted_name,'Xiazhifeng')
#
#
# unittest.main()

# class AnonymousSurvey():
#     '''收集匿名问卷的答案'''
#     def __init__(self,question):
#         self.question=question
#         self.responses=[]
#     def show_question(self):
#         '''显示调查问卷'''
#         print(self.question)
#     def store_response(self,new_response):
#         '''存储单份问卷'''
#         self.responses.append(new_response)
#     def show_result(self):
#         '''显示收集的所有答案'''
#         print('Survey result: ')
#         for response in self.responses:
#             print('- '+response)