from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:50]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
            'author': response_dict['by'],
        }
    except KeyError:
        print(f"Missing data, ID: {submission_id}</ br/>{r.status_code}")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

labels, repo_links = [], []

for submission_dict in submission_dicts:
    label = f"{submission_dict['title']}<br />{submission_dict['author']}"
    labels.append(label)
    repo_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    repo_links.append(repo_link)

comment_number = [submission_dict['comments'] for submission_dict in submission_dicts]
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': comment_number,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most commented articles on Hacker-News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_comments.html')
