def creat(): 
    link_people = []
    ketp = raw_input('want next?/y or n')
    while ketp != 'n':
        name = []
        names = raw_input('name :\n')
        name.append('name:'+names)
        year = raw_input('year:\n')
        name.append('year:'+year)
        sex = raw_input('sex:\n')
        name.append('sex:'+sex)
        link_people.append(name)
        ketp = raw_input('y or n:')
    print link_people
    return link_people
    
def check(list):
    a = 0
    check = raw_input('what name:')
    for i in range(len(list)):
        if check in list[i][0]:
            print (list[i])
            a = 1
        if i == len(list)-1 and a !=1:
            print ('no this name\n')
        

if __name__ == "__main__":
    b = creat()
    print b
    a = '1'
    while a == '1':
        check(b)
        a = raw_input('1:next or 0:exit')


