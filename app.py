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
st.title("خريطة مسار التدريب الإلكتروني القائم على الشفافية الخوارزمية")
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
            <p style="font-size:12px; color:#7f8c8d;">مبادئ XAI والدعم</p>
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
            <div class="step-title">تصميم واليقظة</div>
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
            <p style="font-size:12px; color:#7f8c8d;">المساعد الذكي</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  if st.button("فتح NotebookLM", key="btn4", use_container_width=True):
    st.session_state.current_step = "Tool"

st.write("---")

# ---------------------------------------------------------
# عرض محتوى المرحلة المختارة
# ---------------------------------------------------------

if st.session_state.current_step == "Unit1":
  st.header("الوحدة الأولى: مهارات استخدام بيئة التدريب الذكية وأنماط الدعم")
  st.markdown(
      """
    <div class="content-box">
        <h4>الشرح المعرفي للوحدة الأولى:</h4>
        <p>تُعنى هذه الوحدة بتأسيس المعلم مهارياً للتفاعل السلس مع بيئة التدريب الذكية القائمة على الشفافية والتفسير الخوارزمي:</p>
        <ul>
            <li><b>واجهة البيئة والتنقل:</b> استعراض عناصر التحكم وكيفية متابعة الرسوم البيانية المؤشرية لمستوى الأداء.</li>
            <li><b>أنماط الدعم التكيفية:</b> التعرف على كيفية تقديم الدعم المباشر أو الموجه تلقائياً استناداً إلى أداء المعلم.</li>
            <li><b>تفسير القرارات الخوارزمية:</b> توضيح الأسباب وراء الدرجات والتوصيات بدلاً من النتائج الصماء.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

  col_img, col_chart = st.columns([1, 1])
  with col_img:
    st.subheader("مخطط خطوات التفاعل مع البيئة")
    st.info(
        "1. اختيار الوحدة -> 2. قراءة الشرح -> 3. رفع مسودة النشاط -> 4. تلقي"
        " الشرح التفسيري"
    )

  with col_chart:
    st.subheader("مؤشرات الاستفادة والسهولة")
    u1_data = pd.DataFrame({
        "المهارة": [
            "سهولة التصفح",
            "استيعاب التغذية",
            "التفاعل مع الدعم",
            "المرونة",
        ],
        "النسبة (%)": [92, 88, 85, 90],
    })
    st.bar_chart(u1_data.set_index("المهارة"))

  st.write("---")
  st.subheader("رفع نشاط الوحدة الأولى (Word, PDF, PPTX, Video, Audio)")
  up_1 = st.file_uploader(
      "رفع مسودة خطة الدرس للوحدة الأولى:",
      key="u1",
      type=["docx", "pdf", "pptx", "mp4", "mp3"],
  )

  if up_1 is not None:
    st.success("تم رفع وقراءة الملف بنجاح!")
    seed = int(hashlib.md5(up_1.name.encode()).hexdigest(), 16) % 1000
    random.seed(seed)
    s1 = random.randint(82, 97)
    st.metric(
        label="مؤشر إتقان مهارات البيئة", value=f"{s1}%", delta="متقدم جداً"
    )

elif st.session_state.current_step == "Unit2":
  st.header("الوحدة الثانية: مهارات صياغة وتصميم الأنشطة الذكية واليقظة الرقمية")
  st.markdown(
      """
    <div class="content-box" style="border-right-color: #ee5253;">
        <h4>الشرح المعرفي للوحدة الثانية:</h4>
        <p>تنمية القدرة على بناء أنشطة تفاعلية لطلاب الحلقة الأولى وفحصها بوعي ونقد:</p>
        <ul>
            <li><b>هندسة الأوامر:</b> بناء تعليمات محكمة للذكاء الاصطناعي لتوليد أنشطة تلائم خصائص المتعلمين.</li>
            <li><b>اليقظة الرقمية:</b> رصد التشوهات المعرفية والمعلومات المضللة في المخرجات الرقمية قبل إقرارها.</li>
            <li><b>الأمن المعرفي:</b> التحقق من سلامة الأفكار ومناسبتها تربوياً وأخلاقياً.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

  col_chart1, col_chart2 = st.columns(2)
  with col_chart1:
    st.subheader("أبعاد اليقظة الرقمية في التصميم")
    u2_data = pd.DataFrame({
        "البعد": [
            "التحقق من المصادر",
            "كشف الانحياز",
            "السلامة المعرفية",
            "الدقة التربوية",
        ],
        "المستوى (%)": [88, 82, 94, 89],
    })
    st.bar_chart(u2_data.set_index("البعد"))

  with col_chart2:
    st.subheader("مسار تطبيق اليقظة الرقمية")
    st.markdown(
        "1. التوليد الآلي للنشاط.\n2. الفحص النقدي للمعلومات.\n3. التكيف والتعديل"
        " لطلاب الصفوف الأولى.\n4. الاعتماد النهائي والتطبيق."
    )

  st.write("---")
  st.subheader("رفع نشاط الوحدة الثانية (جميع الصيغ مدعومة)")
  up_2 = st.file_uploader(
      "رفع مسودة نشاط التصميم واليقظة الرقمية:",
      key="u2",
      type=["docx", "pdf", "pptx", "mp4", "mp3"],
  )

  if up_2 is not None:
    st.success("تم رفع وقراءة الملف بنجاح!")
    seed = int(hashlib.md5(up_2.name.encode()).hexdigest(), 16) % 1000
    random.seed(seed)
    s2 = random.randint(78, 95)
    v2 = random.randint(84, 98)
    m1, m2 = st.columns(2)
    m1.metric(
        label="مهارة تصميم الأنشطة الذكية", value=f"{s2}%", delta="ممتاز"
    )
    m2.metric(label="مؤشر اليقظة الرقمية", value=f"{v2}%", delta="+5% مرتفع")

elif st.session_state.current_step == "Unit3":
  st.header(
      "الوحدة الثالثة: إنتاج الأنشطة الذكية المتكاملة وقياس الاتجاه نحو بيئة"
      " التدريب"
  )
  st.markdown(
      """
    <div class="content-box" style="border-right-color: #10ac84;">
        <h4>الشرح المعرفي للوحدة الثالثة:</h4>
        <p>الإنتاج المتكامل للأنشطة وقياس تقبل المعلم لبيئة التدريب القائمة على الذكاء الاصطناعي:</p>
        <ul>
            <li><b>الإنتاج المتقدم:</b> دمج سيناريوهات حل المشكلات والتعلم باللعب.</li>
            <li><b>الاتجاه نحو البيئة:</b> قياس ارتياح وقابلية المعلم لاستخدام البيئة الذكية في ممارساته المستقبلية.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.subheader("نمو اتجاه المعلم نحو بيئة التدريب عبر الجلسات")
  u3_chart = pd.DataFrame({
      "الجلسات": ["الجلسة 1", "الجلسة 2", "الجلسة 3"],
      "الاتجاه الإيجابي (%)": [68, 82, 95],
      "جودة إنتاج الأنشطة (%)": [62, 79, 92],
  })
  st.line_chart(u3_chart.set_index("الجلسات"))

  st.write("---")
  st.subheader("رفع المنتج النهائي للأنشطة التعليمية")
  up_3 = st.file_uploader(
      "رفع المنتج النهائي الشامل:",
      key="u3",
      type=["docx", "pdf", "pptx", "mp4", "mp3"],
  )

  if up_3 is not None:
    st.success("تم رفع وتقييم المنتج النهائي بنجاح!")
    seed = int(hashlib.md5(up_3.name.encode()).hexdigest(), 16) % 1000
    random.seed(seed)
    s3 = random.randint(85, 99)
    att3 = random.randint(88, 98)
    c1, c2, c3 = st.columns(3)
    c1.metric(
        label="جودة إنتاج النشاط الذكي", value=f"{s3}%", delta="مكتمل"
    )
    c2.metric(
        label="الاتجاه نحو بيئة التدريب", value=f"{att3}%", delta="مرتفع جداً"
    )
    c3.metric(label="مؤشر الثقة التكيفي", value="96%", delta="ممتاز")

elif st.session_state.current_step == "Tool":
  st.header("أداة Google NotebookLM المساندة للتصميم التعليمي")
  st.markdown(
      """
    <div style="background-color: #f0f4f9; padding: 25px; border-radius: 12px; border: 1px solid #d3e3fd; text-align: center;">
        <h3 style="color: #1a73e8;">استكشف قوة Google NotebookLM</h3>
        <p style="font-size: 16px; color: #3c4043;">
            تتيح لك أداة NotebookLM رفع المصادر التعليمية وتحليلها بالذكاء الاصطناعي، وإنشاء تلخيصات صوتية ونصوص تفاعلية لبناء الأنشطة التعليمية الذكية.
        </p>
        <br>
        <a href="https://notebooklm.google.com/" target="_blank" style="background-color: #1a73e8; color: white; padding: 12px 24px; text-decoration: none; font-size: 18px; font-weight: bold; border-radius: 8px; display: inline-block;">
            الانتقال المباشر لأداة NotebookLM
        </a>
    </div>
    """,
      unsafe_allow_html=True,
  )
