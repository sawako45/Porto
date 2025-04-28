from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/download-cv')
def download_cv():
    return send_from_directory('static/cv', 'mycv.pdf', as_attachment=False)

@app.route('/Education')
def Education():
    return render_template('education.html')

@app.route('/AboutMe')
def utama():
    return render_template('home.html')

@app.route('/Contact')
def Contact():
    return render_template('contact.html')

@app.route('/Project')
def Project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
