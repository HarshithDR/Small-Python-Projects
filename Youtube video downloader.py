from pytube import YouTube
download_path = 'C:\\Users\\91911\\Desktop'
number = input('How many number of videos should be downloaded: ')
variable_list = []
for b in range(0,int(number)):
    variable_list.append("variable"+str(b))
for i in range(0,int(number)):
    variable_list[i] = input('Enter the youtube '+str(i+1)+' video link: ')
    # variable_list.append(input('Enter the youtube '+str(i+1)+' video link: '))
for x in range(0, int(number)):
    yt = YouTube(variable_list[x])
    videos = yt.streams.all()
    video = videos[0]
    try:
        video.download(download_path)
        print('Download Successful')
    except:
        print('Download ERROR!')