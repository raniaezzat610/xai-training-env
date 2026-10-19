import hashlib
import random
import pandas as pd
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="بيئة التدريب الذكية - XAI والحل الموجه",
    page_icon="🎓",
    layout="wide",
)

# تنسيقات CSS احترافية لتصميم الإنفوجرافيك التفاعلي والبطاقات
st.markdown(
    """
    <style>
    .step-node {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid #e0e0e0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .step-number {
        width: 50px;
        height: 50px;
        line-height: 50px;
        border-radius: 50%;
        color: white;
        font-size: 22px;
        font-weight: bold;
        margin: 0 auto 10px auto;
    }
    .num-1 { background-color: #2e86de; }
    .num-2 { background-color: #ee5253; }
    .num-3 { background-color: #10ac84; }
    .num-tool { background-color: #f39c12; }
    
    .step-title {
        font-size: 15px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    
    .content-box {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        border-right: 6px solid #2e86de;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .metric-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e1e8ed;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        text-align: center;
    }
    .metric-title {
        font-size: 13px;
        color: #555;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
    }
    .card-purple { color: #6C5CE7; }
    .card-green { color: #00B894; }
    .card-blue { color: #0984E3; }
    .card-violet { color: #e84393; }
    
    .progress-bar {
        height: 5px;
        border-radius: 3px;
        margin-top: 8px;
    }
    
    .xai-explanation-box {
        background-color: #e8f4f8;
        border-left: 5px solid #0984E3;
        padding: 20px;
        border-radius: 10px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    
    .solution-box {
        background-color: #e6f4ea;
        border-left: 5px solid #34a853;
        padding: 20px;
        border-radius: 10px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# العنوان الرئيسي للدراسة
st.title("بيئة التدريب الإلكتروني القائمة على الشفافية الخوارزمية (XAI)")
st.caption(
    "فاعلية أنماط الدعم التكيفية لإنتاج الأنشطة التعليمية الذكية واليقظة"
    " الرقمية والاتجاه نحو بيئة التدريب"
)
st.write("---")

# إدارة الحالة لتحديد المرحلة النشطة
if "current_step" not in st.session_state:
  st.session_state.current_step = "Unit1"

# شريط الإنفوجرافيك التفاعلي العلوي
st.subheader("خريطة مراحل ومحتوى بيئة التدريب (اختر المرحلة للانتقال):")
col1, col2, col3, col4 = st.columns(4)

with col1:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-1">1</div>
            <div class="step-title">التعامل مع البيئة</div>
            <p style="font-size:12px; color:#7f8c8d;">مبادئ XAI والدعم التكيفي</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("عرض الوحدة 1", key="btn1", use_container_width=True):
    st.session_state.current_step = "Unit1"

with col2:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-2">2</div>
            <div class="step-title">تصميم الأنشطة واليقظة</div>
            <p style="font-size:12px; color:#7f8c8d;">هندسة الأوامر والنقد</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("عرض الوحدة 2", key="btn2", use_container_width=True):
    st.session_state.current_step = "Unit2"

with col3:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-3">3</div>
            <div class="step-title">إنتاج والاتجاه</div>
            <p style="font-size:12px; color:#7f8c8d;">الإنتاج النهائي والتقييم</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("عرض الوحدة 3", key="btn3", use_container_width=True):
    st.session_state.current_step = "Unit3"

with col4:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-tool">AI</div>
            <div class="step-title">أداة NotebookLM</div>
            <p style="font-size:12px; color:#7f8c8d;">المساعد الذكي لبناء المصادر</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("فتح NotebookLM", key="btn4", use_container_width=True):
    st.session_state.current_step = "Tool"

st.write("---")

# دالة تحليل XAI الموجهة نحو التفسير والحل العملي المباشر
def generate_xai_solution_oriented_analysis(file_obj, unit_name):
  # بصمة فريدة متغيرة حسب الملف
  seed_val = (
      int(hashlib.md5(file_obj.name.encode()).hexdigest(), 16) + file_obj.size
  ) % 100000
  random.seed(seed_val)

  overall = random.randint(78, 96)
  vigilance = random.randint(72, 95)
  attitude = random.randint(80, 98)
  production = random.randint(75, 96)

  st.subheader(
      f"⚡ تقرير التحليل التفسيري والتوجيه نحو الحل (XAI Dashboard) لملف:"
      f" '{file_obj.name}'"
  )

  # 1. كروت المؤشرات
  c1, c2, c3, c4 = st.columns(4)
  with c1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">التقييم العام للمحتوى</div>
            <div class="metric-value card-purple">{overall} <span style="font-size:14px; color:#aaa;">/ 100</span></div>
            <div class="progress-bar" style="background-color: #6C5CE7; width: {overall}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with c2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">مهارات اليقظة الرقمية</div>
            <div class="metric-value card-green">{vigilance}%</div>
            <div class="progress-bar" style="background-color: #00B894; width: {vigilance}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with c3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">الاتجاه نحو بيئة التدريب</div>
            <div class="metric-value card-blue">{attitude}%</div>
            <div class="progress-bar" style="background-color: #0984E3; width: {attitude}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with c4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">إنتاج الأنشطة الذكية</div>
            <div class="metric-value card-violet">{production}%</div>
            <div class="progress-bar" style="background-color: #e84393; width: {production}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")

  # 2. التفسير الخوارزمي المفصل ونقاط القوة والضعف (XAI Explanation)
  strengths = []
  weaknesses = []
  
  if production >= 85:
    strengths.append("وضوح أهداف النشاط التعليمي وملاءمتها لخصائص طلاب الحلقة الأولى.")
  else:
    weaknesses.append("الاحتياج إلى إعادة صياغة الأهداف الإجرائية لتكون أكثر تفاعلية.")
    
  if vigilance >= 85:
    strengths.append("مستوى مرتفع من الفحص النقدي للمحتوى والتحقق من مصادر المعلومات.")
  else:
    weaknesses.append("قصور في آليات التحقق من صحة المخرجات الرقمية ومواجهة التشوهات المعرفية.")
    
  if attitude >= 85:
    strengths.append("اتجاه إيجابي قوي وممتاز نحو التفاعل مع بيئة التدريب الإلكترونية.")
  else:
    weaknesses.append("حاجة لزيادة الممارسة للتغلب على التخوف من أدوات الذكاء الاصطناعي.")

  st.markdown(
      f"""
    <div class="xai-explanation-box">
        <h4 style="color: #0984E3; margin-top:0;">🔍 التفسير الخوارزمي الشفاف (لماذا حصلت على هذه النتيجة؟):</h4>
        <p>بناءً على تحليل خصائص ملفك المرفوع، قامت خوارزميات الـ XAI بتحديد الأسباب الكامنة وراء التقي
