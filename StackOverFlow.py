from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

data = []

def stackoverflow(x):
    url = f'https://stackoverflow.com/questions/tagged/{word}?page={x}&pagesize=50'
    baseurl = 'https://stackoverflow.com'
    r = session.get(url)
    content_tags = r.html.find('div.mln24')
    for item in content_tags:
        try:
            title = item.find('div.summary h3', first=True).text
        except:
            title = ''
        try:
            url = baseurl + item.find('div.summary h3 a', first=True).attrs['href']
        except:
            url = ''
        try:
            tags = item.find('div.flex--item', first=True).text
        except:
            tags = ''
        try:
            posted = item.find('div.user-action-time', first=True).text
        except:
            posted = ''
        try:
            vote = item.find('div.vote-count-post', first=True).text
        except:
            vote = '0'
        try:
            answer = item.find('div.status.answered', first=True).text.replace('answer', '')
        except:
            answer = '0'
        try:
            views = item.find('div.views', first=True).text.replace('views', '')
        except:
            views = '0'
        
        dic = {
            'Title' : title,
            'Tags' : tags,
            'Posted' : posted,
            'Answered' : answer,
            'Votes' : vote,
            'Views' : views,
            'Urls' : url
        }
        
        data.append(dic)
    return

word = input('Enter keyword here: ')
for x in range(0, 11):
    stackoverflow(x)

df = pd.DataFrame(data)
df.to_csv(f'{word}' + '.csv', index=False)
print('Finished')
