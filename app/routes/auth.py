from flask import Blueprint,render_template,redirect,url_for,flash 
from app.forms.AuthForm import RegisterForm,LoginForm 
from app.services.auth_service import register_user,authenticate_user,logout_current_user
from flask_login import login_required 



auth_bp = Blueprint('auth',__name__,template_folder='templates')

@auth_bp.routes('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user,error = register_user(form.email.data,form.password.data)
        if error:
            flash(error,'danger')
            return redirect(url_for('auth.register'))
        
        flash('Account created successfully. Please Log in.','success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html',form=form)



@auth_bp.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if authenticate_user(form.email.data,form.password.data):
            flash('Login Successful !','success')
            return redirect(url_for('auth.dashboard'))
        
        flash('Invalid email or password','danger')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html',form=form)

@auth_bp.route('/dashboard')
@login_required 
def dashboard():
    return "Welcome! You are logged in !"

@auth_bp.route('/logout')
def logout():
    logout_current_user()
    flash("You have been logged out",'info')
    return redirect(url_for('auth.login'))