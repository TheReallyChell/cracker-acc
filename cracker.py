import requests
from roblox import Client
from urllib.parse import urljoin

username = "dimazverop"
password = "superdimazverop"

repo_url = "https://github.com/TheReallyChell/files1"

# Create a Roblox client
client = Client()

client.login(username, password)

if client.authenticated:
    print("Logged in successfully.")
else:
    print("Login failed.")
    exit()

response = requests.get(repo_url)
if response.status_code == 200:
    html = response.text
    file_links = []
    for line in html.splitlines():
        if 'href=' in line and 'title="Download"' in line:
            file_url = line.split('href="')[1].split('"')[0]
            file_links.append(urljoin(repo_url, file_url))

    # Download each file
    for file_link in file_links:
        file_response = requests.get(file_link)
        if file_response.status_code == 200:
            filename = file_link.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(file_response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {file_link}")
else:
    print("Failed to download files.")

print("Hacked")

print(username, password)
