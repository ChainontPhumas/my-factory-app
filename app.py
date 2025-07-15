# -*- coding: utf-8 -*-
import streamlit as st
import json

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(
    page_title="INC Technology Limited - Future Tech Solutions",
    page_icon="🚀",
    layout="wide"
)

# --- Theme Management ---
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# CSS Styles for Light/Dark Theme
def apply_theme():
    if st.session_state.theme == 'dark':
        st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
        }
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        }
        .hero-title {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(45deg, #00d4ff, #0099cc, #0066ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 2rem 0;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }
        .tech-card {
            background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
            transition: all 0.3s ease;
        }
        .tech-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.2);
            border-color: rgba(0, 212, 255, 0.6);
        }
        .neon-text {
            color: #00d4ff;
            text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff, 0 0 30px #00d4ff;
        }
        .contact-info {
            background: rgba(0, 212, 255, 0.1);
            border-left: 4px solid #00d4ff;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 8px;
        }
        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 999;
            background: rgba(0, 212, 255, 0.2);
            border: 1px solid #00d4ff;
            border-radius: 50px;
            padding: 10px 20px;
            color: #00d4ff;
            cursor: pointer;
        }
        .service-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        .pulse {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0, 212, 255, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(0, 212, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 212, 255, 0); }
        }
        </style>
        """, unsafe_allow_html=True)
    else:  # light theme
        st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333333;
        }
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        .hero-title {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 2rem 0;
        }
        .tech-card {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(102, 126, 234, 0.3);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
            transition: all 0.3s ease;
        }
        .tech-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
            border-color: rgba(102, 126, 234, 0.6);
        }
        .neon-text {
            color: #667eea;
            font-weight: bold;
        }
        .contact-info {
            background: rgba(102, 126, 234, 0.1);
            border-left: 4px solid #667eea;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 8px;
        }
        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 999;
            background: rgba(102, 126, 234, 0.2);
            border: 1px solid #667eea;
            border-radius: 50px;
            padding: 10px 20px;
            color: #667eea;
            cursor: pointer;
        }
        </style>
        """, unsafe_allow_html=True)

# Apply theme
apply_theme()

# Theme Toggle in Sidebar
with st.sidebar:
    st.markdown("### 🎨 Theme Settings")
    if st.button("🌙 Dark Theme" if st.session_state.theme == 'light' else "☀️ Light Theme"):
        st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
        st.rerun()

# --- Company Data ---
COMPANY_INFO = {
    "name_th": "บริษัท ไอเอ็นซี เทคโนโลยี จำกัด",
    "name_en": "INC Technology Limited",
    "address": "126/260 ซ.รามอินทรา 40 ถ.รามอินทรา แขวงคลองกุ่ม เขตบึงกุ่ม กรุงเทพฯ 10230",
    "tel": "+66 0.2509.1264",
    "mobile": "+66 0.81856.9812",
    "fax": "+66 0.2509.1631",
    "email": "incscada@gmail.com",
    "contact_person": "คุณชาญณรงค์ชัย ภูมาศ"
}

