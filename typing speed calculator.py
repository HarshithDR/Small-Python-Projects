import time as t
import matplotlib.pyplot as p
times=[]
mistakes=0
print('this program will help you type faster, you will have to type the word "programming" as fast as you can for five times')
input('press enter to continue')
while len(times)<5:
    start=t.time()
    word=input('type the word').lower()
    end =t.time()
    time_taken=end-start
    times.append(time_taken)
    if word!='programming':
        mistakes+=1
print('you have done ',mistakes,'mistakes')
print('lets see evaluation')
t.sleep(2)
x=['1','2','3','4','5']
y=times
p.plot(x,y)
p.xlabel('attempts')
p.ylabel('seconds')
p.title('typing speed calculator')
p.show()
    
