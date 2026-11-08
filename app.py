import streamlit as st

st.set_page_config(page_title="مرصد", page_icon="🛡️")

st.title("🦅 مرحباً بك في مرصد الرقمي")
st.subheader("منصة التوريد الرقمي الذكي")

st.write("المنصة تعمل الآن بشكل مستقر ومباشر!")
st.write("هذه هي النسخة الأولى (Demo) على سيرفرات Streamlit الدائمة.")

# زر تجريبي
if st.button("🛒 اطلب الآن"):
    st.success("تم تجهيز الطلب!")
