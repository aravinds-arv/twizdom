import tweepy
from tkinter import *
from PIL import ImageTk, Image

CONSUMER_KEY = "sgVY9UBbkrtCNsYr7KWwvwGrM"
CONSUMER_SECRET = "pTKEglyY05nvyRzFgx2mEUknARwO7lowgL1L5SwtzY3uxNTrcp"
ACCESS_KEY = "1514259628032684033-YxrTHfmLUgotJE46Q31Vwiw1h3eaZf"
ACCESS_SECRET = "u8fYogOM7L87sEueI3KMHqEEz2tvEMwRJeCUWLeDlwgeK"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

root = Tk()
root.title("twizdom")
root.geometry("650x450")
root.configure(background="#c0deed")

twitter_logo = ImageTk.PhotoImage(Image.open("./assets/twitter.png"))
imgLabel = Label(root, image=twitter_logo, bg="#c0deed")
imgLabel.grid(row=0, column=0, pady=42, padx=250, columnspan=1)

moodLabel = Label(root, text="What's your mood today?", bg="#c0deed", font="Poppins", fg="#0084b4")
moodEntry = Entry(root, width=50, borderwidth=5, bg="#ffffff")
moodLabel.grid(row=1,column=0, padx=17)
moodEntry.grid(row=2, column=0, padx=17)

clicked = StringVar()
clicked.set("Happy")
moodMenu = OptionMenu(root, clicked, "Happy", "Sad", "Angry", "Excited", "Scared", "Surprised", "Love")
moodMenu.grid(row=3, column=0, pady=20)

tweetBtn = Button(root, text="Less go!", font=("Poppins",12), bg="#00aced", fg="#ffffff")
tweetBtn.grid(row=4, column=0, ipadx=12, ipady=4)

root.mainloop()