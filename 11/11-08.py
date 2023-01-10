url = input()
k = input()
url = url[url.index(k) + len(k) + 1:]
if url.find('&') >= 0:
    url = url[:url.find('&')]
    print(url)
else:
    print(url)
    