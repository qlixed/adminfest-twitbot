#!/usr/bin/env python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="xxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        # aca levantar el status y encolarlo para el worker.
        print(status.id,' ', status.text)
        print("-")
        print(status.user.id, status.user.description)
        return True
    #def on_private_message
        # tambien podemos monitorear el inbox de DM’s y otros estados.

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    # Faltaría hacer la parte de buscar para atras, y encolar en algo tipo previous_queue para que el worker decida si tiene que aceptarlos o no. en sucesivos runs el worker ya tiene en su db guardados los twits que proceso o skipeo para no reprocesarlos.
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['orsxg5ak'])
