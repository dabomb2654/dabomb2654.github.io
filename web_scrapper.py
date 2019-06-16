import requests
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import pprint

urls_to_scrape = [
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2000",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2017",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2016",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2015",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2014",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2013",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2012",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2011",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2010",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2009",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2008",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2007",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2006",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2005",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2004",
                  "http://www.takawiki.com/tiki-index.php?page=Performances2003",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2002",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2001",
                  #"http://www.takawiki.com/tiki-index.php?page=Performances2018"
                  ]

def grab_links(perf_url):
    r = requests.get(perf_url)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a', href=True)
    links_to_run = []
    for link in links[0:200]:
        links_to_run.append("http://www.takawiki.com/"+link['href'])
    return links_to_run

def run_for_shows(urls, year):
    init_dict = {'EnglishTitle':["English Title"],'JapaneseTitle':["Japanese Title"],'RomanizedTitle':["Romanized Title"],'Director':['Director'],'Author':['Author'],'Composer':['Composer'],'Choreographer':['Choreographer']}
    pd_data = pd.DataFrame(data = init_dict, columns = ["EnglishTitle", "JapaneseTitle", "RomanizedTitle", "Director", "Author", "Composer","Choreographer"])
    path = "C:\Users\plane\Desktop\shows_by_year\\"+year+"_new.csv"
    for x in urls:
        r = requests.get(x)
        soup = BeautifulSoup(r.text, 'html.parser')
        all_data = soup.find("div", {"id":"page-data"})
        titles, two_shows, show_names, revue_names = get_title(all_data)
        primary_prod = get_prod_staff(all_data)
        #split it all up and check
        add_dict_show = {}
        add_dict_revue = {}
        show_title_eng = "N/A"
        show_title_jpn = "N/A"
        show_title_rom = "N/A"
        revue_title_eng = "N/A"
        revue_title_jpn = "N/A"
        revue_title_rom = "N/A"
        show_director = "N/A"
        show_author = "N/A"
        show_composer = "N/A"
        show_choreographer = "N/A"
        revue_director = "N/A"
        revue_author = "N/A"
        revue_composer = "N/A"
        revue_choreographer = "N/A"
        author_check = 1
        director_check = 1
        composer_check = 1
        choreographer_check = 1
        if two_shows == True:
            if show_names[0]:
                show_title_eng = show_names[0]
            if show_names[1]:
                show_title_jpn = show_names[1]
            if show_names[2]:
                show_title_rom = show_names[2]
            if revue_names[0]:
                revue_title_eng = revue_names[0]
            if revue_names[1]:
                revue_title_jpn = revue_names[1]
            if revue_names[2]:
                revue_title_rom = revue_names[2]
        elif two_shows == False:
            if titles[0]:
                if titles[0][1]:
                    show_title_eng = [titles[0][-1]]
            if titles[1]:
                if titles[1][-1]:
                    show_title_jpn = [titles[1][-1]]
            if titles[2]:
                if titles[2][-1]:
                    show_title_rom = [titles[2][-1]]
        for x in primary_prod:
            if "Author" in x[0]:
                if author_check == 2:
                    revue_author = x[1:]
                elif author_check == 1:
                    show_author = x[1:]
                    author_check += 1
            if "Director" in x[0]:
                if director_check == 2:
                    revue_director = x[1:]
                elif director_check == 1:
                    show_director = x[1:]
                    director_check += 1
            if "Author/Director" in x[0]:
                if director_check == 2:
                    revue_director = x[1:]
                elif director_check == 1:
                    show_director = x[1:]
                    director_check += 1
            if "Composer" in x[0]:
                if composer_check == 2:
                    revue_composer = x[1:]
                elif composer_check == 1:
                    show_composer = x[1:]
                    composer_check += 1
            if "Choreographer" in x[0]:
                if choreographer_check == 2:
                    revue_choreographer = x[1:]
                elif choreographer_check == 1:
                    show_choreographer = x[1:]
                    choreographer_check += 1
        author_check = 1
        director_check = 1
        composer_check = 1
        choreographer_check = 1
        show_dir = ""
        show_auth = ""
        show_comp = ""
        show_choreo = ""
        revue_dir = ""
        revue_auth = ""
        revue_comp = ""
        revue_choreo = ""
        names = [show_director, show_author, show_composer, show_choreographer, revue_author, revue_director, revue_composer, revue_choreographer]
        for x in range(len(names)):
            if isinstance(names[x], list):
                if len(names[x]) == 1:
                    if x == 0:
                        show_dir = names[x][0].encode('utf-8')
                    elif x == 1:
                        show_auth = names[x][0].encode('utf-8')
                    elif x == 2:
                        show_comp = names[x][0].encode('utf-8')
                    elif x == 3:
                        show_choreo = names[x][0].encode('utf-8')
                    elif x == 4:
                        revue_dir = names[x][0].encode('utf-8')
                    elif x == 5:
                        revue_auth = names[x][0].encode('utf-8')
                    elif x == 6:
                        revue_comp = names[x][0].encode('utf-8')
                    elif x == 7:
                        revue_choreo = names[x][0].encode('utf-8')
                elif len(names[x]) > 1:
                    if x == 0:
                        for y in range(len(names[x])):
                            show_dir = names[x][y].encode('utf-8') + show_dir
                    elif x == 1:
                        for y in range(len(names[x])):
                            show_auth = names[x][y].encode('utf-8') + show_auth
                    elif x == 2:
                        for y in range(len(names[x])):
                            show_comp = names[x][y].encode('utf-8') + show_comp
                    elif x == 3:
                        for y in range(len(names[x])):
                            show_choreo = names[x][y].encode('utf-8') + show_choreo
                    elif x == 4:
                        for y in range(len(names[x])):
                            revue_dir = names[x][y].encode('utf-8') + revue_dir
                    elif x == 5:
                        for y in range(len(names[x])):
                            revue_auth = names[x][y].encode('utf-8') + revue_auth
                    elif x == 6:
                        for y in range(len(names[x])):
                            revue_comp = names[x][y].encode('utf-8') + revue_comp
                    elif x == 7:
                        for y in range(len(names[x])):
                            revue_choreo = names[x][y].encode('utf-8') + revue_choreo
        add_dict_show = {'EnglishTitle':[show_title_eng[0]],
                         'JapaneseTitle':[show_title_jpn[0]],
                         'RomanizedTitle':[show_title_rom[0]],
                         'Director':[show_dir],
                         'Author':[show_auth],
                         'Composer':[show_comp],
                         'Choreographer':[show_choreo]}
        #get the sum of the length of the values in the dict to check for non shows, 3 is result current
        sum_test = 0
        for key in add_dict_show.keys():
            sum_test += len(add_dict_show[key][0])
        if sum_test >= 4:
            pd_add = pd.DataFrame(data = add_dict_show, columns = ["EnglishTitle", "JapaneseTitle", "RomanizedTitle", "Director", "Author", "Composer","Choreographer"])
            pd_data = pd_data.append(pd_add)
        #pprint.pprint(pd_data)
        if revue_title_eng != "N/A" and revue_title_jpn != "N/A":
            add_dict_revue = {'EnglishTitle':[revue_title_eng[0]],
                              'JapaneseTitle':[revue_title_jpn[0]],
                              'RomanizedTitle':[revue_title_rom[0]],
                              'Director':[revue_dir],
                              'Author':[revue_auth],
                              'Composer':[revue_comp],
                              'Choreographer':[revue_choreo]}
            pd_add = pd.DataFrame(data = add_dict_revue, columns = ["EnglishTitle", "JapaneseTitle", "RomanizedTitle", "Director", "Author", "Composer","Choreographer"])
            pd_data = pd_data.append(pd_add)
            #pprint.pprint(pd_data)
        pd_data.to_csv(path)
    print "generated file at ", path
    
    return 
