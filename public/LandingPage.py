import requests
from bs4 import BeautifulSoup as bs
import json
import re
import os
import shutil

dir = './images/portfolio'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)


#  Gets posts from WDSS IG using the IG API, ive already generated a token.
def getPosts():
    access_token = "IGQVJWMmN5cnFILWV6dU1LNkZATQXBuN01rUEFiWTF1bWRmXzFoeDZAsTlJualRBci0wQ1RHZAmNZAVUJ1NWtQeVBPRlhCWW56ejMxOVdzQTd2ZATZA4MUJPRmFwd3JCVkNueWxDMHI3aHpDakdpY2p3YUtYZAQZDZD"
    url = "https://graph.instagram.com/me/media?fields=id,media_url,caption,timestamp&access_token=" + access_token
    r = requests.get(url)
    data = r.json()
    posts = []
    for m in data["data"]:
        posts.append(
            [m["id"], m["media_url"], m["caption"], m["timestamp"], re.findall(r'(https?://[^\s]+)', m["caption"])])

    return posts


def writeImagesAndJSON(posts):
    jsonList = []
    for post in posts:
        jsonList.append(
            {"title": post[0], "category": ','.join(map(str, post[4])), "image": post[0] + ".png", "url": ""})
        with open("./images/portfolio/m" + post[0] + ".png", "wb") as handle:
            response = requests.get(post[1], stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
            print("post " + post[0] + " written")

    return jsonList


def updateJSON(jsonList):
    with open("./resumeData.json", "r+") as file:
        data = json.load(file)
        data["portfolio"] = {"posts": jsonList}
        file.seek(0)
        file.write(json.dumps(data))
        file.truncate()


def updateOverlay(posts):
    overlayTemplate = """<div id="{MediaID}" class="overlayContainer" style="display:none;"><div class="overlayImage" style="background-image: url(../images/portfolio/{MediaID}.png);"></div><div class="overlayComments"><div class="overlayCaption"><p>{Caption}</p><p>{Date}</p><div class="links">{Links}</div></div></div><button id="{CloseID}" class="closeOverlayButton">CLOSE</button></div>"""
    linksTemplate = """<a class= "captionLink" href="{Link}">"{Link}"</a>"""
    overlay = ""
    for post in posts:
        links = []
        for link in post[4]:
            links.append(linksTemplate.replace("{Link}", link))
        linksToInject = """<div class="linkDivision"></div>""".join(links)
        overlay = overlay + overlayTemplate.replace("{MediaID}", "m"+post[0]).replace("{Caption}", post[2]).replace("{Date}", post[3]).replace("{Links}", linksToInject).replace("{CloseID}", "b"+post[0])

    with open("index.html") as fp:
        soup = bs(fp, "html.parser")
    soup.find("div", attrs={"class": "overlay"}).replaceWith("""<div class="overlay">""" + overlay + """</div>""")
    html = soup.prettify().replace("&lt;", "<").replace("&gt;", ">")
    return html

def updatePage(html):
    newHTML = bs(html, "html.parser").prettify()
    with open("index.html", "w") as lp:
        lp.write(newHTML)


# Get all posts from IG
IGPosts = getPosts()

# Write Images to folder
js = writeImagesAndJSON(IGPosts)

# Update JSON file
updateJSON(js)

# Update the overlay html
newHtml = updateOverlay(IGPosts)

# Update the HTML.
updatePage(newHtml)
