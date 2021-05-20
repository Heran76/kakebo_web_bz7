from Kakebo import app

@app.route('/')
def index():
    return 'Flask rulando'