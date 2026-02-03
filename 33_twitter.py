import re
url = input("URL:").strip()

#username = url.replace("https://twitter.com", "") -- i.e. if we use url.replace but it will have ton of loopholes like url can have slash of question mark at end or user might give it without httos et cetera so we can also do

#username = url.removeprefix("https://twitter.com/")

#or we can use re.sub

username = re.sub(r"^(https?://)?(www\.)?twitter.com/", "", url)
print(f"username: {username}")
