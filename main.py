import tweepy
import requests, json
from tkinter import *
from PIL import ImageTk, Image

CONSUMER_KEY = "L1K7CFCPvOlJZVJAyI6oxdq85"
CONSUMER_SECRET = "PVeybBGJ4LWwvaAC2h1oSF5lYBJbfba2XyV3sHyzW32AnCwPEC"
ACCESS_KEY = "1356929686387912706-vSCiebzuDdFD3upJPUxivswHcPQmKJ"
ACCESS_SECRET = "t5tBkQ0PmE6KXoQrCPXLhoyynGLqznEfhyOIZenge6FPr"


TOKEN = 'f45946f5d9d776657ae77c4905ce41ff9c800149'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

root = Tk()
root.title("twizdom")
root.geometry("650x450")
root.configure(background="#c0deed")

def tweetFn():
    global clicked
    # mood = moodEntry.get()
    moodOption = clicked.get()
    if moodOption:
        PAPERQUOTES_API_ENDPOINT = f'https://api.paperquotes.com/apiv1/quotes/?tags={moodOption}&random=random&order=?&limit=1'
        response = requests.get(PAPERQUOTES_API_ENDPOINT, headers={'Authorization': 'TOKEN {}'.format(TOKEN)})
        if response.ok:
            quotes = json.loads(response.text).get('results')
        for quote in quotes:
            tweet = quote.get('quote')
        api.update_status(tweet)
        print("Updated")

twitter_logo = ImageTk.PhotoImage(Image.open("./assets/twitter.png"))
imgLabel = Label(root, image=twitter_logo, bg="#c0deed")
imgLabel.grid(row=0, column=0, pady=42, padx=250, columnspan=1)

moodLabel = Label(root, text="What's your mood today?", bg="#c0deed", font="Poppins", fg="#0084b4")
# moodEntry = Entry(root, width=50, borderwidth=5, bg="#ffffff")
moodLabel.grid(row=1,column=0, padx=17)
# moodEntry.grid(row=2, column=0, padx=17)

clicked = StringVar()
clicked.set("Happy")
moodMenu = OptionMenu(root, clicked, "Happy", "Sad", "Angry", "Excited", "Scared", "Surprised", "Love")
moodMenu.grid(row=3, column=0, pady=20)

tweetBtn = Button(root,command=tweetFn, text="Less go!", font=("Poppins",12), bg="#00aced", fg="#ffffff")
tweetBtn.grid(row=4, column=0, ipadx=12, ipady=4)

root.mainloop()