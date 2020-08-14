chrome = App(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
if not chrome.isRunning():
    print "closed - will open it"
    chrome.open(20)
 
if not chrome.isRunning():
    print "still closed- check again"
    exit()
print "running"
chrome.focus()
type("t",Key.CTRL)
type("l", Key.CTRL)
type("https://onecognizant.cognizant.com/")
type(Key.ENTER)
wait(10)
SCREEN = Screen(0)
r = SCREEN.getRect()
stringTobeFound = 'Mon,10Aug'
click(Region(759,109,293,36))
type("Trutime")
type(Key.ENTER)
wait(7)
click(Region(122,193,103,102))
wait(7)
type(Key.PAGE_DOWN)
wait(7)
r = Region(280,429,92,22)
cur = r.text()
r.highlight(5)
print('Before removing wspc : ' +cur)
removed_wspc = cur.replace(" ","")
print('After removing wspc : ' +removed_wspc)
if removed_wspc == stringTobeFound:
    click("1597150904587.png")
    wait(2)
    click(Region(438,473,287,31))
    type("Because of COVID-19 Outbreak")
    wait(2)
    click(Region(441,512,134,22))
    type("11")
    wait(2)
    click(Region(585,511,132,24))
    type("08")
    type(Key.TAB)
    type(Key.TAB)
    type("PM")
    wait(5)
else:
    print('No such Date was found in current screen!')