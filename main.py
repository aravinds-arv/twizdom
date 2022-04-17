from io import BytesIO
import tweepy
import random
import textwrap
import requests, json
from tkinter import *
from PIL import ImageTk, Image
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont

CONSUMER_KEY = "L1K7CFCPvOlJZVJAyI6oxdq85"
CONSUMER_SECRET = "PVeybBGJ4LWwvaAC2h1oSF5lYBJbfba2XyV3sHyzW32AnCwPEC"
ACCESS_KEY = "1356929686387912706-vSCiebzuDdFD3upJPUxivswHcPQmKJ"
ACCESS_SECRET = "t5tBkQ0PmE6KXoQrCPXLhoyynGLqznEfhyOIZenge6FPr"

TOKEN = 'f45946f5d9d776657ae77c4905ce41ff9c800149'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def createImg(text):
    img = Image.open(fp='./assets/tweet.jpg', mode='r')
    draw = ImageDraw.Draw(im=img)
    font = ImageFont.truetype(font='./assets/SourceCodePro-Bold.ttf', size=42)
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    max_char_count = int(img.size[0] * .618 / avg_char_width)
    text = textwrap.fill(text=text, width=max_char_count)
    draw.text(xy=(img.size[0]/2, img.size[1] / 2), text=text, font=font, fill='#ffffff', anchor='mm')
    img.save("./assets/quote1.png")

root = Tk()
root.title("twizdom")
root.geometry("650x450")
root.configure(background="#c0deed")

def tweetFn():
    global clicked
    # mood = moodEntry.get()
    moodOption = clicked.get()
    if moodOption:
        PAPERQUOTES_API_ENDPOINT = f'https://api.paperquotes.com/apiv1/quotes/?tags={moodOption}&random=random&limit=200'
        response = requests.get(PAPERQUOTES_API_ENDPOINT, headers={'Authorization': f'TOKEN {TOKEN}'})
        if response.ok:
            quotes = json.loads(response.text).get('results')
            quotes_list = []
            for quote in quotes:
                quote_single = {}
                quote_single['quote'] = quote.get('quote')
                quote_single['author'] = quote.get('author')
                quotes_list.append(quote_single)
            try:
                quote_choice = random.choice(quotes_list)
                quote_text = f'''{quote_choice.get('quote')}
                \u000a\u000a\u0009\u0009-{quote_choice.get('author')}'''
                createImg(quote_text)
                api.update_status_with_media(status=None, filename="./assets/quote1.png")
            except:
                tweepy.Forbidden()
                quote_choice = random.choice(quotes_list)
                createImg(quote_choice)
                api.update_status(f"{quote_choice.get('quote')}\n-{quote_choice.get('author')}")
            statusLabel = Label(root, text="Head to your profile to receive tWizdom!", font=("Poppins",10), bg="#c0deed", fg="#ffffff")
            statusLabel.grid(row=5, column=0, pady=10)
            root.after(2000, lambda : statusLabel.grid_forget())

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