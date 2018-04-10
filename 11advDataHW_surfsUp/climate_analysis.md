

```python
import warnings
warnings.filterwarnings('ignore')
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func


```


```python
engine = create_engine("sqlite:///hawaii.sqlite",echo=False)
```


```python
engine.execute('SELECT * FROM measurements LIMIT 5').fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65.0),
     (2, 'USC00519397', '2010-01-02', 0.0, 63.0),
     (3, 'USC00519397', '2010-01-03', 0.0, 74.0),
     (4, 'USC00519397', '2010-01-04', 0.0, 76.0),
     (5, 'USC00519397', '2010-01-06', 0.0, 73.0)]




```python
Base = automap_base()
Base.prepare(engine,reflect=True)
Base.classes.keys()




```




    ['measurements', 'stations']




```python
Measurement = Base.classes.measurements
Station = Base.classes.stations


```


```python
session = Session(engine)
```

## Design a query to retrieve the last 12 months of precipitation data.




```python
from sqlalchemy import inspect, func, desc, extract, select
import datetime
from dateutil import parser
import pandas as pd
import numpy as np

inspector = inspect(engine)
columns = inspector.get_columns('measurements')
for column in columns:
    print(column['name'], column['type'])



```

    id INTEGER
    station TEXT
    date DATE
    prcp FLOAT
    tobs FLOAT
    


```python
engine.execute('SELECT * FROM measurements LIMIT 5').fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65.0),
     (2, 'USC00519397', '2010-01-02', 0.0, 63.0),
     (3, 'USC00519397', '2010-01-03', 0.0, 74.0),
     (4, 'USC00519397', '2010-01-04', 0.0, 76.0),
     (5, 'USC00519397', '2010-01-06', 0.0, 73.0)]




```python
sel = [Measurement.station, Measurement.date, Measurement.prcp]
annual_rainfall = session.query(*sel).order_by(Measurement.date.desc()).all()
annual_rainfall_df = pd.DataFrame(np.array(annual_rainfall).reshape(len(annual_rainfall),3), 
                                  columns = ['STATION','DATE', 'RAIN'])
annual_rainfall_df.head(10)
       
       
       
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STATION</th>
      <th>DATE</th>
      <th>RAIN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2017-08-23</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00514830</td>
      <td>2017-08-23</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519523</td>
      <td>2017-08-23</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00516128</td>
      <td>2017-08-23</td>
      <td>0.45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2017-08-22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>2017-08-22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00516128</td>
      <td>2017-08-22</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00519397</td>
      <td>2017-08-21</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00514830</td>
      <td>2017-08-21</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>9</th>
      <td>USC00519523</td>
      <td>2017-08-21</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
last12_months = session.query(Measurement.station, Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()
last12_months_df = pd.DataFrame(last12_months)
last12_months_df.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2016-08-23</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>2016-08-23</td>
      <td>0.15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>2016-08-23</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>2016-08-23</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519523</td>
      <td>2016-08-23</td>
      <td>0.02</td>
    </tr>
  </tbody>
</table>
</div>



## PLOT DATES VS. PRECIPITATION


```python
import cmocean
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.axes import Subplot
import matplotlib.ticker as mtick
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools



```


```python
x = last12_months_df.date
y = last12_months_df.prcp
station = last12_months_df.station

cmap = cmocean.cm.ice

trace1 = go.Bar(
    x=x, 
    y=y, 
    name= "Rain by Date"
)

marker = dict(
    cmap=cmap,
    line=dict(colorscale=cmap, width=1.5), 
    hoverlabel=True,
    text = last12_months_df.station,
    hoverinfo='text',
    opacity=0.6
)
  
