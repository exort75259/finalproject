from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Ответ с кодом 200 OK
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello Exort")
        else:
            # Вызов обработчика родительского класса для любого пути, кроме '/'
            super().do_GET()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Запуск сервера на порту {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
