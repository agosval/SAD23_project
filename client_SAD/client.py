#Project Flask MVC


from project import app
import webview
import threading
import sys

def start_server():
    app.run(host='0.0.0.0', port=8888)

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("Client", "http://localhost:8888", width=1920, height=1080)
    webview.start()
    sys.exit()

    app.run(host="localhost", port=8888, debug=True)
