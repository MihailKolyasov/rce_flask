from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = ""
    file_content = ""
    if request.method == 'POST':
        filename = request.form['filename']
        
        with open(filename, 'r') as f:
            file_content = f.read()
        
        
    return render_template('index.html', filename=filename, file_content=file_content)
	
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
