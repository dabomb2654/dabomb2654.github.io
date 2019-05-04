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
new_urls = [#"http://www.takawiki.com/tiki-index.php?page=The%20way%20Yu%20are%20Dinner%20Show%20(2002)",
            #"http://www.takawiki.com/tiki-index.php?page=Miracle+of+the+Holy+Star+%28Cosmos+2002-03%29",
            "http://www.takawiki.com/tiki-index.php?page=S%20Dinner%20Show%20(2002)",
            "http://www.takawiki.com/tiki-index.php?page=At+the+End+of+A+Long+Spring+%28Moon+2002%29"]
def run_for_shows(urls):
    for x in urls:
        print "URL", x
        init_dict = {'EnglishTitle':["English Title"],'JapaneseTitle':["Japanese Title"],'RomanizedTitle':["Romanized Title"],'ShowDirector':['Show Director'],'ShowAuthor':['Show Author'],'ShowComposer':['Show Composer'],'ShowChoreographer':['Show Choreographer'],'':[''],}
        pd_data = pd.DataFrame(data = init_dict, columns = [""])
        r = requests.get(x)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print soup.prettify()
        all_data = soup.find("div", {"id":"page-data"})
        #print "ALL", all_data
        get_title(all_data)
        #primary_prod = get_prod_staff(all_data)
        #print primary_prod
    return 
def get_title(soup):
    title_list = [[],[],[]]
    show_names = [[],[],[]]
    revue_names = [[],[],[]]
    titles = ["English Title:", "Japanese Title:", "Romanized Title:"]
    for child in soup.descendants:
        for x in range(len(titles)):
            if child.string == titles[x]:
                if child.previous_sibling is not None:
                    if child.previous_sibling.string != child.string:
                        title_list[x].append(child.string)
                        cur = child.next_sibling
                if cur is not None:
                    if child.previous_sibling is not None:
                        if child.previous_sibling.string != child.string:
                            title_list[x].append(cur.string)
    #check for two shows
    '''
    breakdown: 
    title_list[0] = eng
    title_list[1] = jpn
    title_list[2] = rom
    title_list[0][0] = "English Title:"
    title_list[0][1] = TITLE IN ENGLISH
    title_list[1][0] = "Japanese Title:"
    title_list[1][1] = TITLE IN JAPANESE
    title_list[2][0] = "Romanized Title:"
    title_list[2][1] = TITLE IN ROMANIZED
    '''
    if "English Title:" in title_list[0]:
        if "/" in title_list[0][1]:
            showname_split = title_list[0][1].split("/")
            print "SPLIT_eng", showname_split
            show_names[0].append(showname_split[0])
            revue_names[0].append(showname_split[1])
    else: 
        print "No English Split"
        return
    if "Japanese Title:" in title_list[1]:
        if "/" in title_list[1][1]:
            showname_split = title_list[1][1].split("/")
            print "SPLIT_jpn", showname_split
            show_names[1].append(showname_split[0])
            revue_names[1].append(showname_split[1])
    else:
        print "No Japanese Split"
        return
    if "Romanized Title:" in title_list[2]:
        if "/" in title_list[2][1]:
            showname_split = title_list[2][1].split("/")
            print "SPLIT_rom", showname_split
            show_names[2].append(showname_split[0])
            revue_names[2].append(showname_split[1])
        else:
            print "No Rom split"
    else:
        #borrow from English
        if "/" in title_list[0][1]:
            showname_split = title_list[0][1].split("/")
            print "SPLIT_eng", showname_split
            show_names[0].append(showname_split[0])
            revue_names[0].append(showname_split[1])
        else:
            print "No English Split (rom)"
    print "TITLES", title_list
    print "SHOWS", show_names
    print "REVUES", revue_names
    return title_list, show_names, revue_names
        
def get_prod_staff(soup):
    info_list = []
    #get director, composer, choreo, and author
    for child in soup.descendants:
        to_add = []
        if child.previous_sibling is not None and child is not None:
            if child.previous_sibling.string != child.string:
                cur = child
                if stop_check_prod(cur) is True:
                    if cur.string != " ":
                        to_add.append(cur.string)
                    cur = cur.next_sibling
                    if cur.next_sibling == None:
                        break
                    while stop_check_prod(cur) == False:
                        if cur.string != " ":
                            to_add.append(cur.string)
                        cur = cur.next_sibling
        elif child.previous is None and child is not None:
            info_list.append(child.string)
        if to_add != []:
            info_list.append(to_add)
    return info_list
def stop_check_prod(string_val):
    stop = False
    if string_val == None:
        return
    if string_val.string == None:
        return
    if "Director" in string_val.string:
        stop = True
    elif "Author" in string_val.string:
        stop = True
    elif "Choreographer" in string_val.string:
        stop = True
    elif "Composer" in string_val.string:
        stop = True
    elif "Available" in string_val.string:
        stop = True
    return stop
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
        
#run(urls_to_scrape)
run_for_shows(new_urls)

