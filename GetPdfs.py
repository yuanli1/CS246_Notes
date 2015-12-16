from bs4 import BeautifulSoup
from subprocess import call

def getUrl(loc):
    http = loc.split("http")
    if len(http) > 1:
        return loc
    else:
        return "http://web.stanford.edu/class/cs246/" + loc

f = open("./handouts.html","r")
file_text = f.read()
bs_text = BeautifulSoup(file_text,'html.parser')
f.close()
pdf_uls = bs_text.findAll('ul')
count = 0
for ul in pdf_uls:
    lis = ul.find_all("li")
    for li in lis:
        links = li.find_all("a")
        for a in links:
            url = getUrl(a["href"])
            call(["wget",url,"-P","./"+str(count)])
    count = count + 1

