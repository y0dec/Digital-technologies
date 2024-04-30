import numpy as np
import csv
import matplotlib.pyplot as plt
import plotly
import pandas as pd
from bokeh.plotting import figure, output_file, show


url = 'https://drive.google.com/uc?export=download&id=1XHsqYXngEBtabg2eEHnbTCZBbK-KYCFD'

input_df = pd.read_csv(url)

matrix = input_df.values
print(input_df.head())
print('...')
for i in range(60282, 60287):
    print(f'{i}{matrix[i][0]}')

znach = matrix[0:1280]
vremy = np.arange(0, len(znach), 1)
p = znach**2 * 10

sr_p = p.mean()
sr_I = (abs(znach)).mean()
print(f'Среднее значение мощности по графику: {sr_p} > среднее значение мощности по формуле: {sr_I ** 2 * 10}')

graph1 = figure(title='Сила тока', x_axis_label='t, мин', y_axis_label='I, А')
graph2 = figure(title='Мощность', x_axis_label='t, мин', y_axis_label='P, Вт')
y1 = list(map(lambda x: x[0], znach))
y2 = list(map(lambda x: x[0], p))
graph1.line(vremy, y1)
graph2.line(vremy, y2)
output_file('График силы тока.html')
show(graph1)
output_file('График мощности.html')
show(graph2)

data_frame = pd.DataFrame(p)
data_frame.to_csv('График мощности.csv', index = False, header = ['Power'])
