import streamlit
streamlit.title('My parents healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥣 omege 3 and oatmeal')
streamlit.text('🥗 kale,spinach and rocket smoothie')
streamlit.text('🐔 hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruits_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruits_list)
stream.multiselect('pick up some fruits',list(my_fruits_list.index))
#display table on the page
streamlit.dataframe(my_fruits_list)




