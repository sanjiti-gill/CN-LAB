url = input("Enter a URL: ")

protocol = "NULL"
port = "NULL"
path = "NULL"

# Protocol
if "://" in url:
    protocol, url = url.split("://", 1)

# Path
if "/" in url:
    url, path = url.split("/", 1)
    path = "/" + path

# Port
if ":" in url:
    host, port = url.split(":", 1)
else:
    host = url

print("Protocol:", protocol)
print("Host/Domain:", host)
print("Port:", port)
print("Path:", path)
