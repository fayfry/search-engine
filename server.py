from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)  # Send response status code
        self.send_header('Content-type', 'text/html')  # Send headers
        self.end_headers()
        message = "kinda server is kinda running!"  # Send message back to client
        html = bytes("""
                        <html>
                        <body>
                        <form action = "" method = "post">
                        <input type = \"text\" name = \"inquery\">
                        <input type = \"submit\" name = \"button\">
                        </form> </body> </html>""", encoding="utf-8")

        self.wfile.write(html)
        return


def run():
    print('starting server')

    # Server settings
    # 8080 or 8081. for port 80, which is normally used for a http server, you need root access
    # 127.0.0.1 is a local host
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server')
    httpd.serve_forever()

run()