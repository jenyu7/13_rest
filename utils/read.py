import urllib2, json

#Returns a list of names for all the Bestseller Lists
def get_list_names():
    name_url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=70995bc868a043d3bd94e12c22604be6"
    data = urllib2.urlopen(name_url)
    d = json.loads(data.read())
    list_names = []
    for name in d["results"]:
        #API states that all spaces must be replaced with hyphens to extract data
        list_names.append([name['list_name'], name['list_name'].replace(" ", "-")])
    return list_names

#Returns a outerionary of book details for all Bestseller Lists
def get_booklist():
    base_url = "http://api.nytimes.com/svc/books/v3/lists.json?api-key=70995bc868a043d3bd94e12c22604be6&list="
    outer = []
    names = get_list_names()
    i = 0
    try:
        for name in names:
            print "\n\n---" +  base_url+name[1] + "---\n\n"
            data = urllib2.urlopen(base_url+name[1])
            d = json.loads(data.read())
            for item in d["results"]:
                inner = {}
                inner["reviews"] = item["reviews"][0]["sunday_review_link"]
                inner["rank"] = item["rank"]
                details = item["book_details"][0]
                inner["publisher"] = details["publisher"]
                inner["descr"] = details["description"]
                inner["author"] = details["author"]
                inner["title"] = details["title"]
                inner["buy"] = item["amazon_product_url"]
                outer.append([inner])
            i += 1
            if (i >= 2):
                break
    except:
        print "too many reqs"
    print outer
    return outer
    
