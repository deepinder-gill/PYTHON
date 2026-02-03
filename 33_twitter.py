url = input("URL:").strip()

#username = url.replace("https://twitter.com", "") -- i.e. if we use url.replace but it will have ton of loopholes like url can have slash of question mark at end or user might give it without httos so we can also do

#username = url.removeprefix("https://twitter.com/")

#or we can use re.sub

re.sub(r"https://twitter.com/", "", url)
print(f"username: {username}")
