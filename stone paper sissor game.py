import random
choice = {'win':['rock_sissor','sissor_paper','paper_rock'],'draw':['rock_rock','sissor_sissor','paper_paper'],'lose':['sissor_rock','paper_sissor','rock_paper']}
list = ['rock','paper','sissor']
system = random.choice(list)
user = str(input('please enter your choice')).lower()
for x in (0,2):
    a=user+'_'+system
    if choice['win'][x] == a:
        print('win')
    elif choice['draw'][x] == a:
        print('draw')
    elif choice['lose'][x] == a:
        print('lose')
print(system)
