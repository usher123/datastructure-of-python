import pickle
import os
from img import find_son , find_deepth
class define:
    def info_creat(self,use):
        use.setdefault(self.name,{})['mother'] = raw_input('mother\'s name:')
        use.setdefault(self.name,{})['father'] = raw_input('father\'s name:') 
        use.setdefault(self.name,{})['son'] = [raw_input('son\'s name:')]
        
    def info_name(self,use):
        self.name = raw_input("ok here we go! the name:")
        if self.name not in use:
           self.info_creat(use)
        else:
            print('have existed.')
            if raw_input('creat new one:1,exit :2\t') == '1':
                self.name = self.name + '*'
                self.info_creat(use)
            else:
                print('next people')
                pass
        
    def to_del(self,use):
        self.name = raw_input('input del name:')
        a = use.pop(self.name,None)
        if a != None:
            print( 'to del success')
        else:
            print('None this people')

    def to_print_son(self,use):
        b = find_son(use)
        find_deepth(b,use)

    def to_check(self,use):
        self.name = raw_input('to input check name:')
        b = use.get(self.name,None)
        print b
        if b != None:
            _next = raw_input('to input check info / mother,father or son:\nexit:0')
            while _next != '0':
                print(b.get(_next,0))
                _next = raw_input('please continue or exit:')
                
        else:
            print('None this people!')


def new():
    if raw_input('do you want new relationship tree? yes or no:') == 'yes':
        print('push \'ctrl + d\' to complete')
        os.system('cat > info.txt')
        a = dict()
        b = open('info.txt','w')
        pickle.dump(a,b,0)
        b.close()
    else:
        pass

if __name__ == "__main__":
    new()
    ouf = open('info.txt','r')
    use = pickle.load(ouf)
    b = define()
    deal_dict = {'1':b.info_name,'2':b.to_del,'3':b.to_print_son,'4':b.to_check}
    go =raw_input('creat:1,del:2\nprint_son:3,check:4\nexit:5\t')
    while go != '5':
        deal_dict[go](use)
        go =raw_input('continue to creat:1,del:2\nprint_son:3,check:4\nexit:5\t')
    ouf = open('info.txt','w')
    pickle.dump(use,ouf,0)
    ouf.close()
    print('bye-bye')
