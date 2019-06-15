#import os.path
#import pickle
#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request

'''
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET = '1zrAIzl81gSOwz6b8evGYx3WcsHFA3fag-hEA9SZOJ0E'
'''

'''
    init_dict = {'Troupe': ["troupe"], 
                         'English Title': ["eng title"], 
                         'Japanese Title': ["jpn title"], 
                         'Romanized Title':["rom title"], 
                         'Venue': ["venue"],
                         'Director': ["dir"], 
                         'Author': ["auth"], 
                         'Composer': ["comp"], 
                         'Choreographer': ["choreo"],
                         'Top Star':["ts"], 
                         'Number in Run (Top Star)': ["#ts"], 
                         'Top Musumeyaku':["mus"], 
                         'Number in Run (Top Musumeyaku)':["#ms"], 
                         'Lead':["lead"], 
                         'One Act':["oa"],
                         'Two Act':["ta"],
                         'Special':["sp"],
                         'Dinner Show':["ds"],
                         'Genre':["gen"],
                         'Adaption':["adp"],
                         'Adapted From':["adp_frm"],
                         'Revival':["rev"],
                         'Previous Revival Troupe':["prev_rev"],
                         'Start Day':["sd"],
                         'Start Month':["sm"],
                         'Start Year':["sy"],
                         'End Day':["ed"],
                         'End Month':["em"],
                         'End Year':["ey"],}
    panda_dataframe = pd.DataFrame(data = init_dict,
                                     columns = 
                                     ["Troupe",
                                      "EnglishTitle", 
                                      "JapaneseTitle", 
                                      "RomanizedTitle", 
                                      "Venue",
                                      "Director", 
                                      "Author", 
                                      "Composer",
                                      "Choreographer",
                                      "Top Star",
                                      "Number in Run (Top Star)",
                                      "Top Musumeyaku",
                                      "Number in Run (Top Musumeyaku)",
                                      "Lead",
                                      "One Act",
                                      "Two Act",
                                      "Special",
                                      "Dinner Show",
                                      "Genre",
                                      "Adaption",
                                      "Adapted From",
                                      "Revival",
                                      "Previous Revival Troupe",
                                      "Start Day",
                                      "Start Month",
                                      "Start Year",
                                      "End Day",
                                      "End Month",
                                      "End Year"
                                      ])
    
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET, range='A1:AC92').execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            data_dict = {'Troupe': [row[0].encode('utf-8')], 
                         'English Title': [row[1].encode('utf-8')], 
                         'Japanese Title': [row[2].encode('utf-8')], 
                         'Romanized Title':[row[3].encode('utf-8')], 
                         'Venue': [row[4].encode('utf-8')],
                         'Director': [row[5].encode('utf-8')], 
                         'Author': [row[6].encode('utf-8')], 
                         'Composer': [row[7].encode('utf-8')], 
                         'Choreographer': [row[8].encode('utf-8')],
                         'Top Star':[row[9].encode('utf-8')], 
                         'Number in Run (Top Star)': [row[10].encode('utf-8')], 
                         'Top Musumeyaku':[row[11].encode('utf-8')], 
                         'Number in Run (Top Musumeyaku)':[row[12].encode('utf-8')], 
                         'Lead':[row[13].encode('utf-8')], 
                         'One Act':[row[14].encode('utf-8')],
                         'Two Act':[row[15].encode('utf-8')],
                         'Special':[row[16].encode('utf-8')],
                         'Dinner Show':[row[17].encode('utf-8')],
                         'Genre':[row[18].encode('utf-8')],
                         'Adaption':[row[19].encode('utf-8')],
                         'Adapted From':[row[20].encode('utf-8')],
                         'Revival':[row[21].encode('utf-8')],
                         'Previous Revival Troupe':[row[22].encode('utf-8')],
                         'Start Day':[row[23].encode('utf-8')],
                         'Start Month':[row[24].encode('utf-8')],
                         'Start Year':[row[25].encode('utf-8')],
                         'End Day':[row[26].encode('utf-8')],
                         'End Month':[row[27].encode('utf-8')],
                         'End Year':[row[28].encode('utf-8')]}
            row_value = pd.DataFrame(data = data_dict,
                                     columns = 
                                     ["Troupe",
                                      "EnglishTitle", 
                                      "JapaneseTitle", 
                                      "RomanizedTitle", 
                                      "Venue",
                                      "Director", 
                                      "Author", 
                                      "Composer",
                                      "Choreographer",
                                      "Top Star",
                                      "Number in Run (Top Star)",
                                      "Top Musumeyaku",
                                      "Number in Run (Top Musumeyaku)",
                                      "Lead",
                                      "One Act",
                                      "Two Act",
                                      "Special",
                                      "Dinner Show",
                                      "Genre",
                                      "Adaption",
                                      "Adapted From",
                                      "Revival",
                                      "Previous Revival Troupe",
                                      "Start Day",
                                      "Start Month",
                                      "Start Year",
                                      "End Day",
                                      "End Month",
                                      "End Year"
                                      ])
            panda_dataframe = panda_dataframe.append(row_value)
    #pprint.pprint(panda_dataframe['JapaneseTitle'])    
    keys = Troupe
    title_english
    title_japanese
    title_romaji
    Venue
    Director
    Author
    Composer
    Choreographer
    top_star
    num_in_run
    top_musume
    num_in_run.1
    lead
    one_act
    two_act
    special
    dinner_show
    genre
    adaption
    adaption_from
    revival
    previous_revival_troupe
    Start Day
    Start Month
    Start Year
    End Day
    End Month
    End Year
    '''

