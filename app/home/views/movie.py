from app.home import home
from flask import render_template


@home.route("/play/<int:id>/", methods=["GET", "POST"])
def play(id=None):
    return ''


@home.route("/search/<int:page>/")
def search(page=None):
    return ''