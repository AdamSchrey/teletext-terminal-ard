import requests
import html

def input_page():
    site = input("Seite (z.B:100):\n")
    link = "http://www.ard-text.de/index.php?page="+site
    ardtext(link)

def ardtext(link):
    holesite = requests.get(link).text
    holesite = holesite.split(">")
    gettxt = False
    teletext = ""
    for ele in holesite:
        if "ardtext_classic" in ele:
            gettxt = True
        if gettxt == True:
            if "</nobr" in ele:
                teletext+=ele.replace("</nobr","")
            if "</div" in ele:
                teletext+="\n"
            if "</a" in ele:
                teletext+=ele.replace("</a","")
            if "<a onclick" in ele:
                teletext+=ele.split("<")[0]
            if "teleTextNavigation" in ele:
                break

    teletext = html.unescape(teletext)
    if teletext == "":
        print("Ihre Seitenzahl("+link[37:]+") lieferte kein Ergebnis.\n")
    else:
        print(teletext)
    input_page()

if __name__ == "__main__":
    input_page()

