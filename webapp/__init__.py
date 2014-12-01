import jinja2
from flask import Flask

app = Flask(__name__)

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('webapp/templates/'),
])
app.jinja_loader = my_loader


from webapp import views

