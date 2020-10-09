import mysql.connector as c
from tkinter import *
import os 
import pprint
import speech_recognition as sr
from googletrans import Translator
from googletrans import LANGUAGES
from pytube import YouTube
def jessica():
    screen.destroy()
    screen6.destroy()
    import pyttsx3
    import datetime
    import wikipedia
    import webbrowser
    import os
    import random
    import wolframalpha
    import requests
    
    file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3,"r")
    verify1=file1.read().splitlines()
    
    try:
        client=wolframalpha.Client('TTRGT4-28G42RHYUG')
        query2="wheater forecast of kolkata,india"
        res = client.query(query2)
        output=next(res.results).text
    except Exception as e:
        print("")

        
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.7)
    a = 6
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def translator():
        from tkinter.ttk import Combobox
        from tkinter import messagebox
        from textblob import TextBlob
        root = Tk()
        root.geometry('500x400')
        root.title('Translator')
        root.resizable(False,False)
        root.configure(bg='green')
        lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
        def translate():
            word=TextBlob(varname.get())
            lan= word.detect_language()
            lan_todict=languages.get()
            lan_to=lan_dict[lan_todict]
            word=word.translate(from_lang=lan,to=lan_to)
            varname1.set(word)
            
        def main_exit():
            rr=messagebox.askyesnocancel('Notification','Do you want to exit?',parent=root)
            if rr==True:
                root.destroy()
                
        def on_enterentry1(e):
            entry1['bg'] = 'aqua'
        def on_leaveentry1(e):
            entry1['bg']='white'
        def on_enterentry2(e):
            entry2['bg'] = 'aqua'
        def on_leaveentry2(e):
            entry2['bg']='white'


        languages=StringVar()
        font_box=Combobox(root,width=30,textvariable=languages,state='readonly')
        font_box['values']=[e for e in lan_dict.keys()]
        font_box.current(21)
        font_box.place(x=300,y=0)
        varname= StringVar()
        entry1=Entry(root,width=30,textvariable=varname,font=('times',15,'italic bold'))
        entry1.place(x=150,y=50)

        varname1= StringVar()
        entry2=Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'))
        entry2.place(x=150,y=120)

        label1=Label(root,text='Enter Words:',font=('times',15,'italic bold'),bg='green')
        label1.place(x=5,y=50)

        label2=Label(root,text='Translated:',font=('times',15,'italic bold'),bg='green')
        label2.place(x=5,y=120)

        btn1=Button(root,text='Click',command=translate,bd=5,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'))
        btn1.place(x=70,y=190)

        btn2=Button(root,text='Exit',command=main_exit,bd=5,bg='yellow',activebackground='red',width=10,font=('times',15,'italic bold'))
        btn2.place(x=280,y=190)

        entry1.bind('<Enter>',on_enterentry1)
        entry1.bind('<Leave>',on_leaveentry1)

        entry2.bind('<Enter>',on_enterentry2)
        entry2.bind('<Leave>',on_leaveentry2)



        root.mainloop()
    
    if "male" in verify1:
        gender2="male"
    else:
        gender2="female"
    gender=gender2.lower()
    if gender=='male':
        aswd='sir'
    
        def wishme():
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("good morning " + aswd)
                elif hour>=12 and hour<16:
                    speak("good afternoon " + aswd)
                else:
                    speak("good evening " + aswd)
                speak("I am jessica ")
                engine.setProperty('rate',130)
                speak("")
                engine.setProperty('rate',170)
                try:
                    speak("the temperature of the day will be "+output)
                except Exception as e:
                    speak("")
                speak("Tell me how can i help you today")

            
        wishme()

        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=0.6
                r.energy_threshold=250
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "

        while a==6:
            query=takecommand()
            if query=="    ":
                print()
            
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "instagram" in query:
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak(i+1) 
                        print(results[i])
                        speak(results[i])  
                NewsFromBBC()
            elif "play music" in query:
                music_dir='C:\music'
                awer=random.randint(0,1)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif "play some music" in query:
                music_dir='C:\music'
                awer=random.randint(0,1)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif "play movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "godzilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry sir")
                    speak("there are no such movies in the directory")
                    speak("but sir if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif "download movie" in query:
                speak("type the name of the movie you want to download")
                moviename=input("::>>")
                wholename=""
                k=len(moviename)
                i=0
                while i<k:
                    if moviename[i]==" ":
                        wholename+="%20"
                    else:
                        wholename+=moviename[i]
                    i+=1
                totalname="https://www.1337x.am/search/"+wholename +"/1/"
                webbrowser.open(totalname)

            elif "download a movie" in query:
                speak("type the name of the movie you want to download")
                moviename=input("::>>")
                wholename=""
                k=len(moviename)
                i=0
                while i<k:
                    if moviename[i]==" ":
                        wholename+="%20"
                    else:
                        wholename+=moviename[i]
                    i+=1
                totalname="https://www.1337x.am/search/"+wholename +"/1/"
                webbrowser.open(totalname)
            
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                a=7
            elif "shut down yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                a=7

            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif "download youtube video" in query:
                speak("Enter the link of the youtube video")
                link=input("Enter the link of youtube video:")
                yt=YouTube(link)
                try:
                    videos=yt.streams.filter(progressive=True).all()
                    i=1
                    for streams in videos:
                        print(str(i)  +"  " + str(streams))
                        i+=1
                    speak("Select the quality you want to download")
                    stream_input=int(input("Enter the Number:"))
                    video=videos[stream_input-1]
                    print("Downloading....")
                    speak("please wait the video is downloading")
                    video.download("C:\\Users\\my computer\\Desktop")
                    print("Downloaded")
                except:
                    speak("youtube video not found")
            elif "download a youtube video" in query:
                speak("Enter the link of the youtube video")
                link=input("Enter the link of youtube video:")
                yt=YouTube(link)
                try:
                    videos=yt.streams.filter(progressive=True).all()
                    i=1
                    for streams in videos:
                        print(str(i)  +"  " + str(streams))
                        i+=1
                    speak("Select the quality you want to download")
                    stream_input=int(input("Enter the Number:"))
                    video=videos[stream_input-1]
                    print("Downloading....")
                    speak("please wait the video is downloading")
                    video.download("C:\\Users\\my computer\\Desktop")
                    print("Downloaded")
                except:
                    speak("youtube video not found")



            elif "translate" in query:
                translator()
            elif "translator" in query:
                translator()
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry sir")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name is jessica")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse "+aswd)
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "are a male" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "are you boy or man" in query :
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "show me your face" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i don't have handsome face like yours")
            elif "hi" in query:
                speak("hi "+aswd)
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="jessica":
                speak("yes "+aswd)
            elif "i am fine" in query:
                speak("you surely are, "+aswd)
            elif "i am ok" in query:
                speak("i know "+aswd)
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("sir,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "i love you" in query:
                speak("oh!thank you "+aswd)
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse "+aswd +" I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome "+aswd)
            elif "dont call me sir" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "sing a song" in query:
                speak("sorry i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you "+aswd)
            elif "tell me about you" in query:
                speak("i am jessica")
                speak(" i am an artificial intilligence")
                speak("i will do what you tell me to do")
                speak("sir i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "your favourite sport" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except:
                    try:
                        results = wikipedia.summary(query,sentences=3)
                        speak("according to wikipedia")
                        speak(results)
                    except:
                        speak("sorry sir!")
                        speak("i cannot execute your command!")
    else:
        aswd='maam'
        def wishme():
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("good morning " + aswd)
                elif hour>=12 and hour<16:
                    speak("good afternoon " + aswd)
                else:
                    speak("good evening " + aswd)
                speak("I am jessica ")
                engine.setProperty('rate',130)
                speak("")
                engine.setProperty('rate',170)
                try:
                    speak("the temperature of the day will be "+output)
                except Exception as e:
                    speak("")
                speak("Tell me how can i help you today")

            
        wishme()

        def takecommand():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold=0.6
                r.energy_threshold=250
                audio = r.listen(source)
            try:
                print("Recognising......")
                text= r.recognize_google(audio)
                print(text)
                return text.lower()
            except:
                print("Say that again please.....")
                return "    "

        while a==6:
            query=takecommand()
            if query=="    ":
                print()
            
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                webbrowser.open("www.google.com")
            elif "axis bank" in query:
                webbrowser.open("https://www.axisbank.com")
            elif "icici" in query:
                webbrowser.open("WWW.ICICIBANK.COM")
            elif "bank of baroda" in query:
                webbrowser.open("http://www.bobibanking.in")
            elif "sbi" in query:
                webbrowser.open("WWW.ONLINESBI.COM ")
            elif "instagram" in query:
                webbrowser.open("www.instagram.com/")
            elif "facebook" in query:
                speak("Openning facebook")
                webbrowser.open("www.facebook.com/")
            elif " date" in query:
                sk2=datetime.datetime.now()
                sk1=str(sk2)
                sk=str(sk1[0:10])
                speak("the date is")
                speak(sk)
            elif "the time" in query:
                sk2=datetime.datetime.now()
                k=sk2.strftime("%H:%M:%S")
                k0=k.replace(":","")
                k1=k0[0:2]+"hours"
                k2=k0[2:4]+"minutes"
                k3=k0[4:]+"seconds"
                k5=k1+k2+"and"+k3
                print(k)
                speak("the time is")
                speak(k5) 

            elif "news" in query:
                def NewsFromBBC(): 
                    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5687b7b46e604878966b9a48e6f52af6"
                    open_bbc_page = requests.get(main_url).json() 
                    article = open_bbc_page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)):
                        speak(i+1) 
                        print(results[i])
                        speak(results[i])  
                NewsFromBBC()
            elif "play music" in query:
                music_dir='C:\music'
                awer=random.randint(0,1)
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[awer]))
            elif "play movie" in query:
                speak("which movie you want me to play")
                o1=input("Name the movie:")
                o=o1.lower()
                if "your name" in o:
                    music_dir='D:\HOLLYWOOD\[TorrentCounter.to].Your.Name.2016.English.Dubbed.[Kimi.no.Na.wa].1080p.BluRay.x264.[1.5GB].mp4'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "alita battle angel" in o:
                    music_dir='D:\HOLLYWOOD\Alita Battle Angel (2019) [WEBRip] [1080p] [YTS.LT]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "finding nemo" in o:
                    music_dir='D:\HOLLYWOOD\Finding Nemo (2003) [1080p]'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                elif "gozilla" in o:
                    music_dir='D:\HOLLYWOOD\Godzilla (2014)'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                else:
                    speak("sorry sir")
                    speak("there are no such movies in the directory")
                    speak("but sir if you want to see the movie ")
                    speak("i can do it")
                    speak("i can start the VPN and play the movie for you")
                    speak("should i proceed?")
                    asd=input("???")
                    if asd=="yes" or asd == "yeah" or asd =="of course":
                        speak("once the website opens,you have to pass human verification and then you have to search the movie")
                        webbrowser.open("https://openloadmovies.ac/")

            elif "download movie" in query:
                speak("type the name of the movie you want to download")
                a=input("::>>")
                s=""
                k=len(a)
                i=0
                while i<k:
                    if a[i]==" ":
                        s+="%20"
                    else:
                        s+=a[i]
                    i+=1
                d="https://www.1337x.am/search/"+s +"/1/"
                webbrowser.open(d)

            elif "download a movie" in query:
                speak("type the name of the movie you want to download")
                a=input("::>>")
                s=""
                k=len(a)
                i=0
                while i<k:
                    if a[i]==" ":
                        s+="%20"
                    else:
                        s+=a[i]
                    i+=1
                d="https://www.1337x.am/search/"+s +"/1/"
                webbrowser.open(d)
            
            elif "shutdown yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                a=7
            elif "shut down yourself" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                a=7

            elif "shutdown the computer" in query:
                speak("ok!")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("enjoy your day "+aswd)
                elif hour>=18 and hour<21:
                    speak("enjoy your evening "+aswd)
                else:
                    speak("have sweet dreams "+aswd)
                os.system("shutdown /s /t 0")
            elif "ping" in query:
                speak("please type the site to count the ping")
                awe=input("enter the site:")
                aw2="ping "+awe
                result=os.system(aw2)
            elif "download youtube video" in query:
                speak("Enter the link of the youtube video")
                link=input("Enter the link of youtube video:")
                yt=YouTube(link)
                try:
                    videos=yt.streams.filter(progressive=True).all()
                    i=1
                    for streams in videos:
                        print(str(i)  +"  " + str(streams))
                        i+=1
                    speak("Select the quality you want to download")
                    stream_input=int(input("Enter the Number:"))
                    video=videos[stream_input-1]
                    print("Downloading....")
                    speak("please wait the video is downloading")
                    video.download("C:\\Users\\my computer\\Desktop")
                    print("Downloaded")
                except:
                    speak("youtube video not found")
            elif "download a youtube video" in query:
                speak("Enter the link of the youtube video")
                link=input("Enter the link of youtube video:")
                yt=YouTube(link)
                try:
                    videos=yt.streams.filter(progressive=True).all()
                    i=1
                    for streams in videos:
                        print(str(i)  +"  " + str(streams))
                        i+=1
                    speak("Select the quality you want to download")
                    stream_input=int(input("Enter the Number:"))
                    video=videos[stream_input-1]
                    print("Downloading....")
                    speak("please wait the video is downloading")
                    video.download("C:\\Users\\my computer\\Desktop")
                    print("Downloaded")
                except:
                    speak("youtube video not found")



            elif "translate" in query:
                trans = Translator()
                a=input("Write the text and I will translate it for you:")
                for lang in LANGUAGES:
                    print(f'{lang}-{LANGUAGES[lang]}')
                k=input("In which language you want to translate it::Write only code words-->>")
                t= trans.translate(a,dest=k)
                print(f'Source: {t.src}')
                print(f'Destination: {t.dest}')
                print(f'{t.origin} -> {t.text}')
                pm=t.extra_data['possible-mistakes']
                pt=t.extra_data['possible-translations']
                print(f'Possible Mistake:{pm}')
                print(f'Possible Translation:{pt}')
            elif "translator" in query:
                trans = Translator()
                a=input("Write the text and I will translate it for you:")
                for lang in LANGUAGES:
                    print(f'{lang}-{LANGUAGES[lang]}')
                k=input("In which language you want to translate it::Write only code words-->>")
                t= trans.translate(a,dest=k)
                print(f'Source: {t.src}')
                print(f'Destination: {t.dest}')
                print(f'{t.origin} -> {t.text}')
                pm=t.extra_data['possible-mistakes']
                pt=t.extra_data['possible-translations']
                print(f'Possible Mistake:{pm}')
                print(f'Possible Translation:{pt}')
            elif "joke" in query:
                speak("how does a train eats?")    
                speak("it chew-chews")
                a1s=input("")
                if "one more" in a1s:
                    speak("why doesn't anyone laugh at pizza jokes?") 
                    speak("because it's too cheesy")
                    a2s=input("one more?")  
                    if "yes" in a2s:
                        speak("why can't elephants use computers?") 
                        speak("because they are scared of the mouse") 
                        a3s=input("one more?")   
                        if "yes" in a3s:
                            speak("why are football stadiums so cool?")
                            speak("because every seat has a fan on it")
                            a4s=input("one more?")
                            if "yes" in a4s:
                                speak("here we go")
                                speak("why are fish so smart?")
                                speak("because they spend a lot of time hanging out for school")
                                a5s=input("one more?")
                                if "yes" in a5s:
                                    speak("where do cows go to have fun?")
                                    speak("to the moooooooovies!")
                                    a6s=input("one more?")
                                    if "yes" in a6s:
                                        speak("sorry sir")
                                        speak("i can do this much only")
                                        speak("i have been programed with this much humour")
            elif "what is your name" in query:
                speak("my name is jessica")
                speak("i am an artificial intilligence")
            elif "am i beautiful" in query:
                speak("ofcourse "+aswd)
                speak("you are beautiful") 
            elif "are you male or female" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "are a male" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "are you boy or man" in query :
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
                speak("so i am nither male nor female")
                speak("but i have female voice")
            elif "show me your face" in query:
                speak(aswd+" i am genderless and formless")
                speak("you can't see me as an individual figure")
                speak("i am program")
                speak("so i don't have handsome face like yours")
            elif "hi" in query:
                speak("hi "+aswd)
            elif "how are you" in query:
                speak("i am always okay")
                speak("as long as i am provided with electricity.")
                speak("and thanks for asking")
                speak("i am feeling positively tip top")
            elif query=="jessica":
                speak("yes "+aswd)
            elif "i am fine" in query:
                speak("you surely are, "+aswd)
            elif "i am ok" in query:
                speak("i know "+aswd)
            elif "quote" in query:
                speak("here are some quotes")
                speak("success is not final;failure is not fatal:it is the courage that counts")
                a1a=input("do you want to hear one more:")
                if "yes" in a1a:
                    speak("success usually comes to those who are too busy to be looking for it")
                    a2a=input("do you want to hear one more:")
                    if "yes" in a2a:
                        speak("dont't be afraid to give up the good to go for the great")
                        a3a=input("do you want to hear one more:")
                        if "yes" in a3a:
                            speak("if you are not willing to risk the usual,you will have to settle for the ordinary")
                            a4a=input("do you want to hear one more:")
                            if "yes" in a4a:
                                speak("the ones who are crazy enough to think they can change the world,are the ones that do.")
                                a5a=input("do you want to hear one more:")
                                if "yes" in a5a:
                                    speak("if you really look closely,most overnight successes took a long time.")
                                    a6a=input("do you want to hear one more:")
                                    if "yes" in a6a:
                                        speak("the only limit to your realization of tommorow will be our doubts of today.")
                                        a7a=input("do you want to hear one more:")
                                        if "yes" in a7a:
                                            speak("the successful warrior is the average man,with laser like focus")
                                            a8a=input("do you want to hear one more:")
                                            if "yes" in a8a:
                                                speak("i cannot give the formula for success,but i can give you the formula for failure")
                                                speak("it is,try to please everybody")
                                                a9a=input("do you want to hear one more:")
                                                if "yes" in a9a:
                                                    speak("success is not the key to happiness.happiness is the key to success.if you love what you are doing,you will be successful")
                                                    a10a=input("do you want to hear one more:")
                                                    if "yes" in a10a:
                                                        speak("the difference between who you are,and what you want to be,is what you do")
                                                        a11a=input("do you want to hear one more:")
                                                        if "yes" in a11a:
                                                            speak("the only place where success comes before hardwork,is in the dictionary")
                                                            a12a=input("do you want to hear one more:")
                                                            if "yes" in a12a:
                                                                speak("the pain you feel today will be the strength you have tomorrow")
                                                                speak("sir,please don't ask me anymore")
                                                                speak("i am out of stock")
            elif "i love you" in query:
                speak("oh!thank you "+aswd)
                speak("i love you more")
            elif "do you love me" in query:
                speak("ofcourse "+aswd +" I love you more then anything in this world")
            elif "thank" in query:
                speak("awh!your are welcome "+aswd)
            elif "dont call me sir" in query:
                speak("then what should i call you?")
                a1w=input("write the name")
                sdf="oh! hi" + a1w
                speak(sdf)
            elif "sing a song" in query:
                speak("sorry i am a bad singer")
                speak("i can't sing")
            elif "sing song" in query:
                speak("sorry i am a bad singer")
                speak("i can't sing")
            elif "read a book for me" in query:
                speak("reading needs lonliness")
                speak("i can't read a book for you")
                speak("you will not be interested in the story")
            elif "kill yourself" in query:
                speak("i can't kill myself")
                speak("i can switch my self off")
            elif "play a game" in query:
                speak("playing video game is a funtime")
                speak("i don't want to snatch your fun from you")
            elif "gain knowledge" in query:
                speak("read books")
                speak("as simple as that")
            elif "shortcut keys on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "shortcuts on keyboard" in query:
                speak("to open file in the current software press ")
                speak("control plus o")
                speak("to create a new document press")
                speak("control plus n")
                speak("if you want more shortcuts go to the website computerhope.com")
            elif "you are beautiful" in query :
                speak("thank you "+aswd)
            elif "tell me about you" in query:
                speak("i am jessica")
                speak(" i am an artificial intilligence")
                speak("i will you what you tell me to do")
                speak("sir i am formless")
                speak("you can't see me as an individual figure")
                speak("i am a program")
            elif "what can you do for me" in query:
                speak("just ask")
                speak("i can do whatever you tell me to do")
            elif "do something" in query:
                speak("do what?")
            elif "you like football" in query:
                speak("yes! i love seeing so many goal-oriented people in one place")
            elif "favourite football player" in query:
                speak("the ram")
                speak("he is tiny")
                speak("but i bet he runs fast")
            elif "your favourite sports" in query:
                speak("i don't know!maybe")
                speak("football")
            elif "you can't play" in query:
                speak("many people can't do many things")
                speak("but they still love those things")
            elif query=="oh!" in query:
                speak("hm") 
            elif "watching sports is great" in query:
                speak("yes!")
                speak("it is great")
                speak("it makes you feel energetic")
            elif "makes you a good ai" in query:
                speak("it should have patterns to its behaviour,a certain level of consistency over time and space")
                speak("the AI should respond to its enviroment and its opponents")
                speak("it should keep using techniques that are working,and discard techniques that aren't working ")
            else:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    speak(output)
                except:
                    try:
                        results = wikipedia.summary(query,sentences=3)
                        speak("according to wikipedia")
                        speak(results)
                    except:
                        speak("sorry sir!")
                        speak("i cannot execute your command!")
        
            
