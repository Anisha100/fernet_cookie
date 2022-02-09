from flask import *
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
app = Flask(_name_)

@app.route('/login', methods=["GET","POST"])
def login():
	name=request.form['name'].strip()
	uname=request.form['uname'].strip()
	eml=request.form['eml'].strip()

	
	k=name+'$'+request.remote_addr+'$'+uname+'$'+eml
	res=f.encrypt(k.encode()).decode()
	resp = make_response(redirect('/dashboard'))
	resp.set_cookie('username', res, max_age=3600)
	return resp 
@app.route('/dashboard')
def dashboard():
	username=request.cookies.get('username')
	k=f.decrypt(id.encode()).decode()
	arr=k.split('$')
	name=arr[0]
	ip=arr[1]
	uname=arr[2]
	eml=arr[3]

	if ip==request.remote_addr:
	return render_template('dashboard.html',name=name,uname=uname,eml=eml)
	else:
	return render_template('error.html',ip=ip,ip1=request.remote_addr)
app.run()
