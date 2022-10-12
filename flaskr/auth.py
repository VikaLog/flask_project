import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/names/', methods=('GET', 'POST'))
def names():
    db = get_db()
    names_artists = db.execute(
        'SELECT count(distinct artist) FROM tracks'
    ).fetchall()
    return render_template("base.html", data=names_artists)


@bp.route('/tracks/', methods=('GET', 'POST'))
def tracks():
    db = get_db()
    tracks_count = db.execute(
        'SELECT count(*) FROM tracks'
    ).fetchall()
    return render_template("base.html", data=tracks_count)


@bp.route('/tracks/<genre>', methods=('GET', 'POST'))
def genre(genre):
    db = get_db()
    genre_count = db.execute(
        'SELECT count(*) as tracks FROM tracks as t inner join genres as g on t.genre_id = g.id where g.title = ?',
        (genre,)
    ).fetchall()
    return render_template("base.html", data=genre_count)


@bp.route('/tracks-sec/', methods=('GET', 'POST'))
def tracks_sec():
    db = get_db()
    track_sec = db.execute(
        'SELECT title, lengthen FROM tracks'
    ).fetchall()
    return render_template("base.html", data=track_sec)


@bp.route('/tracks-sec/statistics/', methods=('GET', 'POST'))
def tracks_sec_stat():
    db = get_db()
    track_sec_st = db.execute(
        'SELECT avg(lengthen), sum(lengthen) FROM tracks'
    ).fetchall()
    return render_template("base.html", data=track_sec_st)
