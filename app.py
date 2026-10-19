import hashlib
import random
import pandas as pd
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="بيئة التدريب الذكية - مسار التعلم التفاعلي",
    page_icon="🎓",
    layout="wide",
)

# تنسيقات CSS احترافية لتصميم الإنفوجرافيك التفاعلي
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
    </style>
""",
    unsafe_allow_html=True,
)

# العنوان الرئيسي للدراسة
st.title("🎓 خريطة مسار التدريب الإلكتروني القائم على (XAI)")
st.caption(
    "فاعلية أنماط الدعم التكيفية لإنتاج الأنشطة التعليمية الذكية واليقظة"
    " الرقمية والاتجاه نحو بيئة التدريب"
)
st.write("---")

# إدارة الحالة لتحديد المرحلة النشطة
if "current_step" not in st.session_state:
  st.session_state.current_step = (
      "1. مهارات استخدام بيئة التدريب الذكية (XAI)"
  )

# شريط الإنفوجرافيك التفاعلي العلوي
st.subheader("🗺️ خريطة مراحل ومحتوى بيئة التدريب (اختر المرحلة للانتقال):")
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
    st.session_state.current_step = (
        "1. مهارات استخدام بيئة التدريب الذكية (XAI)"
    )

with col2:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-2">2</div>
            <div class="step-title">تصميم الأنشطة واليقظة</div>
            <p style="font-size:12px; color:#7f8c8d;">هندسة الأوامر والفحص النقدي</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("عرض الوحدة 2", key="btn2", use_container_width=True):
    st.session_state.current_step = (
        "2. مهارات تصميم الأنشطة واليقظة الرقمية"
    )

with col3:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-3">3</div>
            <div class="step-title">إنتاج الأنشطة والاتجاه</div>
            <p style="font-size:12px; color:#7f8c8d;">الإنتاج النهائي والتقييم</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("عرض الوحدة 3", key="btn3", use_container_width=True):
    st.session_state.current_step = (
        "3. إنتاج الأنشطة والاتجاه نحو بيئة التدريب"
    )

with col4:
  st.markdown(
      """
        <div class="step-node">
            <div class="step-number num-tool">🤖</div>
            <div class="step-title">أداة NotebookLM</div>
            <p style="font-size:12px; color:#7f8c8d;">المساعد الذكي لبناء المصادر</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("فتح NotebookLM", key="btn4", use_container_width=True):
    st.session_state.current_step = "4. أداة NotebookLM المساندة"

st.write("---")

# ---------------------------------------------------------
# عرض محتوى المرحلة المختارة
# ---------------------------------------------------------

if (
    st.session_state.current_step
    == "1. مهارات استخدام بيئة التدريب الذكية (XAI)"
):
  st.header(
      "📘 الوحدة الأولى: مهارات استخدام بيئة التدريب الذكية وأنماط الدعم"
  )

  st.markdown(
      """
    <div class="content-box">
        <h4>🎯 الشرح المعرفي للوحدة (1):</h4>
        <p>تُعنى هذه الوحدة بتأسيس المعلم مهارياً للتفاعل السلس مع بيئة التدريب الذكية القائمة على الشفافية والتفسير الخوارزمي:</p>
        <ul>
            <li><b>واجهة البيئة والتنقل:</b> استعراض عناصر التحكم وكيفية متابعة الرسوم البيانية المؤشرية لمستوى الأداء.</li>
            <li><b>أنماط الدعم التكيفية:</b> التعرف على كيفية تقديم الدعم المباشر أو الموجه تلقائياً استناداً إلى أداء المعلم.</li>
            <li><b>تفسير القرارات الخوارزمية (XAI):</b> توضيح الأسباب وراء الدرجات والتوصيات بدلاً من النتائج الصماء.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

  col_img, col_chart = st.columns([1, 1])
  with col_img:
    st.subheader("💡 مخطط خطوات التفاعل مع البيئة")
    st.info(
        "1. اختيار الوحدة ⬅️ 2. قراءة الشرح ⬅️ 3. رفع مسودة النشاط ⬅️ 4."
        " تلقي الشرح التفسيري (XAI)"
    )

  with col_chart:
    st.subheader("📊 مؤشرات الاستفادة والسهولة")
    u1_data = pd.DataFrame({
        "المهارة": [
            "سهولة التصفح",
            "استيعاب التغذية الراجعة",
            "التفاعل مع الدعم",
            "المرونة",
        ],
        "النسبة (%)": [92, 88, 85, 90],
    })
    st.bar_chart(u1_data.set_index("المهارة"))

  st.write("---")
  st.subheader("📝 رفع نشاط الوحدة الأولى (Word, PDF, PPTX, Video, Audio)")
  up_1 = st.file_uploader(
      "رفع مسودة خطة الدرس للوحدة الأولى:",
      key="u1",
      type=["docx", "pdf", "pptx", "mp4", "mp3"],
  )

  if up_1 is not None:
    st.success(f"✅ تم رفع وقراءة الملف '{up_1.name}' بنجاح!")
    seed = int(hashlib.md5(up_1.name.encode()).hexdigest(), 16) % 1000
    random.seed(seed)
    s1 = random.randint(82, 97)

    st.subheader("⚡ التقييم والشرح التفسيري (XAI Output)")
    st.metric(
        label="مؤشر إتقان مهارات البيئة", value=f"{s1}%", delta="متقدم جداً"
    )
    with st.expander("🧐 تفاصيل التفسير الخوارزمي:"):
      st.write(
          f"حققت نسبة تفاعل قدرها {s1}% مع أدوات البيئة، مما يدل على استيعاب"
          " عالي لأنماط الدعم المقدمة."
      )

elif (
    st.session_state.current_step == "2. مهارات تصميم الأنشطة واليقظة الرقمية"
):
  st.header(
      "📙 الوحدة الثانية: مهارات صياغة وت
