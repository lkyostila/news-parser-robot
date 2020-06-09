import feedparser
import textwrap

def define_keywords():
    x = input()
    splitted = x.split()
    return splitted

keywords = define_keywords()
url_dict = {"Yle": "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss",
            "Kauppalehti": "https://feeds.kauppalehti.fi/rss/main",
            "Helsingin Sanomat": "https://www.hs.fi/rss/tuoreimmat.xml",
            "Iltasanomat": "https://www.is.fi/rss/tuoreimmat.xml",
            "Iltalehti": "https://www.iltalehti.fi/rss/uutiset.xml"}
used_news_headlines = []

def get_news():
    file = open("news.html","w", encoding="utf-8")
    file.write('<html>'
               '<head>'
               '<meta charset="UTF-8">\n'
               '<title>arvinews</title>\n'
               '</head>')
    file.write('<style>'
               'body {background-color: black; font-family: monospace; color: yellow;}'
               'h2 {color: #03fc30;}'
               'a:link {color: white;}'
               'a:visited {color: #f403fc}'
               'table {border-collapse: collapse}'
               'th,td,table {border: 1px solid cyan}'
               '</style>')
    file.write('<body>\n'
               '<h2>Viimeisimmät uutiset\n\n</h2>')
    if len(keywords) > 0:
        file.write('<h3>Avainsanoilla: ')
        kwstring = ""
        for keyword in keywords:
            kwstring += keyword + ", "
        kwstring = kwstring[0:len(kwstring)-2]
        file.write(kwstring + "</h3>\n\n")
    else:
        file.write("<h3>Kaikki tuoreimmat</h3>\n")
    file.write('<img id="arvi" src='
               '"https://im.mtv.fi/image/95990/landscape16_9/360/203/dcf0576453610282a3879e97ca1ed41d/Ip/991376.jpg"'
               '></img>\n')
    for entry in url_dict:
        parse_news_by_keywords(file,entry,url_dict[entry])
    file.write('\n'
               '<div id="player"></div>\n')
    file.write("<script>"
                  "var tag = document.createElement('script');"
                  "tag.src = \"https://www.youtube.com/iframe_api\";"
                  "var firstScriptTag = document.getElementsByTagName('script')[0];"
                  "firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);"
                  "var player;"
                  "function onYouTubeIframeAPIReady() {"
                    "player = new YT.Player('player', {"
                        "height: '390',"
                        "width: '640',"
                        "videoId: 'VBlFHuCzPgY',"
                    "events: {"
                        "'onReady': onPlayerReady,"
                    "}"
                    "});"
                  "}"
                  "function onPlayerReady(event) {"
                    "event.target.playVideo();"
                    "player.setVolume(20);"
                  "}"
                "</script>"
               "</body>"
               "</html>")
    file.close()
    if len(keywords) > 0:
        headlines = "Hei. Minä olen Arvi Lind ja tervetuloa päivän uutisiin. Tässä uutiset aiheista "
        for keyword in keywords:
            headlines += keyword + ", "
        headlines += ". "
        for headline in used_news_headlines:
            headlines += headline + ". "
        textwrap.shorten(headlines,width=5000)
        return headlines
    else:
        headlines = "Hei. Minä olen Arvi Lind ja tervetuloa päivän uutisiin. Tässä tuoreimmat uutiset. "
        for keyword in keywords:
            headlines += keyword + ", "
        headlines += ". "
        for headline in used_news_headlines:
            headlines += headline + ". "
        textwrap.shorten(headlines,width=5000)
        return headlines

def parse_news_by_keywords(file,newssite_name,url):
    parsed_data = feedparser.parse(url)
    file.write("<h2>%s</h2>\n\n\n" % newssite_name.upper())
    if len(keywords) > 0:
        for news_entry in parsed_data.entries:
            time = news_entry.published[:22]
            for keyword in keywords:
                if len(keyword) > 6:
                    a = len(keyword)
                    b = a - a * 0.1
                    b = int(b)
                    keyword = keyword[0:b]
                if(keyword in news_entry.title and news_entry.title not in used_news_headlines):
                    file.write('<a href="%s" target="_blank" ><p>(%s) | %s</p></a>\n\n'
                               % (news_entry.link, time, news_entry.title))
                    used_news_headlines.append(news_entry.title)
    else:
        for i in range (0,8):
            news_entry = parsed_data.entries[i]
            time = news_entry.published[:22]
            used_news_headlines.append(news_entry.title)
            file.write('<a href="%s" target="_blank" ><p>(%s) | %s</p></a>\n\n'
                       % (news_entry.link, time, news_entry.title))
