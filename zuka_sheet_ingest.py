import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1zrAIzl81gSOwz6b8evGYx3WcsHFA3fag-hEA9SZOJ0E'
#SAMPLE_RANGE_NAME = 'Performances2000!A:A'

def main():
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
    '''
    result = sheet.values().get(spreadsheetId=\SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            print row
    '''
    #2000 - 469197924
    #2001 - 911571157
    #2002 - 386730168
    #2003 - 1961619490
    #2004 - 
    #2005 - 1507870647
    #2006 - 353917322
    #2007 - 1905111971
    #2008 - 
    #2009-  1897219538
    #2011 - 102620884
    #2012 - 1920445980
    #2013 - 301641258
    #2014 - 1889776436
    #2015 - 257370383
    #2016 - 143772276
    #2017 - 2121177408
    #2018 - 447462528

    sheetIds = ['469197924','911571157', '386730168', '1961619490', '1507870647','353917322','1905111971','1897219538','102620884','1920445980','301641258','1889776436','257370383','143772276', '2121177408', '447462528']
    requests = []
    x = 0
    for sheetId in sheetIds:
        t_name = "troupe"+str(x)
        te_name = "title_english"+str(x)
        tj_name = "title_japanese"+str(x)
        tr_name = "title_romaji"+str(x)
        v_name = "venue"+str(x)
        d_name = "director"+str(x)
        a_name = "author"+str(x)
        cm_name = "composer"+str(x)
        ch_name = "choreographer"+str(x)
        ts_name = "top_star"+str(x)
        tsn_name = "top_star_num"+str(x)
        tm_name = "top_musume"+str(x)
        tmn_name = "top_musume_num"+str(x)
        l_name = "lead"+str(x)
        o_name = "one_act"+str(x)
        tw_name = "two_act"+str(x)
        sp_name = "special"+str(x)
        ds_name = "dinner_show"+str(x)
        gen_name = "genre"+str(x)
        ad_name = "adapt"+str(x)
        adf_name = "adapt_from"+str(x)
        rev_name = "revival"+str(x)
        prev_name = "prev_rev"+str(x)
        sd_name = "start_day"+str(x)
        sm_name = "start_month"+str(x)
        sy_name = "start_year"+str(x)
        ed_name = "end_day"+str(x)
        em_name = "end_month"+str(x)
        ey_name = "end_year"+str(x)
        x = x + 1
        print x
        if x == 4:
            x = x+1
        if x == 8:
            x = x + 1
        if x == 10:
            x = x + 1

    #update named ranges
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": t_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 0,
                            "endColumnIndex": 1,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": te_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 1,
                            "endColumnIndex": 2,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tj_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 2,
                            "endColumnIndex": 3,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tr_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 3,
                            "endColumnIndex": 4,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": v_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 4,
                            "endColumnIndex": 5,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": d_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 5,
                            "endColumnIndex": 6,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": a_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 6,
                            "endColumnIndex": 7,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": cm_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 7,
                            "endColumnIndex": 8,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ch_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 8,
                            "endColumnIndex": 9,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ts_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 9,
                            "endColumnIndex": 10,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tsn_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 10,
                            "endColumnIndex": 11,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tm_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 11,
                            "endColumnIndex": 12,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tmn_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 12,
                            "endColumnIndex": 13,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": l_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 13,
                            "endColumnIndex": 14,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": o_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 14,
                            "endColumnIndex": 15,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": tw_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 15,
                            "endColumnIndex": 16,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": sp_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 16,
                            "endColumnIndex": 17,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ds_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 17,
                            "endColumnIndex": 18,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": gen_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 18,
                            "endColumnIndex": 19,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ad_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 19,
                            "endColumnIndex": 20,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": adf_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 20,
                            "endColumnIndex": 21,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": rev_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 21,
                            "endColumnIndex": 22,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": prev_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 22,
                            "endColumnIndex": 23,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": sd_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 23,
                            "endColumnIndex": 24,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": sm_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 24,
                            "endColumnIndex": 25,
                    },
                }
            }
    })
        '''
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": sy_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 25,
                            "endColumnIndex": 26,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ed_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 26,
                            "endColumnIndex": 27,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": em_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 27,
                            "endColumnIndex": 28,
                    },
                }
            }
    })
        requests.append({
                "addNamedRange":{
                    "namedRange": {
                        "name": ey_name,
                        "range":{
                            "sheetId": sheetId,
                            "startRowIndex": 0,
                            "endRowIndex": 200,
                            "startColumnIndex": 28,
                            "endColumnIndex": 29,
                    },
                }
            }
    })
    '''
    body = {
        'requests': requests
    }

    response = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, 
        body=body).execute()
    print response

if __name__ == '__main__':
    main()