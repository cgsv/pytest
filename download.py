import re, urllib2, BeautifulSoup

def getFileLink(fmt, url):
    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(data)
    tags = soup.findAll(attrs={'href':re.compile('.*\.'+fmt)})
    links = map(lambda x:x['href'], tags)
    return links

def traverse(url, depth, action):
    if depth == 0: return
    try:
        data = urllib2.urlopen(url).read()
        soup = BeautifulSoup.BeautifulSoup(data)
        tags = soup.findAll(attrs={'href':re.compile('.*')})
        links = map(lambda x:x['href'], tags)
        action(links)
    except:
        return
    for link in links:
        newurl = urllib2.urlparse.urljoin(url, link)
        traverse(newurl, depth-1, action)

def getFname(url):
    pos = url.rfind('/')
    if pos < 0: return url
    return url[pos+1:]

def downloadFile(url):
    data = urllib2.urlopen(url).read()
    fp = open(getFname(url), 'wb')
    fp.write(data)
    fp.close()

def myprint(url):
    print url

if __name__ == '__main__':
    traverse('http://www.baidu.com', 2, myprint)
