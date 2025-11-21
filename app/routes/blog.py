from flask import Blueprint,render_template,redirect,request,url_for,flash
from app.models.Blog import Blog 
from app import db 
from flask_login import login_required,current_user
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
            form.description.data,
            user_id = current_user.id

        )
        flash("Blog created successfully",'success')
        return redirect(url_for('blog.list_all_blogs__'))
    return render_template('blog/create.html',form=form)

@blog_bp.route('/blogs')
@login_required
def list_all_blogs__():
    blog_list = get_all_blogs()
    return render_template('blog/list.html',blogs=blog_list)

@blog_bp.route('/edit-blog/<int:blog_id>',methods=['GET','POST'])
@login_required 
def edit_blog(blog_id):
    blog = get_blog_by_id(blog_id)
    if blog.user_id != current_user.id:
        flash('you are not allowed to edit this blog','danger')
        return redirect(url_for('blog.list_all_blogs__'))

    form = BlogForm(obj=blog)  #retain the original blog data.
    if form.validate_on_submit():
        update_blog(
                    blog.id,
                    form.title.data,
                    form.description.data
                    )
        flash('Blog updated successfully','success')
        return redirect(url_for('blog.list_all_blogs__'))
    return render_template('blog/edit.html',form=form)

@blog_bp.route('/delete-blog/<int:blog_id>',methods=['GET','POST'])
@login_required
def delete_blog_route(blog_id):
    blog = get_blog_by_id(blog_id)
    if blog.user_id != current_user.id:
        flash("You are not allowed to edit this blog.", "danger")
        return redirect(url_for('blog.list_all_blogs__'))
    delete_blog(blog_id)
    flash("Blog Deleted Successfully",'success')
    return redirect(url_for('blog.list_all_blogs__'))

