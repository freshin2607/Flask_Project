
  
from flask import render_template, request, Blueprint
from Exam.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/examination")
def exanimation():
    return render_template('examination.html', title='Examination')

@main.route("/importantdates")
def importantdates():
    return render_template('importantdates.html', title='Important Dates')

@main.route("/contactus")
def contactus():
    return render_template('contactus.html', title='Contact Us')