import urllib.request
import re
htmldata = urllib.request.urlopen(input("Enter a url with the http or the https protocol.\n")).read()
# Αφαίρεση όλων των σχολίων με regular expressions.
htmldata = str(htmldata)
htmldata = re.sub("(<!--.*?-->)", "", htmldata, flags = re.DOTALL)
with open("sourcecode.txt", "w+") as sourcecode:
    sourcecode.write(str(htmldata))
infile = open("sourcecode.txt", "r")
for line in infile:
    print(line, end = "")
infile.close()
with open("sourcecode.txt", "r") as infile:
    listsc = [line.strip() for line in infile]
for i in range(len(listsc)):
    listsc[i].replace(" ", "")
atagscount = 0
paragraphscount = 0
breakscount = 0
for i in range(len(listsc)):
    atagscount += listsc[i].count("</a>")
    paragraphscount += listsc[i].count("</p>")
    breakscount += listsc[i].count("<br>")
linechanges = paragraphscount + breakscount
print("The number of links is", atagscount, "\nThe number of line changes is", linechanges)
