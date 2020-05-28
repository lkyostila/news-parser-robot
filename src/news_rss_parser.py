import feedparser

keywords = ['kesä', 'loma', 'lomavinkit', "matkailu", "matka", "lomamatka"]
url_dict = {"yle": "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss",
            "kauppalehti": "https://feeds.kauppalehti.fi/rss/main",
            "hs": "https://www.hs.fi/rss/tuoreimmat.xml"}
used_news_headlines = []

def get_news():
    file = open("news.html","w", encoding="utf-8")
    file.write('<meta charset="UTF-8">\n')
    file.write('<style>'
               'body {background-color: black; font-family: monospace; color: yellow;}'
               'h2 {color: #03fc30;}'
               'a:link {color: white;}'
               'a:visited {color: #f403fc}'
               '</style>')

    file.write('<h2>Viimeisimmät uutiset</h2>\n\n')
    if len(keywords) > 0:
        file.write('<h3>Avainsanoilla: ')
        kwstring = ""
        for keyword in keywords:
            kwstring += keyword + ", "
        kwstring = kwstring[0:len(kwstring)-2]
        file.write(kwstring + "</h3>\n\n")
    else:
        file.write("\n")
    for entry in url_dict:
        parse_news_by_keywords(file,entry,url_dict[entry])
    file.close()

def parse_news_by_keywords(file,newssite_name,url):
    parsed_data = feedparser.parse(url)
    file.write("<h2>%s</h2>\n\n\n" % newssite_name.upper())
    for news_entry in parsed_data.entries:
        time = news_entry.published[5:22]
        if len(keywords) > 0:
            for keyword in keywords:
                if(keyword in news_entry.title and news_entry.title not in used_news_headlines):
                    used_news_headlines.append(news_entry.title)
                    file.write('<a href="%s" ><p>(%s) | %s</p></a>\n\n'
                               % (news_entry.link,time,news_entry.title))
        else:
            file.write('<a href="%s" ><p>(%s) | %s</p></a>\n\n'
                       % (news_entry.link, time, news_entry.title))