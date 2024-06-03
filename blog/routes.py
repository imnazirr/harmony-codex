# blog/routes.py

from flask import render_template, request, redirect, url_for
from blog import blog_bp
from blog.models import blogs as blog_list, Blog

@blog_bp.route('/')
def blogs():
    return render_template('blogs.html', blogs=blog_list)

@blog_bp.route('/<int:blog_id>')
def blog_post(blog_id):
    blog = next((b for b in blog_list if b.id == blog_id), None)
    if blog is None:
        return redirect(url_for('blog_bp.blogs'))
    return render_template('blog_post.html', blog=blog)

@blog_bp.route('/create', methods=['GET', 'POST'])
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']
        new_blog = Blog(len(blog_list) + 1, title, content, date)
        blog_list.append(new_blog)
        return redirect(url_for('blog_bp.blogs'))
    return render_template('create_blog.html')