def login_success():
    global screen6
    screen4.destroy()
    screen5.destroy()
    screen6=Tk()
    screen6.config(bg="purple")
    screen6.geometry("500x500")
    screen6.title("Desktop Assistant")
    Label(screen6,text="Choose your favourite assistant",bg="black",fg="white",width="500",height="3",font=20).pack()
    Label(screen6,text="",bg="purple").pack()
    Button(screen6,text="JESSICA",bg="blue",fg="aqua",height="3",width="20",command=jessica).pack()
def login_again():
    screen5.destroy()
def login_user():
    import datetime
    global screen5
    global username3
    sk21=datetime.datetime.now()
    sk=str(sk21)
    sk=sk[0:10]
    sk2=datetime.datetime.now()
    k1=sk2.strftime("%H:%M:%S")
    k=str(k1)
    password4=password3.get()
    username3=username2.get()
    files=os.listdir()
    if "AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3 in files:
        file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username3,"r")
        info=file1.read().splitlines()
        if password4 in info:
            screen5=Tk()
            screen5.config(bg="yellow")
            screen5.title("Login Status")
            screen5.geometry("150x150")
            Label(screen5,text="Login Successful",bg="yellow",fg="green",font=15).pack()
            Label(screen5,text="",bg="yellow").pack()
            Button(screen5,text="Ok",height="2",width="8",command=login_success).pack()
            file1=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm1"+username3,"w")
            file1.write(sk+"\n")
            file1.write(k+"\n")
            file1.close()
        else:
            screen5=Tk()
            screen5.config(bg="yellow")
            screen5.title("Login Status")
            screen5.geometry("150x150")
            Label(screen5,text="Password is incorrect",bg="yellow",fg="red",font=15).pack()
            Label(screen5,text="",bg="yellow").pack()
            Button(screen5,text="Ok",height="2",width="8",command=login_again).pack()
    else:
        screen5=Tk()
        screen5.config(bg="yellow")
        screen5.title("Login Status")
        screen5.geometry("150x150")
        Label(screen5,text="Username not found",bg="yellow",fg="red",font=15).pack()
        Label(screen5,text="",bg="yellow").pack()
        Button(screen5,text="Ok",height="2",width="8",command=login_again).pack()
    username2.delete(0,END)
    password3.delete(0,END)
