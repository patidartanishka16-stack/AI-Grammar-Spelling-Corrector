import streamlit as st
import language_tool_python

st.title("AI Grammar & Spelling Corrector")

tool = language_tool_python.LanguageToolPublicAPI("en-US")

text = st.text_area("Enter your text:")

st.write("Your text:", text)
if st.button("Check Text"):

    if not text.strip():
        st.warning("Please enter some text.")
    else:
        matches = tool.check(text)

        if len(matches) == 0:
            st.success("No grammar or spelling errors found!")
        else:
            st.write("Total errors:", len(matches))

        for i, match in enumerate(matches, start=1):

            with st.expander(f"Error {i} - {match.category}"):
               st.write("Message:", match.message)
               st.write("Suggestions:", ", ".join(match.replacements))

        corrected_text = tool.correct(text)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Text")
            st.write(text)

        with col2:
            st.subheader("Corrected Text")
            st.write(corrected_text)
