# Библиотека функций для ноутбука 1-го этапа соревнования Моторика


# Импортируем библиотеки
import pandas as pd
import numpy as np

# графические библиотеки
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sys
# Библиотека вызова функций, специально разработанных для данного ноутбука
sys.path.insert(1, '../')

from utils.functions import config_reader
 

# import constants from the config
config = config_reader('../config/data_config.json') 


def get_all_sensors_plot(id, X_train, plot_counter=None):
    """
    Функция построения диаграммы показания датчиков. Аргумент функции - 
    id - номер наблюдения;
    X_train - обучающая выборка;
    plot_counter - порядковый номер рисунка.
    """
    
    fig = px.line(data_frame=X_train[id].T)
    
    fig.update_layout( 
        xaxis_title_text = 'Время', 
        yaxis_title_text = 'Сигналы датчиков', # yaxis_range = [0, 3000],
        legend_title_text='Индекс <br>датчика',
        width=600, height=400,
        margin=dict(l=20, r=20, t=20, b=100),
    )

    fig.show()

    # # сохраним результат в папке figures. Если такой папки нет, то создадим её
    # if not os.path.exists("figures"):
    #     os.mkdir("figures")

    if plot_counter is not None:
        fig.write_image(f'../figures/fig_{plot_counter}.png', engine="kaleido")
    else:
        
        plot_counter = 1
        
    fig.update_layout(title=dict(text=f'Рис. {plot_counter} - сигналы датчиков <br> наблюдения ' + str(id), x=.5, y=0.08, xanchor='center'))
        
def get_sensor_command_plot(id:str, X_train:np.ndarray, y_train:pd.Series, plot_counter=None):
    """
    Plots 2 diagrams: sensors signals of the given test and the manipulator command. 
    id - test number;
    X_train - sensor data;
    y_train - manipulator's command;
    plot_counter - figure number.
    """
    
    fig = make_subplots(rows=2, cols=1,
        subplot_titles=(f'Sensor signals', 'y_train - original manipulator command'), vertical_spacing=0.15,
    )
    
    for i in range(X_train.shape[1]): 
        fig.add_trace(go.Scatter(x=np.arange(len(X_train[id].T)), y=X_train[id, i].T), row=1, col=1) 
    
    y_signals = y_train.values[X_train.shape[2] * id : X_train.shape[2] * (id + 1)]
    
    for i in range(len(y_signals)): 
        fig.add_trace(go.Scatter(
            x=np.arange(len(X_train[id].T)), y=y_signals), row=2, col=1) #, name=str(df_1[i].name)

    
    fig.update_layout(width=600, height=600, legend_title_text ='Sensor id',
                        xaxis_title_text='Period', yaxis_title_text='Sensor signal',  # yaxis_range=[1500, 1700],
                        xaxis2_title_text='Period', yaxis2_title_text='Gestures', yaxis2_range=[-1, len(config.gestures)],
                        yaxis2=dict(
                                    tickmode='array',  # change 1
                                    tickvals=np.arange(len(config.gestures)),  # change 2
                                    ticktext=config.gestures),
                        margin=dict(l=40, r=60, t=30, b=80),  
                        showlegend=False  # легенда загромождает картинку
    )
    
    if plot_counter is not None:
        fig.write_image(f'../figures/fig_{plot_counter}.png', engine="kaleido")
        
    else:
        plot_counter = 1
    
    
    fig.update_layout(title={'text':
        f'Fig. {plot_counter} - Sensors signals and the original manipulator command <br> during the sample # ' + str(id),
        'x': 0.5, 'y': 0.01}
    )


    fig.show()  