def get_title(soup):
    title_list = [[],[],[]]
    show_names = [[],[],[]]
    revue_names = [[],[],[]]
    two_show_check = False
    titles = ["English Title:", "Japanese Title:", "Romanized Title:"]
    if soup is not None:
        for child in soup.descendants:
            for x in range(len(titles)):
                if child.string == titles[x]:
                    if child.previous_sibling is not None:
                        if child.previous_sibling.string != child.string:
                            title_list[x].append(child.string.encode('utf-8'))
                            cur = child.next_sibling
                    if cur is not None:
                        if child.previous_sibling is not None:
                            if child.previous_sibling.string != child.string:
                                if cur.string != None:
                                    title_list[x].append(cur.string.encode('utf-8'))
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
    if title_list[0] and "English Title:" in title_list[0]:
        if title_list[0][1] and "/" in title_list[0][1]:
            showname_split = title_list[0][1].split("/")
            show_names[0].append(showname_split[0])
            revue_names[0].append(showname_split[1])
    if title_list[1] and "Japanese Title:" in title_list[1]:
        if len(title_list[1]) > 1:
            if "/" in title_list[1][1]:
                showname_split = title_list[1][1].split("/")
                show_names[1].append(showname_split[0])
                revue_names[1].append(showname_split[1])
    if title_list[2] and "Romanized Title:" in title_list[2]:
        if len(title_list[2]) > 1:
            if "/" in title_list[2][1]:
                showname_split = title_list[2][1].split("/")
                show_names[2].append(showname_split[0])
                revue_names[2].append(showname_split[1])
    else:
        #borrow from English
        if title_list[0] and "/" in title_list[0][1]:
            showname_split = title_list[0][1].split("/")
            show_names[0].append(showname_split[0])
            revue_names[0].append(showname_split[1])
    if len(show_names[0]) > 0:
        two_show_check = True
    #print title_list, show_names, revue_names
    return title_list, two_show_check, show_names, revue_names
        
def get_prod_staff(soup):
    info_list = []
    two_show_check = False
    #get director, composer, choreo, and author
    if soup is not None:
        for child in soup.descendants:
            to_add = []
            if child.previous_sibling is not None and child is not None:
                if child.previous_sibling.string != child.string:
                    cur = child
                    if stop_check_prod(cur) is True:
                        if cur.string != " ":
                            to_add.append(cur.string)
                        if cur is not None:
                            cur = cur.next_sibling
                            if cur is not None:
                                if cur.next_sibling == None:
                                    break
                                while stop_check_prod(cur) == False:
                                    if cur.string != " ":
                                        to_add.append(cur.string)
                                    if cur is not None:
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
    elif "Shinjin Kouen Director" in string_val.string:
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
            '''
            #table_entry:
            #0 - troupe
            #1 - title
            #2 - stars
            #3 - venue
            #4 - date
            '''
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
                stars_end = 3 #table_entry.index(table_entry[-3])
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
for x in urls_to_scrape:
    year = x[-4:]
    print "YEAR", year
    urls = grab_links(x)
    run_for_shows(urls, year)

