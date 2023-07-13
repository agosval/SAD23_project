#Project Flask MVC


from project import app
import webview
import threading
import sys

def start_server():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("Server", "http://localhost:8080")
    webview.start()
    sys.exit()
    #app.run(host="localhost", port=8080, debug=True)
    #webview.start()