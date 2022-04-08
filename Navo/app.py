from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import audiototext
import transcribe	

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "data/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        print(filename)
        
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        
        transcribe.videotoaudio(filename)
        audiototext.audiototext()
        
        file = open(app.config['UPLOAD_FOLDER'] + "Happy.txt","r")
        content = file.read()   
        
    return render_template('content.html', content=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)