def login():
    global screen4
    global username2
    global password3
    password3 = StringVar()
    username2=StringVar()
    screen4=Tk()
    screen4.config(bg="green")
    screen4.title("Login Terminal")
    screen4.geometry("250x250")
    Label(screen4,text="Login here",bg="green",font=("TIMES NEW ROMAN",20,"bold")).pack()
    Label(screen4,text="",bg="green").pack()
    Label(screen4,text="Username",bg="green",font=10).pack()
    username2=Entry(screen4,textvariable=username2)
    username2.pack()
    Label(screen4,text="Password",bg="green",font=10).pack()
    password3=Entry(screen4,textvariable=password3,show="*")
    password3.pack()
    Label(screen4,text="",bg="green").pack()
    Button(screen4,text="Login",bg="light green",height="1",width="8",command=login_user).pack()
    
    
def login_after_registering():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
def login_from_register():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()
def register_again():
    screen3.destroy()
def register_user():
    global fullname1
    global password1
    global gender1
    global passcode
    global username1
    fullname1=fullname.get()
    username1=username.get()
    password1=password.get()
    password2=type_password.get()
    gender1=gender.get()
    passcode1=passcode.get()
    global screen3
    screen3=Tk()
    screen3.config(bg="yellow")
    screen3.title("Registration Status")
    screen3.geometry("300x250")
    if fullname1=="":
        Label(screen3,text="Name is required for registration",bg="yellow",fg="red",font=15).pack()
        Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
        Label(screen3,text="",bg="yellow").pack()
        Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
        Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
    else:
        if username1=="":
            Label(screen3,text="Username is required for registration",bg="yellow",fg="red",font=15).pack()
            Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
            Label(screen3,text="",bg="yellow").pack()
            Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
            Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
        else:
            if password1!=password2:
                Label(screen3,text="Passwords didn't match",bg="yellow",fg="red",font=15).pack()
                Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                Label(screen3,text="",bg="yellow").pack()
                Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
            else:
                if gender1=="":
                    Label(screen3,text="Gender is required for registration",bg="yellow",fg="red",font=15).pack()
                    Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                    Label(screen3,text="",bg="yellow").pack()
                    Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                    Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
                else:
                    if passcode1!="mayday":
                        Label(screen3,text="Passcode is incorrect",bg="yellow",fg="red",font=15).pack()
                        Button(screen3,text="Ok",height="2",width="8",command=register_again).pack()
                        Label(screen3,text="",bg="yellow").pack()
                        Label(screen3,text="Already have an account",bg="yellow",fg="Green",font=15).pack()
                        Button(screen3,text="Login",height="2",width="8",command=login_from_register).pack()
                    else:
                        file=open("AI_account_qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"+username1,"w")
                        file.write(fullname1+"\n")
                        file.write(gender1+"\n")
                        file.write(password1+"\n")
                        file.close()
                        Label(screen3,text="Your account is registered successfully",bg="yellow",fg="green",font=15).pack()
                        Button(screen3,text="Ok",height="2",width="7",command=login_after_registering).pack()
                        
    fullname.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    type_password.delete(0,END)
    gender.delete(0,END)
    passcode.delete(0,END)
    
