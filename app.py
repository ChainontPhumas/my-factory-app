# -*- coding: utf-8 -*-
import streamlit as st

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(
    page_title="FAC-WAREHOUSE Solutions",
    page_icon="🏭",
    layout="wide"
)

# --- ฐานข้อมูลจำลองของแพ็คเกจ ---
PACKAGES = [
    {
        "id": "FW01",
        "name": "Compact Warehouse",
        "type": "โกดัง",
        "description": "โกดังขนาดเล็ก เหมาะสำหรับธุรกิจ SME และสต็อกสินค้าทั่วไป",
        "area_sqm": 500,
        "features": ["โครงสร้างเหล็กคุณภาพสูง", "ประตูม้วนไฟฟ้า", "พื้นคอนกรีตขัดมัน"],
        "base_price_per_sqm": 8000,
        "image_url": "https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/02/warehouse-3.jpg" # URL รูปภาพตัวอย่าง
    },
    {
        "id": "FM02",
        "name": "Modern Factory",
        "type": "โรงงาน",
        "description": "โรงงานขนาดกลาง พร้อมพื้นที่สำนักงานและสายการผลิต",
        "area_sqm": 1200,
        "features": ["โครงสร้างเหล็กและคอนกรีต", "ระบบระบายอากาศ", "พื้นที่สำนักงาน 2 ชั้น", "รองรับเครน"],
        "base_price_per_sqm": 11000,
        "image_url": "https://www.constrofacilitator.com/wp-content/uploads/2021/11/Modern-factory.jpg" # URL รูปภาพตัวอย่าง
    },
    {
        "id": "FWL03",
        "name": "Large Logistics Hub",
        "type": "โกดังโลจิสติกส์",
        "description": "ศูนย์กระจายสินค้าขนาดใหญ่ พร้อม Loading Docks และพื้นที่กว้างขวาง",
        "area_sqm": 3000,
        "features": ["Loading Docks 10 จุด", "เพดานสูง 12 เมตร", "ระบบจัดการสต็อกเบื้องต้น"],
        "base_price_per_sqm": 9500,
        "image_url": "https://www.copri-systems.co.uk/wp-content/uploads/2021/04/Telescopic-loading-bays-1024x768.jpeg" # URL รูปภาพตัวอย่าง
    }
]


# --- เมนูด้านข้าง (Sidebar) ---
st.sidebar.title("🏭 FAC-WAREHOUSE Solutions")
menu_choice = st.sidebar.radio(
    "เมนูหลัก:",
    ("ดูแพ็คเกจทั้งหมด", "คำนวณราคาประเมินจากข้อมูลของคุณ", "ขอใบเสนอราคา")
)

# --- การแสดงผลตามเมนูที่เลือก ---

if menu_choice == "ดูแพ็คเกจทั้งหมด":
    st.title("เลือกแบบโรงงานและโกดังที่เหมาะกับคุณ")
    st.markdown("---")

    for pkg in PACKAGES:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(pkg["image_url"], use_column_width=True)
        with col2:
            st.header(f'{pkg["name"]} ({pkg["type"]})')
            st.write(pkg["description"])
            st.info(f"**พื้นที่มาตรฐาน:** {pkg['area_sqm']:,} ตร.ม. | **ราคาเริ่มต้น/ตร.ม.:** {pkg['base_price_per_sqm']:,} บาท")
            st.write("**คุณสมบัติเด่น:**")
            for feature in pkg['features']:
                st.markdown(f"- {feature}")
        st.markdown("---")


elif menu_choice == "คำนวณราคาประเมินจากข้อมูลของคุณ":
    st.title("📝 คำนวณราคาประเมินจากข้อมูลของคุณ")
    st.info("ระบบจะใช้ข้อมูลขนาดพื้นที่ที่คุณเคยบันทึกไว้เพื่อการคำนวณเบื้องต้น")

    # คำนวณพื้นที่ทั้งหมดจากข้อมูลที่บันทึกไว้ (หน่วยเป็น ตร.ม.)
    total_area_sqm = (
        (3.34 * 4.45) + (2.30 * 3.00) + (2.65 * 4.13) + (3.90 * 7.20) +
        (2.40 * 1.80) + (1.80 * 5.10) - (0.60 * 1.80) - (0.60 * 3.00) +
        (1.40 * 1.80) + (1.00 * 0.60) + (1.95 * 2.73) + (1.95 * 2.20) +
        (3.50 * 3.00) + (3.20 * 3.00) + (2.40 * 2.00) + (3.53 * 6.53) +
        (1.00 * 3.00) + (3.00 * 13.80)
    )
    
    st.write(f"**พื้นที่ใช้สอยรวมจากข้อมูลของคุณคือ:** `{total_area_sqm:.2f}` ตารางเมตร")
    
    st.markdown("---")
    
    st.subheader("เลือกประเภทสิ่งก่อสร้างเพื่อใช้ประเมินราคา:")
    
    # สร้าง list ของชื่อแพ็คเกจสำหรับ selectbox
    package_names = [pkg['name'] for pkg in PACKAGES]
    selected_package_name = st.selectbox("เลือกประเภทการก่อสร้าง:", package_names)
    
    # หาข้อมูลแพ็คเกจที่ถูกเลือก
    selected_pkg = next(pkg for pkg in PACKAGES if pkg['name'] == selected_package_name)
    
    if st.button("คำนวณราคาประเมิน"):
        estimated_price = total_area_sqm * selected_pkg['base_price_per_sqm']
        st.success(f"### ราคาประเมินเบื้องต้น: {estimated_price:,.2f} บาท")
        st.balloons()
        st.markdown(f"_(คำนวณจากพื้นที่ `{total_area_sqm:.2f}` ตร.ม. x ราคา/ตร.ม. ของ `{selected_pkg['name']}` ที่ `{selected_pkg['base_price_per_sqm']:,}` บาท)_")
        st.warning("**หมายเหตุ:** ราคาดังกล่าวเป็นการประเมินเบื้องต้นเท่านั้น")


elif menu_choice == "ขอใบเสนอราคา":
    st.title("📧 ขอใบเสนอราคา (Inquiry)")
    st.markdown("กรอกข้อมูลเพื่อให้ทีมงานติดต่อกลับโดยเร็วที่สุด")

    package_names = [pkg['name'] for pkg in PACKAGES]
    
    with st.form("inquiry_form"):
        selected_package = st.selectbox("แพ็คเกจที่สนใจ:", package_names)
        customer_name = st.text_input("ชื่อผู้ติดต่อ:")
        customer_phone = st.text_input("เบอร์โทรศัพท์:")
        customer_email = st.text_input("อีเมล:")
        
        submitted = st.form_submit_button("ส่งข้อมูล")
        
        if submitted:
            if customer_name and customer_phone and customer_email:
                st.success(f"✔️ ส่งข้อมูลเรียบร้อยแล้ว!")
                st.info(f"ขอบคุณ คุณ {customer_name} สำหรับความสนใจในแพ็คเกจ {selected_package} ทีมงานจะรีบติดต่อกลับทางอีเมล {customer_email} หรือเบอร์ {customer_phone} โดยเร็วที่สุด")
            else:
                st.error("กรุณากรอกข้อมูลให้ครบทุกช่อง")
