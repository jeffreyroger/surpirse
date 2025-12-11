from flask import Flask, render_template, request, redirect, flash, url_for
import os
app = Flask(__name__)
app.secret_key = "supersecret123"  # needed for flash errors

# Secret password
SECRET_PASSWORD = "amizhthini"

# ------------------------- ROUTES -------------------------

@app.route("/")
def index():
    return render_template("home.html", title="Home ❤️")

@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Our Timeline ❤️")
@app.route("/quiz")
def quiz():
    questions = [
        {
            "q": "When did we first meet?",
            "options": ["Online", "College", "School", "At a shop"],
            "answer": "College"
        },
        {
            "q": "My favourite thing about you is?",
            "options": ["Your smile", "Your voice", "Your kindness", "Everything"],
            "answer": "Everything"
        },
        {
            "q": "Which date is most special to us?",
            "options": ["3rd", "5th", "7th", "12th"],
            "answer": "7th"
        },
        {
            "q": "If I could describe you in one word, it would be:",
            "options": ["Cute", "Beautiful", "Lovely", "Perfect"],
            "answer": "Perfect"
        },
        {
            "q": "How much do I love you?",
            "options": ["A little", "Medium", "A lot", "Infinity"],
            "answer": "Infinity"
        }
    ]
    return render_template("quiz.html", questions=questions)
@app.route("/quiz/result", methods=["POST"])
def quiz_result():
    score = int(request.form.get("score", 0))
    return render_template("quiz_result.html", score=score)


@app.route("/gallery")
def gallery():
    import os, random

    image_folder = os.path.join(app.static_folder, "gallery/images")
    video_folder = os.path.join(app.static_folder, "gallery/videos")

    images = [f for f in os.listdir(image_folder)
              if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]

    videos = [f for f in os.listdir(video_folder)
              if f.lower().endswith((".mp4", ".mov", ".webm"))]

    # Combine and shuffle
    media = images + videos
    random.shuffle(media)

    return render_template("gallery.html", media=media)


@app.route("/love-letter")
def love_letter():
    return render_template("love_letter.html", title="Love Letter ❤️")

@app.route("/surprise")
def surprise():
    return render_template("surprise.html", title="Surprise ❤️")

@app.route("/typing-love")
def typing_love():
    return render_template("typing_love.html", title="I Love You ❤️")

@app.route("/fireworks")
def fireworks():
    return render_template("fireworks.html", title="Fireworks ❤️")

@app.route('/polaroids')
def polaroids():
    folder = os.path.join(app.static_folder, 'polaroids')

    images = sorted(
        [img for img in os.listdir(folder) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    )

    return render_template("polaroids.html", images=images)

@app.route("/reasons")
def reasons():
    return render_template("reasons.html", title="Reasons I Love You ❤️")

# ---------------- SECRET PAGE ----------------

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    if request.method == 'POST':
        entered = request.form.get('password')
        if entered and entered.lower() == SECRET_PASSWORD.lower():
            return render_template('secret_success.html')
        else:
            flash("Incorrect password! Try again 💔", "error")
            return redirect(url_for('secret'))
    return render_template('secret.html')

# ----------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
