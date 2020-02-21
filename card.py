import random
card_tuple=('wzt','lb','zgl','gbwz')
package_list=[]

while 1:
    num=int(input('''
'czrnbdgq!
qxzzl
1.ck
2.ckbb
3.zlbb
4.lk'
'''))
    if num==1:
        num2=int(input('''
'qxzckcc'
'''))
        for i in range(0,num2):
            randnum=random.randint(0,3) 
            package_list.append(card_tuple[randnum])
            print('ncdl:{}'.format(card_tuple[randnum]))
    elif num==2:
        if len(package_list)==0:
            print('qxzyxfubb')
        elif len(package_list)>0:
            for i in package_list:
                print(i)
    elif num==3:
        if len(package_list)==0:
            print('qxzyxfubb')
        elif len(package_list)>0:
            package_list.sort()
            for i in package_list:
                print(i)
    elif num==4:
        break

