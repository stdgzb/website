import wsgiref.handlers
from google.appengine.ext import webapp

class MyHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hello")

def main():
    app = webapp.WSGIApplication([(r'.*', MyHandler)], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()