# --- Technology Services ---
TECH_SERVICES = [
    {
        "id": "SCADA01",
        "name": "SCADA Systems",
        "icon": "🖥️",
        "description": "ระบบควบคุมและเก็บข้อมูลอัตโนมัติ สำหรับการจัดการโรงงานและอุตสาหกรรม",
        "features": ["Real-time Monitoring", "Data Analytics", "Remote Control", "Alarm Management"],
        "technologies": ["HMI", "PLC Integration", "Cloud Computing", "IoT Sensors"]
    },
    {
        "id": "AUTO02", 
        "name": "Industrial Automation",
        "icon": "🤖",
        "description": "ระบบอัตโนมัติสำหรับอุตสาหกรรม เพิ่มประสิทธิภาพและลดต้นทุนการดำเนินงาน",
        "features": ["Process Automation", "Quality Control", "Predictive Maintenance", "Energy Management"],
        "technologies": ["AI/ML", "Robotics", "Digital Twins", "Edge Computing"]
    },
    {
        "id": "IOT03",
        "name": "IoT Solutions",
        "icon": "🌐",
        "description": "เชื่อมต่ออุปกรณ์และเครื่องจักรเข้าสู่ระบบอัจฉริยะเพื่อการบริหารจัดการที่ดีขึ้น",
        "features": ["Smart Sensors", "Data Collection", "Real-time Analytics", "Mobile Monitoring"],
        "technologies": ["LoRaWAN", "NB-IoT", "WiFi 6", "Bluetooth 5.0"]
    },
    {
        "id": "CYBER04",
        "name": "Cybersecurity",
        "icon": "🔒",
        "description": "ป้องกันระบบอุตสาหกรรมจากภัยคุกคามทางไซเบอร์ด้วยเทคโนโลยีล้ำสมัย",
        "features": ["Network Security", "Endpoint Protection", "Threat Detection", "Incident Response"],
        "technologies": ["AI Security", "Zero Trust", "Blockchain", "Quantum Encryption"]
    }
]

# --- เมนูด้านข้าง ---
st.sidebar.markdown(f"""
<div style="text-align: center; padding: 2rem;">
    <h1 style="color: {'#00d4ff' if st.session_state.theme == 'dark' else '#667eea'};">🚀 INC Tech</h1>
    <p style="color: {'#ffffff' if st.session_state.theme == 'dark' else '#333333'};">Future Technology Solutions</p>
</div>
""", unsafe_allow_html=True)

menu_choice = st.sidebar.radio(
    "🔧 Navigation:",
    ("🏠 Home", "💼 Services", "📊 Solutions", "📧 Contact")
)

