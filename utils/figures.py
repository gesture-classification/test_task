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


def get_all_sensors_plot(id, X_train, plot_counter=None):
    """
    Функция построения диаграммы показания датчиков. Аргумент функции - 
    id - номер наблюдения;
    X_train - обучающая выборка;
    plot_counter - порядковый номер рисунка.
    """
    
    fig = px.line(data_frame=X_train[id].T)
    
    fig.update_layout(
        title=dict(text=f'Рис. {plot_counter}'+' - сигналы датчиков <br> наблюдения ' + str(id), x=.5, y=0.08, xanchor='center'), 
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
        fig.update_layout(title=dict(text=f'Рис. 1 - сигналы датчиков <br> наблюдения ' + str(id), x=.5, y=0.08, xanchor='center'))