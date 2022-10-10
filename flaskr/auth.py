import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/names/', methods=('GET', 'POST'))
def names():
    db = get_db()
    db.execute(
        'SELECT count(distinct artist) FROM tracks'
    )



@bp.route('/tracks/', methods=('GET', 'POST'))
def tracks():
    db = get_db()
    tracks_count = db.execute(
        'SELECT count(*) FROM tracks'
    )



@bp.route('/tracks/<genre>', methods=('GET', 'POST'))
def genre():
    db = get_db()
    genre_count = db.execute(
        'SELECT count(*) FROM tracks as t inner join genres as g on t.genre_id = g.id where g.title = <genre>'
    )


@bp.route('/tracks-sec/', methods=('GET', 'POST'))
def tracks_sec():
    db = get_db()
    track_sec = db.execute(
        'SELECT title, "lenght" FROM tracks'
    )


@bp.route('/tracks-sec/statistics/', methods=('GET', 'POST'))
def tracks_sec_stat():
    db = get_db()
    track_sec = db.execute(
        'SELECT avg("lenght"), sum("lenght") FROM tracks'
    )