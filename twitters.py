import twitter
import voice as v

api = twitter.Api(consumer_key='key',
           consumer_secret='key',
           access_token_key='key',
           access_token_secret='key')

def share():
    print "Say something to post on twitter \n"
    post = v.voice() 
    print post
    print "We understood from your speech that and we are going to share this as a tweet.Are you sure ?  Yes/No" 
    question = v.voice()
 
    
    if question == "yes":
        status = api.PostUpdate(post)
        print "Tweet is shared."
    elif question == "no":
        while True:
            print "Say something to post on twitter \n"
            post = v.voice() 
            print post
            print "We understood from your speech that and we are going to share this as a tweet.Are you sure ?  Yes/No" 
            question = v.voice()
            if question == "yes":
                status = api.PostUpdate(post)
                print "Tweet is shared."
                break
            else:
                print "Could not understand audio, try again"
    else:
        print "Could not understand audio, try again"
 

                        
