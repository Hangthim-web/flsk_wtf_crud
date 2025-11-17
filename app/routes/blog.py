from flask import Blueprint,render_template,redirect,request,url_for,flash
from app.models.Blog import Blog 
from app import db 
from flask_login import login_required
from app.services.blog_services import create_blog,update_blog,get_all_blogs,get_blog_by_id,delete_blog
from app.forms.BlogForm import BlogForm

blog_bp = Blueprint('blog',__name__,template_folder='templates')

@blog_bp.route('/create-blog',methods=['GET','POST'])
@login_required
def create():
    form = BlogForm()
    # if request.method == "POST":
    #     create_blog(
    #         request.form.get('title'),
    #         request.form.get('description')
    #     )
    if form.validate_on_submit():
        create_blog(
            form.title.data, 
            form.description.data
        )
        flash("Blog created successfully",'success')
        return redirect(url_for('blog.list_all_blogs__'))
    return render_template('blog/create.html',form=form)

@blog_bp.route('/blogs')
@login_required
def list_all_blogs__():
    blog_list = get_all_blogs()
    return render_template('blog/list.html',blogs=blog_list)
