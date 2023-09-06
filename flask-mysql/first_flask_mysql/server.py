from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()
    return render_template("index.html", all_friends = all_friends)

@app.route('/create_friend', methods = ['POST'])
def create_friend():
    Friend.save(request.form)
    
    return redirect('/')

@app.route('/friend/id/<int:friend_id>')
def show_one(friend_id):
    friend = Friend.return_one(friend_id)
    return render_template('show_friend.html', friend = friend)

if __name__ == "__main__":
    app.run(debug=True)

