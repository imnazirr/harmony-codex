# blog/__init__.py

from flask import Blueprint

blog_bp = Blueprint('blog_bp', __name__)

from blog import routes
