import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. إعدادات الصفحة والهوية
st.set_page_config(page_title="DGN | لوحة العمليات", page_icon="🛡️", layout="wide")

# 2. تصميم الصورة الشخصية
st.markdown("""
    <style>
    .profile-img { display: block; margin: 0 auto; width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 3px solid #D4AF37; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }
    .profile-title { text-align: center; color: #D4AF37; font-weight: 900; margin-top: 10px; font-size: 18px; }
    .profile-subtitle { text-align: center; color: #94A3B8; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (الصورة + كلمة السر)
with st.sidebar:
    st.markdown('<img src="founder_vision.jpg" class="profile-img">', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">مخلد العنزي</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-subtitle">قائد الرحلة | المؤسس</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 🔐 غرفة العمليات")
    password = st.text_input("أدخل كلمة المرور:", type="password")

# 4. التحقق من كلمة السر
if password != "OPS-2026":
    st.warning("🔒 يرجى إدخال كلمة المرور الصحيحة في القائمة الجانبية للدخول.")
    st.stop() 

# 5. غرفة العمليات
st.title("مرحباً بك، مدير العمليات 👋")
st.write(f"📅 تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")
st.divider()

# 6. عرض الطلبات
st.subheader("📦 الطلبات الحالية")
orders_data = {
    "رقم الطلب": ["MRS-8892", "MRS-1023"],
    "اسم الزبون": ["أبو محمد", "بقالة النظيم"],
    "الموقع": ["حي النظيم", "حي النسيم"],
    "الحالة": ["قيد التجهيز", "تم التسليم"],
}
df_orders = pd.DataFrame(orders_data)
st.dataframe(df_orders, use_container_width=True)

st.divider()

# 7. إضافة منتجات جديدة
st.subheader("🔌 إضافة منتج جديد للكتالوج")
with st.form("sync_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        new_p_name = st.text_input("اسم المنتج الجديد*")
        new_p_cat = st.selectbox("التصنيف*", ["بقالة", "مواد غذائية", "بطاقة رقمية"])
    with col_f2:
        new_p_price = st.number_input("السعر (ر.س)*", min_value=1.0, value=25.0)
        
    submitted = st.form_submit_button("🚀 ربط وإضافة المنتج")
    
    if submitted:
        if new_p_name and new_p_price > 0:
            new_row = {'اسم المنتج': new_p_name, 'السعر': new_p_price, 'القطاع': new_p_cat}
            file_path = "Marsad_Valid_Products.csv"
            if os.path.exists(file_path):
                df_existing = pd.read_csv(file_path)
                df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)
            else:
                df_updated = pd.DataFrame([new_row])
            df_updated.to_csv(file_path, index=False, encoding='utf-8-sig')
            st.success(f"✅ تم إضافة المنتج: {new_p_name} بنجاح!")
        else:
            st.warning("⚠️ يرجى إدخال اسم المنتج والسعر.")

st.caption("© 2026 DIGITAL GIFTING NETWORK - لوحة العمليات المركزية")
