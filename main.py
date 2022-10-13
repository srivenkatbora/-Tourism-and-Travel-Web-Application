from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

app= Flask(__name__)
app.secret_key='somethingyouuknow'


@app.route('/')
def index():
   return render_template("index.html")

@app.route('/about')
def about():
   return render_template("About.html")
@app.route('/welcome')
def aftlogin():
   return render_template("aftlogin.html")
@app.route('/alleppey')
def allp():
   return render_template("alleppey.html")

@app.route('/blog')
def blog():
   return render_template("blog.html")

@app.route('/colva')
def colva():
   return render_template("colva.html")

@app.route('/contact')
def contact():
   return render_template("contact.html")

@app.route('/gold')
def dold():
   return render_template("GoldenTemple-info.html")

@app.route('/gwalior')
def gwalior():
   return render_template("gwalior.html")
@app.route('/hampi')
def hampi():
   return render_template("hampi.html")
@app.route('/home')
def home():
   return render_template("home.html")





@app.route('/login', methods=['POST','GET'])
def login():
   if request.method == 'POST':
      username=request.form.get('username')
      password=request.form.get('password')
      return render_template("aftlogin.html")

        
   return render_template("login.html")
@app.route('/mehrangarh')
def megv():
   return render_template("mehrangarh.html")
@app.route('/mon')
def mon():
   return render_template("mon.html")
@app.route('/recents')
def recents():
   return render_template("Recents-Announcement.html")
@app.route('/signup')
def signup():
   if request.method =='POST':
      
      return render_template(login.html)

   return render_template("SignUp.html")
@app.route('/sanchi')
def sanchi():
   return render_template("sanchi.html")
@app.route('/taj')
def taj():
   return render_template("taj.html")
@app.route('/thankyou')
def thankyou():
   return render_template("thankyou.html")
@app.route('/umgot')
def umgot():
   return render_template("umgot.html")
@app.route('/vivekananda')
def vivk():
   return render_template("vivekanada.html")
@app.route('/twang')
def twang():
   return render_template("twamg.html")


if __name__ == '__main__':
   app.run(debug=False)