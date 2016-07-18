import mailler
import os,sys
import subprocess
import time
import voice as v
import twitters
import speech_recognition as vv
import get_image as img
loop_you_mp4 = 0
loop_you_mp3 = 0 
general_time_for_shutdown= 0
choosee=""
while choosee != "write"or choosee != "voice":
    choosee = raw_input("Search with voice or just write  :  ")
    if choosee == "voice" or choosee == "write": break

if choosee== "voice":
    while True:
        print "Listen is the keyword\nYou can speak ....   "
        try:
             user_entry = v.voice()
             if user_entry == "listen":
                 print "*\nYou activated the command system, please tell me what I do.\n"
                 try:
                     a = v.voice()
                     print "You said " + str(a)

                     if a == "search":
                         print "\n\n-----Search System-----\n\n"
                         import webbrowser

                         print "Search with google"
                         try:
                             url = "https://www.google.com.tr/search?q={}".format(v.voice())
                             webbrowser.open(url)
                         except vv.UnknownValueError:
                             print("Could not understand audio, try again")
                         except vv.RequestError as e:
                             print("Could not request results from Google Speech Recognition service; {0}".format(e))


                     elif a == "hello":
                         print "\n\nHello, this script is a helper for people who wants a easy access on computer\n"
                         print "and its under the develop. You can use, improve this script.\n\n"

                     elif a == "apple" or a == "Apple":
                         print "\n\n-----Twitter Share System-----\n\n"
                         twitters.share()
                         print "\n\n"
                     elif a == "bring picture" or a == "bring Picture" or a == "bring pictures" or a == "bring picture" or a == "bring image" or a == "brings image" or a == "bring images":
                         img.download()
                     elif a == "ip":
                         output = subprocess.check_output(['cmd.exe', '/c ipconfig'])
                         print output
                     elif a == "mail":
                         mailler.main()
                     elif a == "write":
                         print "will add."

                 except vv.UnknownValueError:
                     print("Could not understand audio, try again")
                 except vv.RequestError as e:
                     print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except vv.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except vv.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        else:
            print "Could not understand audio, try again"
            
                
elif choosee == "write":
    while True:
        data = raw_input("What should I do ?\ndo .. ")
        if data == "mail" or data == "Mail":
            mailler.main()
        elif data == "ip":
            output = subprocess.check_output(['cmd.exe', '/c ipconfig'])
            print output
        elif data == "ara":
            import webbrowser
            url = "https://www.google.com.tr/search?q={}".format(raw_input("\nSearch via Mozilla   : "))  
            webbrowser.open(url)
        elif data == "go y":
            import webbrowser
            url = "www.youtube.com"
            webbrowser.open(url)
        elif data == "down y":
            choose = raw_input("Choose 1 for download the file as a video\nChoose 2 for download the file as a sound  :")
            loop_you_mp4 = 0
            if choose == "1":
                while loop_you_mp4 == 0:
                    from pytube import YouTube
                    from pprint import pprint
                    print "Write back for quit"
                    link = raw_input("Enter link : ")
                    if link == "back":
                        loop_you_mp4 = 1
                        break
                    while len(link) <  10:
                        print "Write back for quit"
                        link = raw_input("Enter link : ")
                    yt = YouTube(link)
                    
                    pprint(yt.get_videos())
                    video = yt.get(raw_input("format  : "),raw_input("resolution  : ")+"p")
                    video.download('C:\\Users\\ahmetwww\\Desktop\\youtube\\mp4\\')
            elif choose == "2": 
                while loop_you_mp3 == 0:
                    print "Write back for quit"
                    link = raw_input("Enter link : ")
                    if link =="back":
                        loop_you_mp3 = 1
                        break
                    while len(link) <  10:
                        print "Write back for quit"
                        link = raw_input("Enter link : ")
                    import youtube_dl

                    options = {'format': 'bestaudio/best','extractaudio' : True,'audioformat' : "mp3",  'outtmpl': 'C:\\Users\\ahmetwww\\Desktop\\youtube\\mp3\\%(title)s.%(ext)s', 'noplaylist' : True,} 
                    with youtube_dl.YoutubeDL(options) as ydl:
                        result = ydl.extract_info(link, download=True) 
                        print "Downloaded and converted %s successfully!" % result['title']
        elif data == "timer":
            a = raw_input("Close the system after   : ")
            b = raw_input("Hours or Minute?   :")
            if b == "hours" or b =="Hours" or b =="HOURS" or b =="hour":
                general_time_for_shutdown = int(a) * 3600
            elif b=="minute" or b == "Minutes" or b == "Minute" or b == "minutes":
                general_time_for_shutdown = int(a) * 60
            output = subprocess.check_output(['cmd.exe', '/c shutdown -s -t %s' % (general_time_for_shutdown)])
            print output
            while general_time_for_shutdown >= 1: 
                print "The computer will close in %s seconds." % (general_time_for_shutdown)
                if general_time_for_shutdown  == 20:
                     loopp = raw_input("Your computer going to close in 20 seconds if you want to cancel please write back and enter  : ")
                     if loopp == "back":
                         output = subprocess.check_output(['cmd.exe', '/c shutdown -a'])
                         print output
                         break
                     else:
                         continue
                general_time_for_shutdown-=1
                time.sleep(1)
        elif data == "back":
            mains()
            

                
                    
else:
    print "Wrong text."
    mains()

            
