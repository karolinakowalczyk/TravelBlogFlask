from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)
