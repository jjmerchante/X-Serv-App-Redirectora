import webapp
import random
import sys


class aleat(webapp.webApp):

    def process(self, parsedRequest):
        randNumber = random.randint(1, 1000000)
        return ('302 Found', "Location: http://localhost:1234/"+str(randNumber)+"\r\n",
                           "<html><body><p>Hola." +
                           "<a href=" + str(randNumber) + ">Redirige</a></p>" +
                           "</body></html>")
if __name__ == "__main__":
    try:
        testWebApp = aleat("localhost", 1234)
    except KeyboardInterrupt:
        print "Exit\n"
        sys.exit()
