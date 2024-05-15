import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_ages(filename):
    big_list = []
    male_ages = []
    female_ages = []

    with open(filename, 'r') as file:
        next(file)
        for line in file:
            big_list.append(line.split(','))

    for line in big_list:
        if line[5] == 'male' and line[6] != '':
            male_ages.append(line[6])
        if line[5] == 'female' and line[6] != '':
            female_ages.append(line[6])

    male_ages = list(map(float, male_ages))
    female_ages = list(map(float, female_ages))

    return male_ages, female_ages

filename = 'data.csv'
male_ages, female_ages = get_ages(filename)

# Создание сайта с изображением Титаника и диаграммой
st.title('Титаник: статистика пассажиров')
st.image('t.jpg', use_column_width=True)

status = st.radio('Выберите статус пассажира:', ('спасен', 'погиб'))
gender = st.radio('Выберите пол пассажира:', ('male', 'female'))

if status == 'спасен':
    if gender == 'male':
        st.write(f'Минимальный возраст спасенных мужчин: {min(male_ages)}')
        st.write(f'Максимальный возраст спасенных мужчин: {max(male_ages)}')
    else:
        st.write(f'Минимальный возраст спасенных женщин: {min(female_ages)}')
        st.write(f'Максимальный возраст спасенных женщин: {max(female_ages)}')
else:
    if gender == 'male':
        st.write(f'Минимальный возраст погибших мужчин: {min(male_ages)}')
        st.write(f'Максимальный возраст погибших мужчин: {max(male_ages)}')
    else:
        st.write(f'Минимальный возраст погибших женщин: {min(female_ages)}')
        st.write(f'Максимальный возраст погибших женщин: {max(female_ages)}')

# Создание диаграммы
fig, ax = plt.subplots()
ax.hist(male_ages, bins=10, alpha=0.5, label='Мужчины')
ax.hist(female_ages, bins=10, alpha=0.5, label='Женщины')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.legend()
st.pyplot(fig)