data = [trace1] 
layout = go.Layout(
    title="Precipitation Analysis",
        titlefont=dict(
            family='Raleway',
            size=18
        ),
    xaxis=dict(
        tickangle=-45,
        title="Date",
            titlefont=dict(
                family='Raleway',
                size=16
            ),
        showgrid=True,
        ),
    yaxis=dict(
        title='Rainfall',
            titlefont=dict(
                family='Raleway',
                size=16
            ),
        showgrid=True
    ),
    showlegend=True,
    legend=dict(
        x=x, 
        y=y, 
        traceorder='normal',
        font=dict(
            family='Raleway', 
            size=14
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)   
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~tatertot53/120.embed" height="525px" width="100%"></iframe>




```python
last12_months_df.describe()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2230.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.160664</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.442067</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.010000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.110000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6.700000</td>
    </tr>
  </tbody>
</table>
</div>



## STATION ANALYSIS


```python
totalStations = session.query(Measurement.station).distinct().count()
```


```python
session.query(Measurement.station, func.count(Measurement.tobs)).group_by(Measurement.station).\
    order_by(desc(func.count(Measurement.tobs))).all()
```




    [('USC00519281', 2772),
     ('USC00519397', 2724),
     ('USC00513117', 2709),
     ('USC00519523', 2669),
     ('USC00516128', 2612),
     ('USC00514830', 2202),
     ('USC00511918', 1979),
     ('USC00517948', 1372),
     ('USC00518838', 511)]




```python
most_active = session.query(Measurement.station, func.count(Measurement.tobs)).\
                group_by(Measurement.station).\
                order_by(desc(func.count(Measurement.tobs))).first()

```


```python
most_active
```




    ('USC00519281', 2772)




```python
details_most_active = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > '2016-08-23', Measurement.station == most_active.station).all()
details_most_active_df = pd.DataFrame(details_most_active)
details_most_active_df.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-08-24</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-08-25</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-08-26</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-08-27</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-08-28</td>
      <td>73.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
x0 = details_most_active_df.tobs
x1 = details_most_active_df.date

trace1 = go.Histogram(
    x=x0,
    name='TObs',
    nbinsx=12,
    xbins=dict(
        start=55,
        end=85,
        size=2.5
    ),
    marker=dict(
        color='rgba(171, 50, 96, 0.6)'
    ),
    opacity=0.75
)

data = [trace1]

layout = go.Layout(
    title='Station Analysis',
    titlefont=dict(
                family='Raleway',
                size=18
            ),
    xaxis=dict(
        title='Value',
        showgrid=True,
        titlefont=dict(
                family='Raleway',
                size=16
            )
    ),
    yaxis=dict(
        title='Frequency',
        showgrid=True,
        titlefont=dict(
                family='Raleway',
                size=16
            )
    ),
    bargap=0.1
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~tatertot53/122.embed" height="525px" width="100%"></iframe>



## TEMPERATURE ANALYSIS


```python
def calc_temps (start_date, end_date, plot=True):
    temp = session.query(func.avg(Measurement.tobs),
                         func.min(Measurement.tobs).label('min_temp'), 
                         func.max(Measurement.tobs).label('avg_temp')).\
                            filter((Measurement.date >= start_date) & (Measurement.date <= end_date)).all()[0]        
    print("Min Temp = %2.2f,  Avg Temp = %2.2f,  Max Temp = %2.2f" \
        % (temp[1], temp[0], temp[2]))
    trace = go.Bar(
        y=temp[0],
        width = 0.25,
        name="Average Temps",
        marker = dict(
            color = 'hsl(358, 78%, 47%)',
        ),
        error_y = dict(
            type = 'constant',
            value = list(temp),
            thickness = 3,
            color = 'hsl(312, 6%, 33%)'
        ),
        )
    
    data= [trace]
    
    layout = go.Layout(
        title = "<b>Trip Average Temp</b>",
        titlefont = dict(
            family = 'Raleway',
            size = 18,
        ),
        yaxis = dict(title = 'Temperature'),
        xaxis = dict(title = '{} to {}'.format(start_date, end_date),
                    showticklabels=False),
        )
    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig)
    
  

```


```python
calc_temps('2015-01-24', '2016-01-24')
```

    Min Temp = 56.00,  Avg Temp = 74.11,  Max Temp = 86.00
    




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~tatertot53/124.embed" height="525px" width="100%"></iframe>



## CREATE FLASK APPLICATION
