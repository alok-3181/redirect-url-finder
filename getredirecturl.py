import grequests

with open('urls.txt') as f:
    for content in f:
        content = content.strip('\n')
        content = content.strip('\t')   
        url = "http://" + content

        rs = grequests.get(url, verify=False, redirect=True)
        requests = grequests.map(rs)
        for response in requests:
            print response.url
