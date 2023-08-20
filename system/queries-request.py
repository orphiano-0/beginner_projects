import requests
def search(query):
    with requests.session() as c:
        url = 'https://www.google.com.ph'
        query = {'q': query}
        url_link = requests.get(url, params=query)
        print(url_link)
# return the status code of the function
search("What is google?")