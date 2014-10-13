from BeautifulSoup import BeautifulSoup
import urllib2
 
wiki = "http://sudo.utero.pe/2014/06/07/universidades-peru-intro/"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
 
area = ""
district = ""
town = ""
county = ""
 
table = soup.find("table", { "class" : "aligncenter" })
#print table
f = open('universities.csv', 'w')
 
for row in table.findAll("tr"):
    cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
    if len(cells) == 4:
        universidad = cells[0].find(text=True)
        tipo = cells[1].findAll(text=True)
        lugar = cells[2].find(text=True)
        region = cells[3].find(text=True)
    print "----------------------------------------------------------------------------+++"
    print universidad
 #   print tipo
    print lugar
    print region

    write_to_file = universidad + ", " + lugar + ", " + region + "\n"
    f.write(write_to_file.encode('utf-8'))
    #print cells
    #print len(cells)
    #district can be a list of lists, so we want to iterate through the top level lists first...
    """for x in range(len(district)):
        #For each list, split the string
        postcode_list = district[x].split(",")
        #For each item in the split list...
        for i in range(len(postcode_list)):
            #Check it's a postcode and not other text
            if (len(postcode_list[i]) > 2) and (len(postcode_list[i]) <= 5):
                #Strip out the "\n" that seems to be at the start of some postcodes
                write_to_file = area + "," + postcode_list[i].lstrip('\n').strip() + "," + town + "," + county + "\n"
                print write_to_file
                f.write(write_to_file)
    """
f.close()
