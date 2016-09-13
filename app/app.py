import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)
