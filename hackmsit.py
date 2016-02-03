from flask import Flask, render_template, request,session,redirect,url_for
from flask.ext.socketio import SocketIO,emit,join_room,leave_room
import cgi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#dic = {'c':''}

@app.route('/',methods=['GET','POST'])
def index():
	#webbrowser.open_new(url)
	if request.method=='POST':
		session['name'] = request.form['name']
		session['room'] = request.form['room']
		return redirect(url_for('py'))
	return render_template('index.html')



@app.route('/py')
def py():
	name = session.get('name','')
	room = session.get('room','')
	return render_template('out.html', name=name, room=room)


@socketio.on('connect')
def ws_connect():
    
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
	    
    socketio.emit('msg',{'count':'0'},namespace='/chat',broadcast=True)


def check(link):
		if link[0:4] == 'http':
			return '<a  target="_blank" href='+link+'>'+cgi.escape(link)+'</a>'
		elif link[0:3] == 'www' :
			return '<a target="_blank "href=https://'+link[4:] +'>'+cgi.escape(link)+'</a>'
		else:
			return link

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    print "joined"
    emit('status', {'msg': session.get('name') + ' has entered the room.','name':session.get('name')}, room=room,namespace='/chat')

@socketio.on('disp', namespace='/chat')
def ws_city(message):
	print message['disp']
	print "jouned new"
	fina  = check(cgi.escape(message['disp']))
	room = session.get('room')
	print room
	emit('disp', {'nam': session.get('name')+': ','disp' :fina},room = room,namespace='/chat')
@socketio.on("type",namespace='/chat')
def auto_print(message):
	room = session.get('room')
	
	emit("atype",{'name':session.get('name')+" is typing ....",'press':message['press']},room=room,namespace='/chat')



if __name__ == '__main__' :
	#port = int(os.environ.get('PORT', 5000))

	socketio.run(app,host='0.0.0.0',port=5000,debug=True)
	#app.run(debug=True)
