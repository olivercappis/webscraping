from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as go
import ssl
from collections import Counter

context = ssl._create_unverified_context()

author_list = []
author_count = Counter()
quotes_list = []
tag_list = []
tag_count = Counter()



for page in range(10):
    url = f"https://quotes.toscrape.com/page/{page + 1}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(url, headers = headers)
    
    webpage = urlopen(req, context=context).read()

    soup = BeautifulSoup(webpage, 'html.parser')

    authors = soup.findAll('small')
    
    for x in authors: 
        author_list.append(x.text)

    

    quotes = soup.findAll('span', attrs={'class': 'text'})
    for quote in quotes:
        quotes_list.append(quote.text)


    tags = soup.findAll('a', attrs={'class': 'tag'})
    for tag in tags:
        tag_list.append(tag.text)




        


     
        





#author data output 
author_count.update(author_list)       
author_most = author_count.most_common(1)[0][0]
author_least = author_count.most_common()[:-2:-1][0][0]



print('Number of quotes by author')
print()
for author, count in author_count.items():
    print(f"Author: {author}")
    print(f'Number of Quotes: {count}')
    print()

print(f"The author with the most quotes is {author_most}")
print(f"The author with the least quotes is: {author_least}")




#quotes data output
total_words = sum(len(quote.split()) for quote in quotes_list)
average_words_per_quote = total_words / len(quotes)

print(f"The average number of words per quote is: {average_words_per_quote:.2f}")
print()


longest_quote_len = 0
shortest_quote_len = 100000
for quote in quotes_list:
    if len(quote) > longest_quote_len:
        longest_quote_len = len(quote)
        longest_quote = quote 

    if len(quote) < shortest_quote_len:
        shortest_quote_len = len(quote)
        shortest_quote = quote

print(f"The longest quote is: {longest_quote}")
print()
print(f"The shortest quote is: {shortest_quote}")
print()



tag_count.update(tag_list)
tag_most = tag_count.most_common(1)[0][0]
print('Tag data output')
print(f'The most popular tag is: {tag_most}')
print()
print(f'Total number of tags: {len(tag_list)}')




#create plotly
top_authors = author_count.most_common(10)
author_names = [author[0] for author in top_authors]
author_quotes_count = [author[1] for author in top_authors]

fig = go.Figure(data=[go.Bar(x=author_names, y=author_quotes_count)])
fig.update_layout(title='Top 10 Authors with the Highest Number of Quotes',
                  xaxis_title='Author',
                  yaxis_title='Number of Quotes')
fig.show()






top_tags = tag_count.most_common(10)
tag_names = [tag[0] for tag in top_tags]
tag_popularity = [tag[1] for tag in top_tags]

fig = go.Figure(data=[go.Bar(x=tag_names, y=tag_popularity)])
fig.update_layout(title='Top 10 Tags Based on Popularity',
                  xaxis_title='Tag',
                  yaxis_title='Popularity')
fig.show()