# --- Main Content ---
if menu_choice == "🏠 Home":
    # Hero Section
    st.markdown(f"""
    <div class="hero-title">
        {COMPANY_INFO['name_en']}
    </div>
    <div style="text-align: center; margin-bottom: 3rem;">
        <h2 class="neon-text">🚀 Pioneering the Future of Industrial Technology</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            Transforming industries through cutting-edge automation, IoT, and intelligent systems
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Company Overview
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="tech-card pulse">
            <h3 class="neon-text">🏢 About INC Technology</h3>
            <p>We are a leading technology company specializing in industrial automation, SCADA systems, and IoT solutions. 
            Our mission is to revolutionize industrial processes through innovative technology and exceptional service.</p>
            <div style="display: flex; justify-content: space-around; margin-top: 2rem;">
                <div style="text-align: center;">
                    <h4 class="neon-text">50+</h4>
                    <p>Projects Completed</p>
                </div>
                <div style="text-align: center;">
                    <h4 class="neon-text">15+</h4>
                    <p>Years Experience</p>
                </div>
                <div style="text-align: center;">
                    <h4 class="neon-text">100%</h4>
                    <p>Client Satisfaction</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif menu_choice == "💼 Services":
    st.markdown('<h1 class="hero-title">Our Technology Services</h1>', unsafe_allow_html=True)
    
    for i, service in enumerate(TECH_SERVICES):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"""
            <div class="tech-card" style="text-align: center; height: 300px; display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 4rem;">{service['icon']}</div>
                <h3 class="neon-text">{service['name']}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="tech-card">
                <h3>{service['name']}</h3>
                <p>{service['description']}</p>
                <h4 class="neon-text">Key Features:</h4>
                <ul>
                    {''.join([f'<li>{feature}</li>' for feature in service['features']])}
                </ul>
                <h4 class="neon-text">Technologies:</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {''.join([f'<span style="background: rgba(0,212,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;">{tech}</span>' for tech in service['technologies']])}
                </div>
            </div>
            """, unsafe_allow_html=True)

elif menu_choice == "📊 Solutions":
    st.markdown('<h1 class="hero-title">Technology Solutions</h1>', unsafe_allow_html=True)
    
    # Interactive Solution Calculator
    st.markdown("""
    <div class="tech-card">
        <h3 class="neon-text">🔧 Solution Calculator</h3>
        <p>Get a preliminary assessment for your technology needs</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        industry_type = st.selectbox(
            "🏭 Industry Type:",
            ["Manufacturing", "Energy & Utilities", "Oil & Gas", "Food & Beverage", "Pharmaceutical", "Automotive"]
        )
        
        project_size = st.selectbox(
            "📏 Project Scale:",
            ["Small (1-10 devices)", "Medium (11-50 devices)", "Large (51-200 devices)", "Enterprise (200+ devices)"]
        )
    
    with col2:
        automation_level = st.slider("🤖 Automation Level (%)", 0, 100, 50)
        timeline = st.selectbox(
            "⏱️ Implementation Timeline:",
            ["1-3 months", "3-6 months", "6-12 months", "12+ months"]
        )
    
    if st.button("🚀 Calculate Solution", type="primary"):
        # Simple calculation logic
        base_cost = {"Small": 500000, "Medium": 2000000, "Large": 5000000, "Enterprise": 15000000}
        size_key = project_size.split(" ")[0]
        estimated_cost = base_cost.get(size_key, 1000000) * (1 + automation_level/100)
        
        st.success(f"""
        ### 💰 Estimated Investment: ฿{estimated_cost:,.0f}
        
        **Project Details:**
        - Industry: {industry_type}
        - Scale: {project_size}
        - Automation Level: {automation_level}%
        - Timeline: {timeline}
        
        *This is a preliminary estimate. Contact us for a detailed proposal.*
        """)
        st.balloons()

elif menu_choice == "📧 Contact":
    st.markdown('<h1 class="hero-title">Contact Us</h1>', unsafe_allow_html=True)
    
    # Company Information
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="tech-card">
            <h3 class="neon-text">🏢 {COMPANY_INFO['name_th']}</h3>
            <h4>{COMPANY_INFO['name_en']}</h4>
            
            <div class="contact-info">
                <h4>📍 Address</h4>
                <p>{COMPANY_INFO['address']}</p>
            </div>
            
            <div class="contact-info">
                <h4>📞 Contact Information</h4>
                <p><strong>Tel:</strong> {COMPANY_INFO['tel']}</p>
                <p><strong>Mobile:</strong> {COMPANY_INFO['mobile']}</p>
                <p><strong>Fax:</strong> {COMPANY_INFO['fax']}</p>
                <p><strong>Email:</strong> {COMPANY_INFO['email']}</p>
            </div>
            
            <div class="contact-info">
                <h4>👤 Contact Person</h4>
                <p><strong>{COMPANY_INFO['contact_person']}</strong></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-card">
            <h3 class="neon-text">🚀 Quick Contact</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact Form
        with st.form("contact_form"):
            name = st.text_input("👤 Your Name:")
            email = st.text_input("📧 Email:")
            phone = st.text_input("📱 Phone:")
            service_interest = st.selectbox(
                "🔧 Service of Interest:",
                [service['name'] for service in TECH_SERVICES]
            )
            message = st.text_area("💬 Message:")
            
            submitted = st.form_submit_button("🚀 Send Message", type="primary")
            
            if submitted:
                if name and email and phone:
                    st.success("✅ Message sent successfully!")
                    st.info(f"""
                    Thank you, **{name}**! 
                    
                    We've received your inquiry about **{service_interest}**.
                    Our team will contact you at **{email}** or **{phone}** within 24 hours.
                    """)
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")

# Footer
st.markdown("""
<div style="text-align: center; padding: 3rem 0 1rem 0; border-top: 1px solid rgba(0,212,255,0.3); margin-top: 3rem;">
    <p style="color: #888;">© 2024 INC Technology Limited. Powered by Future Tech Solutions 🚀</p>
</div>
""", unsafe_allow_html=True)
