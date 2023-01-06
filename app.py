import streamlit as st
import pickle
import pandas as pd

def recommender(product):
    index = products[products['product_name'] == product].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_products=[]
    for i in distances[1:6]:
        recommended_products.append(products.iloc[i[0]].product_name)
    return recommended_products   
    


product_dict=pickle.load(open('product_dict.pkl','rb'))
products=pd.DataFrame(product_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Product recommendation system')


selected_product_name=st.selectbox('Please select the product name.',products['product_name'].values)

if st.button('Recommend'):
    recommendations=recommender(selected_product_name)
    for i in recommendations:
        st.write(i)