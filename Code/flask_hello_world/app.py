from flask import Flask, render_template, request

# Create instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL

@app.route('/')
def hello_world():
    # Get the 'color', 'hostname', and 'network' parameters from the URL query string
    # If any parameter is not provided, set a default value
    background_color = os.getenv('color', 'red')
    hostname = os.getenv('hostname', 'localhost')
    network = os.getenv('network', 'LAN')
    
    return render_template('index.html', 
                           background_color=background_color, 
                           hostname=hostname, 
                           network=network)

@app.route('/user')
def hello_user():
    return "Hello User"
# Run the app when script is executed directly

if __name__ == '__main__':
    app.run(debug=True)