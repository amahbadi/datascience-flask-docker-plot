#--------ALI AKBAR MAHBADI :aamahbadi@yahoo.com----------
from flask import Flask, render_template
import csv, os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO
import base64


app = Flask(__name__,
            static_url_path=''
            )


from app import views
