import sounddevice as sd
import numpy as np

fs= 44100
duration=4
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
fay=[]
way=[]
for p in range(1,fs*duration):
    fay.append(recording[0][p])
    way.append(recording[0][p])
me=open('A.txt','a')
for elem in fay:
    me.write(str(elem))
    me.write('\n')
me.close()
em=open('B.txt','a')
for elem in way:
    em.write(str(elem))
    em.write('\n')
em.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            