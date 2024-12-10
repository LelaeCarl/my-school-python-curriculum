'''
app/admin/views.py
'''
from . import admin
from flask import render_template, flash, redirect, url_for, session, request
from app.admin.forms import LoginForm, TagForm
from app import db  # db variable in app.__init__.py
from app.models import Admin, Adminlog, Tag, Oplog

# 1. Login module functionality
@admin.route("/login/", methods=['GET', 'POST'])
def login():
    # 1.1 Get login form
    form = LoginForm()
    # 1.2 Check if the form is submitted (POST)
    if form.validate_on_submit():
        # 1.3 Get form data (account, pwd)
        data = form.data
        # 1.4 Query if the user exists based on account
        # name is the field in the Admin table in the database
        # data is form data in dictionary format, key is the LoginForm variable
        admin = Admin.query.filter_by(name=data['account']).first()
        # 1.5 Check if account is found and if password matches
        if admin is None or not admin.check_pwd(data['pwd']):
            # 1.5.1 Send error message via Flask
            flash("Incorrect username or password", 'err')
            # 1.5.2 Redirect the request
            return redirect(url_for('admin.login'))
        # 1.6 If username and password match, save data to session
        session['admin'] = data['account']
        session['admin_id'] = admin.id

        # 1.7 Log admin login activity (admin id, login IP address, login time)
        adminlog = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr
        )
        # 1.8 Add admin login log to the database
        db.session.add(adminlog)
        db.session.commit()

        # 1.9 Redirect to the homepage
        return redirect(url_for('admin.index'))

    return render_template("admin/login.html", form=form)

# 2. Backend management system homepage
@admin.route("/")
def index():
    return render_template("admin/index.html")

# 3. Tag management - Add tag
@admin.route("/tag_add/", methods=['GET', 'POST'])
def tag_add():
    # 3.1 Get Tag form
    form = TagForm()
    # 3.2 Check if the submit button was clicked
    if form.validate_on_submit():
        # 3.3 Get form data
        data = form.data
        # 3.4 Check if the tag already exists in the database
        tag = Tag.query.filter_by(name=data['name']).count()
        # 3.5 If the tag exists, show an error message
        if tag == 1:
            flash("Movie tag already exists, cannot duplicate!", 'err')
            return redirect(url_for("admin.tag_add"))
        # 3.6 Create new tag object (set model instance)
        tag = Tag(name=data['name'])
        # 3.7 Add the tag to the session
        db.session.add(tag)
        db.session.commit()
        # 3.8 Log admin operation (adding a tag)
        oplog = Oplog(
            admin_id=session['admin_id'],
            ip=request.remote_addr,
            reason=f'Added tag {data["name"]}'
        )
        # 3.9 Add the operation log to the database
        db.session.add(oplog)
        db.session.commit()
        # 3.10 Show success message and redirect
        flash("Tag added successfully", "ok")
        return redirect(url_for("admin.tag_add"))
    return render_template("admin/tag_add.html", form=form)

# 4. Tag management - Tag list
@admin.route("/tag_list/<int:page>/", methods=['GET'])
def tag_list(page=None):
    # 4.1 If no page parameter, set default page to 1
    if page is None:
        page = 1
    # 4.2 If page exists, fetch tags for that page (pagination)
    page_data = Tag.query.order_by(Tag.addtime).paginate(page=page, per_page=5)
    # 4.3 Return the page with tag data
    return render_template("admin/tag_list.html", page_data=page_data)

# 5. Tag management - Edit tag
@admin.route("/tag_edit/<int:id>", methods=['GET', 'POST'])
def tag_edit(id=None):
    # 5.1 Get the form for editing
    form = TagForm()
    # 5.2 Get tag object by id
    tag = Tag.query.get_or_404(id)
    # 5.3 Change the form submit button text to "Modify"
    form.submit.label.text = "Modify"
    # 5.4 Check if the modify button was clicked
    if form.validate_on_submit():
        # 5.5 Get form data
        data = form.data
        # 5.6 Check if the modified tag name already exists
        tag_count = Tag.query.filter_by(name=data['name']).count()
        # 5.7 If the name is different but the tag already exists
        if tag.name != data['name'] and tag_count == 1:
            flash("Tag already exists!", 'err')
            return redirect(url_for("admin.tag_edit", id=tag.id))
        # 5.8 Modify the tag's name
        tag.name = data['name']
        # 5.9 Commit the changes to the database
        db.session.add(tag)
        db.session.commit()
        # 5.10 Show success message
        flash("Tag has been successfully modified!", 'ok')
        # 5.11 Redirect back to the edit page
        return redirect(url_for("admin.tag_edit", id=tag.id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)

# 6. Tag management - Delete tag
@admin.route("/tag_del/<int:id>", methods=['GET'])
def tag_del(id=None):
    # 6.1 Query the tag by id
    tag = Tag.query.filter_by(id=id).first_or_404()
    # 6.2 Delete the tag from the database
    db.session.delete(tag)
    db.session.commit()
    # 6.3 Show success message
    flash(f"Tag <<<{tag.name}>>> deleted successfully", 'ok')
    # 6.4 Redirect to the tag list page
    return redirect(url_for('admin.tag_list', page=1))
