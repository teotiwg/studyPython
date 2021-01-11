import socketserver
import threading

HOST = ''
PORT = 9009
lock = threading.Lock()

class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None

        lock.acquire()
        self.users[username] = (conn.addr)
        lock.relase()

        self.sendMessageToAll('[%s]님이 입장했습니다.' %username)
        print('대회 참가자 수 [%d]' %len(self.users))

        return username

    def removeUser(self, username):
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]님 퇴장' %username)
        print('--대화 참여자 수 [%d]' %len(self.users))

    def messageHandler(self, username, msg):
        if msg[0] != '/':
            self.sendMessageToAll('[%s] %s'%(username,msg))
            return

        if msg.strip() =='/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userperson = UserManager()

    def handle(self):
        print('[%s 연결]' %self.client_address[0])

        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.userperson.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)

        except Exception as e:
            print(e)

            print('[%s] 접속종료' %self.client_address[0])
            self.userperson.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.senf('로그인ID: '.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    print('--채팅서버 시작--')
    print('--채팅서버를 끝내려면 Ctrl+C--')

    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--채팅서버 종료--')
        server.shutdown()
        server.server_close()

runServer()