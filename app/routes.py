from flask import render_template, request, redirect, url_for
from . import db
from .models import User, Post

# reittejä ja niiden käsittelijöitä
