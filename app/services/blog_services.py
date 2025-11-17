from app.models.Blog import Blog 
from app.extensions import db 

def create_blog(title,description):
    blog = Blog(title = title,description = description)
    db.session.add(blog)
    db.session.commit()
    return blog 


def get_blog_by_id(id):
    blog = Blog.query.get_or_404(id)
    return blog     

def get_all_blogs():
    blogs = Blog.query.all()
    return blogs 


def update_blog(id,title,description):
    blog = get_blog_by_id(id)
    blog.title = title 
    blog.description = description
    db.session.commit()
    return blog 


def delete_blog(id):
    blog = get_blog_by_id(id)
    db.session.delete(blog)
    db.session.commit()
    return True 

