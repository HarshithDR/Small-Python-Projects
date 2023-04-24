import requests
number = input('How many number of documents should be downloaded: ')
variable_list = []
for b in range(0,int(number)):
    variable_list.append("variable"+str(b))
for i in range(0,int(number)):
    variable_list[i] = input('Enter the pdf '+str(i+1)+' link: ')
for x in range(0,int(number)):
    try:
        r = requests.get(variable_list[x], stream=True)
        with open('C:\\Users\\91911\\Desktop\\'+str(x+1)+'.pdf', 'wb') as f:
            f.write(r.content)
        print('successfully downloaded..')
    except:
        print('Download ERROR!')