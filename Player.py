import pygame as pg
import os
pg.mixer.init()



"""
it requires pygame library.
"""
    
def play(i):
    if i is None:
        for key in dic.keys():
            pg.mixer.music.load(dic[key])
            pg.mixer.music.play()
            while pg.mixer.music.get_busy() == True:
                continue
    else:
        pg.mixer.music.load(dic[i])
        pg.mixer.music.play()
        while pg.mixer.music.get_busy() == True:
            continue
        

def filname(s):
    x=0
    name=''
    while True:
        x-=1
        if s[x]=='/':
            l=name[::-1]
            return l
        name+=s[x]
dic={}        
count=0       

def showDir(s):
    global count
    if os.path.isdir(s):
        size=0
        if '.' in s:
            pass
        else:
            try:
                for file in os.listdir(s):
                    tem=os.path.join(s,file)
                    if os.path.isfile(tem):
                        if '.mp3' in tem:
                            count+=1
                            print(count,' ',filname(tem))
                            dic[count]=tem
                    elif os.path.isdir(tem):
                        showDir(tem)
            except Exception as e:
                    print(e)
                    
if __name__=='__main__':
    print('Welcome to music palyer by pradyumn Yoohoooooooooooooooooooo')
    showDir(os.getcwd())
    
    running =True
    
    while running:
        print('Enter music no. to play that music and -1 to play all and 0 to exit')
        i=int(input())
        if i==-1:
            play(None)
        elif i==0:
            print('good byee!!!:))')
            running=False
        else:
            print('playing '+filname(dic[i]))
            play(i)
    

   
