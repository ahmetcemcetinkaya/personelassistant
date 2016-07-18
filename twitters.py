import twitter
import voice as v
import speech_recognition as sr
api = twitter.Api(consumer_key='key',
           consumer_secret='key',
           access_token_key='key-key',
           access_token_secret='key')

def share():
    print "Say something to post on twitter \n"
    try:
      post = v.voice()
    except v.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except v.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print post
    print "We understood from your speech that and we are going to share this as a tweet.Are you sure ?  Yes/No" 
    try:
        question = v.voice()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    
    if question == "yes":
        status = api.PostUpdate(post)
        print "Tweet is shared."
    elif question == "no":
        while True:
            print "Say something to post on twitter \n"
            try:
                post = v.voice()
                print post
                print "We understood from your speech that and we are going to share this as a tweet.Are you sure ?  Yes/No"

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


            try:
                question = v.voice()
                if question == "yes":
                    status = api.PostUpdate(post)
                    print "Tweet is shared."
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            else:
                print "Could not understand audio, try again"
    else:
        print "Could not understand audio, try again"
 

                        
