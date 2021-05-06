from flask import Flask

#dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
import numpy as np
import datetime as dt

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'