import os
from flask import Flask, render_template
import data_engine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           dayparts=data_engine.get_caf_dayparts())

#port = int(os.environ.get("PORT", 5004))
#app.run(port=port

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
