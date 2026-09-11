class Hotstar:
    def __init__(self,name):
        print(f'welcome to the Hotstar, {name}--------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play start pause")
    def ads(self):
        print("You can see ads")
    def quality(self):
        print("You can see low quality")
    def devices(self):
        print("Single devices")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can download")
class PremiumHotstar(Hotstar):
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play start pause")
    def ads(self):
        print("You can see ads")
    def quality(self):
        print("You can see low quality")
    def devices(self):
        print("Multiple devices")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can download")

shashi = Hotstar("shashi")
shashi.auth()
shashi.dashboard()
shashi.search()
shashi.history()
shashi.playcontrollers()
shashi.ads()
shashi.quality()
shashi.devices()
shashi.access()
shashi.download()

vardhan = PremiumHotstar("vardhan")
vardhan.auth()
vardhan.dashboard()
vardhan.search()
vardhan.history()
vardhan.playcontrollers()
vardhan.ads()
vardhan.quality()
vardhan.devices()
vardhan.access()
vardhan.download()
