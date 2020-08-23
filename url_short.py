import pyshorteners
url = input("Enter your url ->> ")
simplified = pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted is >>>", simplified)
