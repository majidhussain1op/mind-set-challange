import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Sweeper", layout="wide")

st.title("🧹 Data Sweeper App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Original Data")
    st.dataframe(df)

    with st.expander("🛠️ Data Cleaning Options"):
        remove_duplicates = st.checkbox("Remove Duplicates")
        drop_na = st.checkbox("Drop Rows with Missing Values")
        fill_na = st.checkbox("Fill Missing Values")
        normalize_columns = st.checkbox("Normalize Column Names (lowercase, no spaces)")

    if st.button("Clean Data"):
        if remove_duplicates:
            df = df.drop_duplicates()

        if drop_na:
            df = df.dropna()

        if fill_na:
            df = df.fillna("N/A")

        if normalize_columns:
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        st.success("✅ Data cleaned!")
        st.subheader("🧼 Cleaned Data")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Cleaned CSV", data=csv, file_name="cleaned_data.csv", mime="text/csv")

else:
    st.info("Please upload a CSV file to begin.")
