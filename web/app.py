from flask import Flask
from flask import render_template

app = Flask(__name__)

#Error handlers
@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403


@app.route("/<name>")
def hello(name):
    if (len(name) > 1):
        if ("//" not in name) and ("~" not in name) and (".." not in name):
            try:
                return open(name,"r").read()
            except IOError:
                  return error_404(404)
        else:
            return error_403(403)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
