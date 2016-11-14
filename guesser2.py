import webapp2
import random


def random_gen():
    global rnd
    rnd = random.randrange(1,100)

global rnd
rnd = 0
random_gen()

form = """
<p>guess a number 1-100!</p>
<form method="post" action="/guesser">
<input name="guess">
<input type="submit" value="guess">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        random_gen()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h1>Welcome to Alex's Number Guesser Game</h1>")
        self.response.write(form)

class GuessHandler(webapp2.RequestHandler):
    def post(self):
        global rnd
        g = self.request.get("guess")
        self.response.write("you guessed: "+ str(g))
        if(g.isdigit()):
            self.response.write("<br>the answer was: "+ str(rnd))
            if(int(g) == int(rnd)):
                self.response.write("<br>you are correct")
            else:
                self.response.write("<br>you were wrong,")
                if(int(g) < int(rnd)):
                    self.response.write(" you guessed too low")
                else:
                    self.response.write(" you guessed too high")
                self.response.write(form)
        else:
            self.response.write("<br>please enter a number (this guess was not counted)")
            self.response.write(form)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/guesser', GuessHandler),   
], debug=True)