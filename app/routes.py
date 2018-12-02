from app import app

# these are decorators, modifying the following function. 
# associating the url / with the function
@app.route('/')
# associating the url /index with the function
@app.route('/index')

def index():
    return "Hello, World!"