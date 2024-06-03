from flask import Flask, render_template, redirect, url_for
from blog.routes import blog_bp

app = Flask(__name__)

# Register the blog blueprint
app.register_blueprint(blog_bp, url_prefix='/blogs')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
