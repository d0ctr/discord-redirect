from flask import Flask, redirect, render_template, request, url_for
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

@app.route('/b')
@app.route('/a')
def redirect_by_param():
    link = request.get('link')
    if link is None:
        return redirect(url_for('index'))

    route = request.path[-1:0]
    if route == 'a':
        return redirect(url_for('app_redirect', link=link)
    elif route == 'b':
        return redirect(url_for('browser_redirect', link=link)

@app.route('/<path:link>')
@check_link_arg(name='link')
def redirect_index(link):
    return render_template('index.html', link=link)

@app.route('/')
def index():
    link = request.args.get('link')
    if link is None:
        return redirect('https://github.com/d0ctr/discord-redirect')

    return redirect(url_for('redirect_index', link=link))
