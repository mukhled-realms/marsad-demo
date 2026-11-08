import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة والهوية
st.set_page_config(page_title="DGN | لوحة العمليات", page_icon="🛡️", layout="wide")

# 2. إعدادات الأمان (كلمة سر ولد عمك)
OPS_PASSWORD = "OPS-2026"  # كلمة السر الخاصة بغرفة العمليات

# 3. تصميم الهوية (Dark Luxury)
st.markdown("""
    <style>
    .main-title { text-align: center; font-size: 28px; font-weight: 900; color: #D4AF37; margin-bottom: 20px; }
    .stButton>button { background-color: #D4AF37; color: #0A2540; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 4. نظام تسجيل الدخول
st.sidebar.title("🛡️ DGN Control")
password = st.sidebar.text_input("أدخل كلمة مرور غرفة العمليات:", type="password")

if password != OPS_PASSWORD:
    st.warning("🔒 يرجى إدخال كلمة المرور الصحيحة في القائمة الجانبية للدخول إلى غرفة العمليات.")
    st.stop() # إيقاف تحميل باقي الصفحة حتى يتم إدخال كلمة السر

# 5. غرفة العمليات (تظهر فقط بعد إدخال كلمة السر)
st.markdown('<h1 class="main-title">مرحباً بك، مدير العمليات 👋</h1>', unsafe_allow_html=True)
st.write(f"📅 تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")
st.divider()

# 6. بيانات تجريبية (في المستقبل سنربطها بقاعدة بيانات حقيقية)
st.subheader("📦 الطلبات الحالية")
orders_data = {
    "رقم الطلب": ["MRS-8892", "MRS-1023"],
    "اسم الزبون": ["أبو محمد", "بقالة النظيم"],
    "الموقع": ["حي النظيم", "حي النسيم"],
    "الطلب": ["2 روبلوكس 1000", "1 بطاقة ستيم"],
    "الحالة": ["قيد التجهيز", "تم التسليم"],
}
df = pd.DataFrame(orders_data)
st.dataframe(df, use_container_width=True)

st.divider()

# 7. إحصائيات سريعة
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي الطلبات", "25", "5 جديدة")
col2.metric("الطلبات المكتملة", "20")
col3.metric("الطلبات المعلقة", "5")

st.divider()
st.subheader("🗺️ خريطة التوصيل")
st.write("(سيتم عرض الخريطة التفاعلية هنا)")
# يمكنك إضافة كود الخريطة (Folium) هنا لاحقاً

st.caption("© 2026 DIGITAL GIFTING NETWORK - لوحة العمليات المركزية")
