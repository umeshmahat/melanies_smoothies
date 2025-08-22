# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie :cup_with_straw: {st.__version__}")
st.write(
  """Choose the fruits in your custom smoothie!
  """
)


#option = st.selectbox(
#    "What is your favourite fruits?",
#    ("Strawberries", "Peaches", "Banana"),
#)

#st.write("You selected:", option)
#import streamlit as st
Name_On_Order = st.text_input('Name Of Smoothie:')
st.write('the name on your smoothie will be:',Name_On_Order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


Ingredients_list=st.multiselect(
    "Choose Up To 5 Ingredients"
    ,my_dataframe
    #,default=["Apples"]
)

#st.write("You selected:")
#st.text(Ingredients)
#st.write()
if Ingredients_list:
    #st.write(Ingredients_list)
    #st.text(Ingredients_list)

    Ingredients_string =''

    for fruit_chosen in Ingredients_list: 
        Ingredients_string += fruit_chosen +' '

    st.write(Ingredients_list)
    my_insert_stmt = """ insert into smoothies.public.orders(INGREDIENTS,Name_On_Order)
                values ('""" + Ingredients_string + """','"""+ Name_On_Order+"""')"""
    
    st.write(my_insert_stmt)
    time_to_insert= st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

#new section to display smoothiefroot nutrition information
#import requests
#smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#st.text(smoothiefroot_response)
#sf_df = st.dataframe(data=smoothiefroot_response.json(),use_container_width= True)


        
