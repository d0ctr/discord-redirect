from flask import Flask, redirect, render_template
from .utils import check_link_arg

app = Flask(__name__)

@app.route('/b/<path:link>')
@check_link_arg(name='link')
def browser_redirect(link):
    return redirect(f'https://discord.com/{link}')

@app.route('/a/<path:link>')
@check_link_arg(name='link')
def app_redirect(link):
    return redirect(f'discord://discord.com/{link}')

@app.route('/<path:link>')
@check_link_arg(name='link')
def index(link):
    return render_template('index.html', link=link)