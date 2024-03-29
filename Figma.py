import streamlit as st

st.title(
  'Study Buddy'
)
st.write(
  'Breaking down dense topics without derailing the session!'
)
# image to be added later
st.header(
  'About Study Buddy'
)
st.write(
  'Study Buddy is your all in one AI study companion. It can generate explanations on your documents, make follow up questions and more!'
)
st.header(
  'How To Study Buddy'
)
st.write(
  '1. Upload the files you want to study this session.\n'
  '2. Select a general type of questioning to guide the session.\n'
  '3. Tell your Study Buddy what to explain, ask or do!'
)
st.header(
  'File Upload'
)
st.file_uploader('Upload file for Study Buddy to read.',accept_multiple_files=True)
st.header(
  'Ask your Study Buddy'
)
st.write(
  'Have questions about the submitted file? Lets go through it!'
)
st.selectbox('What should we focus on?',['Explain', 'Follow up questions', 'Test my knowledge', 'Rephrase text', 'Proof', 'Algorithm', 'Proof', 'Make assumptions'])
st.text_input('How can I help?')
