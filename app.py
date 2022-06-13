from socketApp import socketio , app
if __name__ == '__main__':
    socketio.run(app ,debug=True,port=2400)