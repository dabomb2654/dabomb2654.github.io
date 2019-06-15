import pandas as pd
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.plotly as plpl
import datetime

def main():
    
    from_csv = pd.read_csv("C:\\Users\\plane\\Documents\\GitHub\\online-charts\\misc\\zuka_performances-performances2000.csv", encoding='utf-8')
    app = dash.Dash(__name__)
    server = app.server
    time_val = str(datetime.datetime.now())
    # num_shows_piechart
    troupe_names = ['Flower','Snow','Moon','Cosmos','Star','Senka']
    troupe_names_jpn = ['花組','月組','星組','雪組','宙組','専科']
    numFlower = 0
    numSnow = 0
    numStar = 0 
    numCosmos = 0
    numMoon = 0
    numSenka = 0
    for key in from_csv:
        print (key)
    for x in from_csv["Troupe"]:
        if "Flower" in x:
            numFlower += 1
        if "Snow" in x:
            numSnow += 1
        if "Star" in x:
            numStar += 1
        if "Cosmos" in x:
            numCosmos += 1
        if "Moon" in x:
            numMoon += 1
        if "Senka" in x:
            numSenka += 1
    labels=troupe_names
    colors = ['#F489A1','#A8D7C4', '#F2D269', '#E5C6DE', '#5ABCD8', '#5C508D']
    values = [numFlower, numSnow, numMoon, numCosmos, numStar, numSenka]
    data = [{
          'values': values,
          'labels':labels,
          'type': 'pie',
          'showlegend': True,
        },
        ]
    #graph = makePie(labels, values)
    id_name = 'graph'+time_val
    line_data = [{
          'x': [906, 1013],
          'y': [1, 1],
          'type': 'scatter',
          'mode': 'lines+markers',
          'showlegend': True,
        },
        {
          'x': [1004, 1111],
          'y': [2, 2],
          'type': 'scatter',
          'mode': 'lines+markers',
          'showlegend': True,
        },
        {
          'x': [1012, 1110],
          'y': [3, 3],
          'type': 'scatter',
          'mode': 'lines+markers',
          'showlegend': True,
        },
        {
          'x': [1016, 1017, 1022],
          'y': [4, 4, 4],
          'type': 'scatter',
          'mode': 'markers',
          'showlegend': True,
        },
        ]
    app.layout = html.Div(children=[
    html.H1('Number of shows per troupe'),
    #graph
    dcc.Graph(
        id='numshowspie',
        figure={
        'data': data,
        'layout': {
            'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
            },
            'legend':{'Flower':numFlower, 'Snow':numSnow, 'Cosmos':numCosmos, 'Snow':numSnow, 'Senka':numSenka, 'Moon':numMoon}
            }
          }
      ),
    dcc.Graph(
        id=id_name,
        figure={
        'data': line_data,
        }
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True, port='8051')
    plpl.iplot([pieChart],filename='piecharttest')
    return

def importAllData():
  path = "C:\\Users\\plane\\Documents\\GitHub\\online-charts\\misc\\"
  csv_list = [path+"zuka_performances-performances2000.csv",
              path+"zuka_performances-performances2000.csv"]
  from_csv = pd.read_csv(csv_list[0], encoding='utf=8')
  for csv in csv_list[1:]:
      from_csv.append(pd.read_csv(csv, encoding='utf-8'))
  return from_csv
'''
def makePie(labels, values):
  data = [{
          'values': values,
          'labels':labels,
          'type': 'pie',
          'showlegend': True,
          'bgcolor': '#FFFFFF',
          'bordercolor': '#000000',
          'family': 'Raleway', 'Balto', 'Times New Roman', 
        },
        ]
  graph = dcc.Graph(
        id='numshowspie',
        figure={
        'data': data,
        'layout': {
            'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
            },
            'legend':{'Flower':labels[0], 'Snow':labels[1], 'Cosmos':labels[2], 'Snow':labels[3], 'Senka':labels[4], 'Moon':labels[5]}
            }
          }
      )
  return graph
'''
main()
#help(dcc.Graph)

