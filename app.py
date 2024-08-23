import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama



#function to get response from llama2 model
def get_response(input_text,no_words,story_type):


    #llm model
    llm = Ollama(model="llama3")
    #prompt template
    template= """
         You are a great story writer and writes story of differnet {story_type}types for a topic{input_text} within {no_words} words.

              """

    prompt=PromptTemplate(input_variables=["poetry_type","input_text","no_words"],
                          template=template)

    #generate response form llma2 model
    response= llm(prompt.format(story_type=story_type, input_text=input_text,no_words=no_words))
    print(response)
    return response



st.set_page_config(page_title="Welcome to Story World",
                 layout='wide',
                 page_icon=':balloon:',
                 initial_sidebar_state='expanded')

st.header("Generate Story :balloon:")

input_text=st.text_input("Enter Story topic")

#Creating 2 more additional columns
col1, col2 = st.columns([5, 5])

with col1:
    no_words=st.text_input("No Of Words")

with col2:
    story_type=st.selectbox("Select the type of Story you want!",('Fantasy','Sci-Fi',' Romance'),index=0)


Submit=st.button("Generate")

#final response
if Submit:
    st.write(get_response(input_text,no_words,story_type))