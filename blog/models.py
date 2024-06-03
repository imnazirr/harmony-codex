# blog/models.py

class Blog:
    def __init__(self, id, title, content, date):
        self.id = id
        self.title = title
        self.content = content
        self.date = date

# Mock data
blogs = [
    Blog(1, 'First Blog', 'Content of the first blog', '2024-01-01'),
    Blog(2, 'Second Blog', 'Content of the second blog', '2024-02-01')
]
