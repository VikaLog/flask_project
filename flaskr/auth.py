import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/names/', methods=('GET'))
def names():
    db = get_db()
    names_artists = db.execute(
        'SELECT count(distinct artist) FROM tracks'
    )
    return names_artists


@bp.route('/tracks/', methods=('GET'))
def tracks():
    db = get_db()
    tracks_count = db.execute(
        'SELECT count(*) FROM tracks'
    )
    return tracks_count


@bp.route('/tracks/<genre>', methods=('GET'))
def genre():
    db = get_db()
    genre_count = db.execute(
        'SELECT count(*) FROM tracks as t inner join genres as g on t.genre_id = g.id where g.title = <genre>'
    )
    return genre_count


@bp.route('/tracks-sec/', methods=('GET'))
def tracks_sec():
    db = get_db()
    track_sec = db.execute(
        'SELECT title, "lenght" FROM tracks'
    )
    return track_sec


@bp.route('/tracks-sec/statistics/', methods=('GET'))
def tracks_sec_stat():
    db = get_db()
    track_sec_st = db.execute(
        'SELECT avg("lenght"), sum("lenght") FROM tracks'
    )
    return track_sec_st