def register():
    global screen2
    global fullname
    global username
    global password
    global type_password
    global gender
    global passcode
    passcode=StringVar()
    gender=StringVar()
    type_password=StringVar()
    password=StringVar()
    username=StringVar()
    fullname=StringVar()
    screen2=Tk()
    screen2.geometry("350x450")
    screen2.config(bg="aqua")
    screen2.title("Registration Terminal")
    Label(screen2,text="Please Give The Details To Register",fg="blue",bg="aqua",font=("times new roman",15,"bold")).pack()
    Label(screen2,text="",bg="aqua").pack()
    Label(screen2,text="Fullname",bg="aqua").pack()
    fullname=Entry(screen2,textvariable=fullname)
    fullname.pack()
    Label(screen2,text="Username",bg="aqua").pack()
    username=Entry(screen2,textvariable=username)
    username.pack()
    Label(screen2,text="Set Password",bg="aqua").pack()
    password=Entry(screen2,textvariable=password,show="*")
    password.pack()
    Label(screen2,text="Match Password",bg="aqua").pack()
    type_password=Entry(screen2,textvariable=type_password,show="*")
    type_password.pack()
    Label(screen2,text="Gender",bg="aqua").pack()
    gender=Entry(screen2,textvariable=gender)
    gender.pack()
    Label(screen2,text="Passcode",bg="aqua").pack()
    passcode=Entry(screen2,textvariable=passcode,show="#")
    passcode.pack()
    Label(screen2,text="",bg="aqua").pack()
    Button(screen2,text="Register",bg="blue",fg="white",height="2",width="10",command=register_user).pack()
def mainscreen():
    global screen
    screen=Tk()
    screen.geometry("700x400")
    screen.title("AI Access Terminal")
    screen.config(bg="black")
    Label(text="Welcome To The Age Of New Technology",bg="black",fg="white",font=("Algerian",24,"underline")).pack()
    Label(text="",bg="black").pack()
    Label(text="",bg="black").pack()
    Button(text="Login",height="5",width="50",bg="green",fg="white",font=("times new roman",12,"bold"),command=login).pack()
    Label(text="",bg="black").pack()
    Label(text="",bg="black").pack()
    Button(text="Register",height="5",width="50",bg="blue",fg="white",font=("times new roman",12,"bold"),command = register).pack()
    
    screen.mainloop()
mainscreen()
