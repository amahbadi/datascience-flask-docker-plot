#--------ALI AKBAR MAHBADI :aamahbadi@yahoo.com----------
import csv, os
from flask import Flask, render_template

app = Flask(__name__,
            static_url_path=''
            )


from app import views