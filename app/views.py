from app import app
from flask import render_template, redirect, flash, session
import sys
import sqlite3 as lite
import os
from flask import request

import string
import random

def id_gen(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/url', methods=['POST'])
def url():
	url = request.form['url']
	if url == '':
		return redirect('/index')
	
	orig = []
	shorten = []

	
	tmp = id_gen()

	shorten.append('http://127.0.0.1:5000/'+tmp)
	orig.append(url)
	
	con = lite.connect('url.db')
	
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO url(link, short) VALUES (?,?)',[url,tmp])
	return render_template('index.html',orig=orig,shorten=shorten) 

#	return ('<h3><b><i>Shortend Url >> http://127.0.0.1:5000/%s</i></b></h3>' % (tmp))
	
@app.route('/<path:path>')
def redirection(path):
	print path
	
	con = lite.connect('url.db')
	with con:
		cur = con.cursor()
		cur.execute("SELECT link FROM url WHERE short=:name", {"name" : path})
		rows = cur.fetchall()
		if rows:
			for row in rows:
				return redirect(row[0])
