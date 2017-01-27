import webapp2
import caesar






class MainRequestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(caesar.encrypt("Hello, World!", 13))









routes = [('/', MainRequestHandler)]
app = webapp2.WSGIApplication(routes, debug=True)
