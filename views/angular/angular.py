from flask import url_for, render_template, redirect, session, request, Blueprint
from flask_login import login_required

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='../../static')


@admin.route('/', methods=['GET'])
@login_required
def admin_page():
    """
    View for Admin Page
    @return:
    """
    return render_template("/admin_page.html")
