#! python3

import requests, bs4
from collections import Counter, defaultdict

url = 'http://www.imsdb.com/scripts/Pulp-Fiction.html'

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

# Search script
script = soup.pre.text
dict = Counter(script.split())

# Convert to lower case
lower_d = defaultdict(int)

for key, val in dict.items():
    lower_d[key.lower()] += val

# Search f-word
for key, val in lower_d.items():
    if key.find('fuck') >= 0:
        print(key.ljust(40), str(val).rjust(1))
