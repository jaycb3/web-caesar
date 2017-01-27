import webapp2
import caesar
import cgi


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>web caesar</title>
</head>
<body>
<h2>Web Caesar</h2>
"""

page_footer = """
</body>
</html>
"""

def make_page(text_content):
        page = ''
        sentence_1 = "<p>Enter the text you'd like to encrypt:</p>"
        rotation = "<br><br><label>Enter rotation:<br><br><input type='number' name='rotation' min='1' max='200' style='width:80px;'/></label><br>"
        text_area = "<textarea name='text' style='height:100px;width:400px;'>" + text_content + "</textarea>"
        submit =  "<br><input type='submit' value='Encrypt'/>"
        form = "<form method='post'>" + text_area + rotation + submit + "</form>"
        page = page_header + sentence_1 + "<br>" + form + page_footer
        return page



class MainRequestHandler(webapp2.RequestHandler):
    def get(self):
        page = make_page("")
        self.response.write(page)

    def post(self):
        message = cgi.escape(caesar.encrypt(self.request.get('text'), int(self.request.get('rotation'))))
        page = make_page(message)
        self.response.write(page)









routes = [('/', MainRequestHandler)]
app = webapp2.WSGIApplication(routes, debug=True)
