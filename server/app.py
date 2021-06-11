from flask import Flask, request, jsonify, make_response
import os
import sys
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app, resources=)