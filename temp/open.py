import webbrowser 

def setup():
    global amazon, twitter, qhss, reddit, vimeo
    amazon = "amazon.com"
    twitter = "twitter.com"
    qhss = "qhss.org"
    reddit = "reddit.com"
    vimeo = "vimeo.com"
    
def start():
    webbrowser.open(amazon, new=0, autoraise=True)
    webbrowser.open(twitter, new=0, autoraise=True)
    webbrowser.open(qhss, new=0, autoraise=True)
    webbrowser.open(reddit, new=0, autoraise=True)
    webbrowser.open(vimeo, new=0, autoraise=True)
    
setup()
start()