import copy
def find_son(_dict):
    note = []
    for other in _dict:
        for i in range(len((_dict[other]['son'][0]).split(','))):
##''' print (_dict[other]['son'][0]).split(',')[i]'''
            note.append((_dict[other]['son'][0]).split(',')[i])
    for one in _dict:
        if one not in note:
            return(one)
        else:
            pass
def find_deepth(tom,_dict):
    change = _dict[tom]['son']
    print('  '*(10)+' ['+ tom +']')
    while change != ['None']:
        a = []             ##[] and [....] = [] 
        print('  '*8+' '+str(change))
        change = change[0].split(',')
        for goal in change:
            if goal in _dict:
                a = a + _dict[goal]['son']
            else:
                a = a + ['None']
        change = copy.copy(a)
        
'''if __name__ == "__main__":
    _dict={'qq': {'mother': '3', 'father': '4', 'son': ['aa,ss']}, 'ww': {'mother': '55', 'father': '66', 'son': ['zz']}, 'tom': {'mother': '1', 'father': '2', 'son': ['qq,ww,ee']}}
    b = find_son(_dict)
    find_deepth(b,_dict)'''
##'''print ('  '*(9-i)+(' '+one)*i)'''
