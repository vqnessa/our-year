from flask import Flask, render_template

app = Flask(__name__)

timeline = [
    {"month": "January", "type": "image", "file": "m01.jpeg", "text": "The day we met in person. I felt so many sparks that day with you."},
    {"month": "February", "type": "image", "file": "m02.jpeg", "text": "Our first month together."},
    {"month": "March", "type": "image", "file": "m03.jpeg", "text": "The month I said I love you on accident. I couldn't find a good photo :("},
    {"month": "April", "type": "image", "file": "m04.jpeg", "text": "The day we both said I love you. My love has never stopped growing."},
    {"month": "May", "type": "image", "file": "m05.jpeg", "text": "Still together but followed by a month of growth. I treasure you and I want to show you that every day."},
    {"month": "June", "type": "image", "file": "m06.jpeg", "text": "Our hearts felt closer together. You're worth everything baby."},
    {"month": "July", "type": "image", "file": "m07.jpeg", "text": "Your #1 fan, now I can look at you every day."},
    {"month": "August", "type": "image", "file": "m08.jpeg", "text": "Life is so fun and beautiful with you."},
    {"month": "September", "type": "image", "file": "m09.jpeg", "text": "I got to imagine a life with you. A whole month of waking up next to you."},
    {"month": "October", "type": "image", "file": "m10.jpeg", "text": "Hootie, you're always with me in every piece of my life."},
    {"month": "November", "type": "image", "file": "m11.jpeg", "text": "Together in the city of love. Our love is constant and warm."},
    {"month": "December", "type": "video", "file": "m12.MOV", "text": "We weren't together in December but I love this video of our moments that you made. "
    "I'm completely in love with you, all of 2025 and onwards. Happy one year anniversary my love."}
]

@app.route("/")
def index():
    return render_template("index.html", timeline=timeline)

if __name__ == "__main__":
    app.run(debug=True)