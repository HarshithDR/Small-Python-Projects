from pydub import AudioSegment

#AudioSegment.ffmpeg = 'C:\\Python36\\Lib\\ffmpeg\\bin\\ffmpeg.exe'
#AudioSegment.converter = "C:\\Python36\\Lib\\ffmpeg\\bin\\ffmpeg.exe"

# file_path = 'C:\\Users\\91911\\Desktop\\audio1.mp3'
#file_name = 'audio1.mp3'
# import subprocess
# subprocess.Popen(['mpg123','-q', 'audio1.mp3']).wait()
for y in range(8,11):
    for x in range(0,31):

        startMin = x * 2
        # startSec = 0

        endMin = startMin + 2
        # endSec = 0

        # Time to miliseconds
        # startTime = startMin*60*1000+startSec*1000
        # endTime = endMin*60*1000+endSec*1000

        startTime = startMin * 60 * 1000
        endTime = endMin * 60* 1000
        path = 'C:\\Users\\harsh\\OneDrive\\Desktop\\Dataset\\Background\\Animals'

        # Opening file and extracting segment
        song = AudioSegment.from_mp3(path + '\\original\\Animals.' +str(y)+'.mp3')
        #song = AudioSegment.from_mp3('C:\\Users\\91911\\Desktop\\audio2.' + str(y) + '.mp3')
        extract = song[startTime:endTime]

        # Saving
        extract.export(path+'\\Animals.' + str(y) + '.' + str(x) + '.mp3', format="mp3")
        #extract.export('river-1.'+ str(x) + '.mp3', format="mp3")
