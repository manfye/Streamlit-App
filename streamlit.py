# import statements
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
import time
from datetime import date
from io import StringIO

# adding title and text in the app

st.write("Welcome to your first streamli application")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.title("Gainers")
select = st.sidebar.selectbox('Share', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')

df = pd.DataFrame({'col1': [1,2,3]})

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x
st.markdown('Streamlit is **_really_ cool**.')
st.latex(r'''
   a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.write(1234)
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')


df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  

st.dataframe(df, 200, 100)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df)

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.area_chart(chart_data)
st.bar_chart(chart_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

dfmap = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(dfmap)

image = Image.open('food.png')
st.image(image, caption='Sunrise by the mountains')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')


genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)


number = st.number_input('Insert a number')
st.write('The current number is ', number)

def run_sentiment_analysis(txt):
    return "Hello"

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair     ''')
st.write('Sentiment:', run_sentiment_analysis(txt))

d = st.date_input(
     "When's your birthday",
     date(2019, 7, 6))
st.write('Your birthday is:', d)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)



name = st.text_input('Name')
if not name:
   st.warning('Please input a name.')
#    st.stop()
st.success('Thank you for inputting a name.')


color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")

col1, col2, col3 = st.beta_columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed. !!

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
st.write('Done!')

my_bar = st.progress(0)

# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)

# with st.spinner('Wait for it...'):
#     time.sleep(5)
st.success('Done')
# st.balloons()
st.error('This is an error')
st.warning('This is a warning')
st.info('This is a purely informational message')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

# with st.empty():
#     for seconds in range(60):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")

st.help(pd.DataFrame)

df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(
   np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

my_table.add_rows(df2)
