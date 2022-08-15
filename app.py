from flask import Flask, request
import git
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 

@app.route('/git_update', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./basic_flask')
        origin = repo.remotes.origin
        repo.create_head('master', 
    origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World and Friends'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()