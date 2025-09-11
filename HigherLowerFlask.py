from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0,9)


@app.route("/")
def guess_a_number():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Yza2YzODBtc3JrOTR5cmk5OTg3bHp5MThzYWJkM3Q5am4wYmpjOSZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/Pw4DoWaNHDj8YVCWtu/giphy.gif'</img>"

@app.route("/<int:num>")
def guessed_number(num):
    if num < random_number:
        return "<h1 color: red>Too low, try again!</h1>" \
               "<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWEzbTZrdmZub2Nzb2ttbHludndtN2U4M2hpdmVmMWhkMjNlMnFwZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1rzHSymOFmy0Do1Mb0/giphy.gif'</img>"
    elif num > random_number:
        return "<h1 color: yellow>Too high, try again!</h1>" \
               "<img src= 'https://media.giphy.com/media/TKSLd3q4TFh9jKzdQX/giphy.gif'</img>"
    else:
        return "<h1 color: green>You found me!!!</h1>" \
               "<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWEzbTZrdmZub2Nzb2ttbHludndtN2U4M2hpdmVmMWhkMjNlMnFwZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PqLcW0s1xWz0ySP6Ed/giphy.gif'</img>"

print(random_number)

if __name__ == "__main__":
    app.run(debug=True)