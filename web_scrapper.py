import requests
import pandas as pd
from bs4 import BeautifulSoup, NavigableString

urls_to_scrape = [
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2010",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2009",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2008",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2007",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2006",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2005",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2004",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2003",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2002",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2001",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2000",]
def run(urls):
    for x in urls_to_scrape:
        year = x[-4:]
        print year
        intro_dictionary = {'Troupe':["Troupe"],'Show': ["Show"], 'Alt Show Name':["Alternate Show Name"], 'Stars':["Stars"],'Venue':["Venue"],'Start Day':["Start Day"],'Start Month':["Start Month"],'Start Year':["Start Year"], 'End Day':["End Day"], 'End Month':["End Month"], 'End Year':["End Year"]}
        pd_data = pd.DataFrame(data = intro_dictionary, columns = ["Troupe", "Show", "Alt Show Name", "Stars", "Venue", "Start Day", "Start Month", "Start Year", "End Day", "End Month", "End Year"])
        r = requests.get(x)
        soup = BeautifulSoup(r.text, 'html.parser')
        table_data = soup.find_all('tr')
        schedule = []
        prev_table_entry_length = 0
        table_entry = []
        for y in range(len(table_data)):
            t=0
            sam = table_data[y]
            prev_table_entry_length = len(table_entry)
            table_entry = []
            for child in sam.descendants:
                if isinstance(child, NavigableString) == True:
                    child_readable = str(child.encode('utf-8'))
                    if child_readable != " ":
                        table_entry.append(child_readable)
                        t+=1
            #table_entry:
            #0 - troupe
            #1 - title
            #2 - stars
            #3 - venue
            #4 - date
            if prev_table_entry_length == 0:
                new_show = True
                date = table_entry[-1]
                s_d = "check"
                s_m = "check"
                e_d = "check"
                e_m = "check"
                s_y = year
                e_y = year
                if "-" in date:
                    date_split = date.split("-")
                    s_d = date_split[0].split("/")[1]
                    s_m = date_split[0].split("/")[0]
                    e_d = date_split[1].split("/")[1]
                    e_m = date_split[1].split("/")[0] 
                stars_start = 2
                stars_end = 3#table_entry.index(table_entry[-3])
                stars = ""
                for x in table_entry[stars_start:stars_end]:
                    stars = stars+x
                add_dict = {'Troupe':[table_entry[0]],'Show': [table_entry[1]], 'Alt Show Name':["N/A"], 'Stars':[stars],'Venue':[table_entry[-2]],'Start Day':[s_d],'Start Month':[s_m],'Start Year':[s_y], 'End Day':[e_d], 'End Month':[e_m], 'End Year':[e_y]}
                pd_add = pd.DataFrame(data = add_dict, columns = ["Troupe", "Show", "Alt Show Name", "Stars", "Venue", "Start Day", "Start Month", "Start Year", "End Day", "End Month", "End Year"])
                pd_data = pd_data.append(pd_add) 
            elif len(table_entry) == 1 and prev_table_entry_length > 1:
                pd_data.iat[-1, 2] = table_entry[0]
            elif len(table_entry) == 1 and prev_table_entry_length == 1:
                value_to_update = pd_data.iat[-1, 2]
                value_to_update = value_to_update + ","+table_entry[0]
                pd_data.iat[-1, 2] = value_to_update
        path = "C:\Users\Admin\Desktop\performances" + year +".csv"
        pd_data.to_csv(path)
        print "generated file at ", path
run(urls_to_scrape)

