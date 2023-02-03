import urllib.parse

def extract_inner_link(url):
    url_params = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
    if "url" in url_params:
        inner_link = urllib.parse.unquote(url_params["url"][0])
        inner_link = inner_link.replace("%3A", ":").replace("%2F", "/").replace("%3F", "?").replace("%3D", "=")
        return inner_link
    else:
        return None

url = input("Enter the URL: ")
inner_link = extract_inner_link(url)

if inner_link:
    print("The extracted inner link is:", inner_link)
else:
    print("No inner link found in the URL.")
