import webapp2
import caesar


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>web caesar</title>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""



class MainRequestHandler(webapp2.RequestHandler):
    def get(self):
        page = ''
        sentence_1 = "<p>Enter the text you'd like to encrypt:</p>"
        rotation = "<br><input type='number' name='rotation-number' min='1' max='200'/>"
        text_area = "<textarea name='text' style='height:100px;width:400px;'></textarea>"
        submit =  "<br><input type='submit' value='Encrypt'/>"
        form = "<form method='post'>" + rotation + text_area + submit + "</form>"
        page = page_header + sentence_1 + "<br>" + form + page_footer
        self.response.write(page)










routes = [('/', MainRequestHandler)]
app = webapp2.WSGIApplication(routes, debug=True)
