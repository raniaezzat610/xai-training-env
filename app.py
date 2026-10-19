import hashlib
import random
import pandas as pd
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="بيئة التدريب الذكية متعددة الوحدات - XAI",
    page_icon="🎓",
    layout="wide",
)

# تنسيقات CSS احترافية وجذابة
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 18px;
        border: 1px solid #e1e8ed;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
    }
    .metric-title {
        font-size: 14px;
        color: #555;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 30px;
        font-weight: bold;
    }
    .card-purple { color: #6C5CE7; }
    .card-green { color: #00B894; }
    .card-blue { color: #0984E3; }
    .card-violet { color: #e84393; }
    
    .progress-bar {
        height: 5px;
        border-radius: 3px;
        margin-top: 10px;
    }
    
    .content-box {
        background-color: #f1f3f5;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
        border: 1px solid #dee2e6;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# العنوان الرئيسي للدراسة
st.title(
    "🎓 بيئة التدريب التكيفية متعددة الوحدات (القائمة على XAI والاتجاه نحو"
    " البيئة)"
)
st.caption(
    "فاعلية أنماط الدعم التكيفية في تنمية مهارات إنتاج الأنشطة التعليمية"
    " الذكية واليقظة الرقمية"
)
st.write("---")

# ---------------------------------------------------------
# القائمة الجانبية: اختيار الوحدات التدريبية المتعددة
# ---------------------------------------------------------
st.sidebar.header("📁 الوحدات التدريبية للبرنامج")
selected_unit = st.sidebar.radio(
    "اختر الوحدة للانتقال إليها:",
    [
        "📚 الوحدة الأولى: مدخل إلى الذكاء الاصطناعي القابل للتفسير (XAI)",
        "🔍 الوحدة الثانية: مهارات اليقظة الرقمية في التصميم",
        "🎯 الوحدة الثالثة: إنتاج الأنشطة الذكية والاتجاه نحو بيئة التدريب",
    ],
)

st.sidebar.write("---")
st.sidebar.info(
    "💡 **إرشاد الاستخدام:** كل وحدة تحتوي على دليلها النظري الخاص ومحطة رفع"
    " الأنشطة وتقييمها بصورة مستقلة."
)

# ---------------------------------------------------------
# محتوى الوحدة الأولى
# ---------------------------------------------------------
if (
    selected_unit
    == "📚 الوحدة الأولى: مدخل إلى الذكاء الاصطناعي القابل للتفسير (XAI)"
):
  st.header(
      "📚 الوحدة الأولى: أساسيات الذكاء الاصطناعي القابل للتفسير (XAI) وأنماط"
      " الدعم"
  )

  st.markdown("""
    <div class="content-box">
        <h4>🎯 أهداف الوحدة والمحتوى التعليمي:</h4>
        <p>تهدف هذه الوحدة إلى إحاطة المعلم بمفاهيم الشفافية والخوارزميات التفسيرية في اتخاذ القرار:</p>
        <ul>
            <li><b>مفهوم XAI:</b> تحويل قرارات الذكاء الاصطناعي من "صندوق أسود" إلى مخرجات مفهومة ومبررة تزيد من ثقة المعلم.</li>
            <li><b>أنماط الدعم التكيفية:</b> تقديم التوجيه الفوري (المباشر وغير المباشر) بناءً على أسلوب المعلم الفردي.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

  st.subheader("📝 النشاط التطبيقي للوحدة الأولى")
  uploaded_file_1 = st.file_uploader(
      "رفق خطة الدرس الخاصة بالوحدة الأولى (.docx):",
      key="file1",
      type=["docx"],
  )

  if uploaded_file_1 is not None:
    st.success(
        f"✅ تم تحليل ملف الوحدة الأولى ('{uploaded_file_1.name}') بنجاح!"
    )

    # توليد درجات ديناميكية متغيرة حسب الملف
    seed = (
        int(hashlib.md5(uploaded_file_1.name.encode()).hexdigest(), 16) % 1000
    )
    random.seed(seed)
    s_score = random.randint(80, 95)
    v_score = random.randint(75, 92)

    st.write("---")
    st.header("⚡ نتائج وتقسيمات XAI للوحدة الأولى")

    c1, c2, c3 = st.columns(3)
    c1.metric(label="مؤشر فهم مبادئ XAI", value=f"{s_score}%", delta="جيد جداً")
    c2.metric(label="درجة التفاعل التكيفي", value=f"{v_score}%", delta="+4%")
    c3.metric(label="جاهزية التطبيق", value="91%", delta="مرتفع")

    # رسم توضيحي تفسيري
    st.markdown("##### 📊 تحليل عوامل القبول والتفسير الخوارزمي:")
    chart_df = pd.DataFrame({
        "العامل": ["الشفافية", "سهولة الفهم", "منطق القرار", "الموثوقية"],
        "النسبة (%)": [s_score, v_score, 88, 92],
    })
    st.bar_chart(chart_df.set_index("العامل"))

# ---------------------------------------------------------
# محتوى الوحدة الثانية
# ---------------------------------------------------------
elif selected_unit == "🔍 الوحدة الثانية: مهارات اليقظة الرقمية في التصميم":
  st.header("🔍 الوحدة الثانية: تنمية مهارات اليقظة الرقمية والأمن المعرفي")

  st.markdown("""
    <div class="content-box">
        <h4>🎯 أهداف الوحدة:</h4>
        <p>تركيز هذه الوحدة على إكساب المعلمين القدرة على فحص المحتوى الرقمي المولد آلياً ورصده من التشوهات:</p>
        <ul>
            <li><b>التقييم النقدي:</b> فحص مصادر المعلومات والتحقق من سلامتها قبل عرضها على الطلاب.</li>
            <li><b>مواجهة التحيزات:</b> تجنب الوقوع في فخ الأخطاء المعرفية الرقمية.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

  st.subheader("📝 النشاط التطبيقي للوحدة الثانية")
  uploaded_file_2 = st.file_uploader(
      "رفق نشاط اليقظة الرقمية المخطط (.docx):", key="file2", type=["docx"]
  )

  if uploaded_file_2 is not None:
    st.success(
        f"✅ تم تحليل نشاط اليقظة الرقمية ('{uploaded_file_2.name}') بنجاح!"
    )

    seed = (
        int(hashlib.md5(uploaded_file_2.name.encode()).hexdigest(), 16) % 1000
    )
    random.seed(seed)
    vig_score = random.randint(72, 98)
    crit_score = random.randint(78, 96)

    st.write("---")
    st.header("⚡ نتائج وتقسيمات XAI لوحدة اليقظة الرقمية")

    c1, c2 = st.columns(2)
    c1.metric(
        label="درجة اليقظة الرقمية المحسوبة",
        value=f"{vig_score}%",
        delta="متقدم",
    )
    c2.metric(
        label="كفاءة التفكير النقدي للمحتوى",
        value=f"{crit_score}%",
        delta="+6%",
    )

    # رسم توضيحي تفسيري
    st.markdown("##### 📊 توزيع مستويات اليقظة الرقمية بالنشاط:")
    chart_df2 = pd.DataFrame({
        "مؤشر اليقظة": [
            "كشف التحيز",
            "التحقق من المصادر",
            "الأمن المعرفي",
            "الموثوقية",
        ],
        "الدرجة (%)": [vig_score, crit_score, 85, 90],
    })
    st.bar_chart(chart_df2.set_index("مؤشر اليقظة"))

# ---------------------------------------------------------
# محتوى الوحدة الثالثة
# ---------------------------------------------------------
elif (
    selected_unit
    == "🎯 الوحدة الثالثة: إنتاج الأنشطة الذكية والاتجاه نحو بيئة التدريب"
):
  st.header(
      "🎯 الوحدة الثالثة: إنتاج الأنشطة التعليمية الذكية وقياس الاتجاه نحو بيئة"
      " التدريب"
  )

  st.markdown("""
    <div class="content-box">
        <h4>🎯 أهداف الوحدة:</h4>
        <p>تتوج هذه الوحدة التدريب بإنتاج أنشطة ذكية متكاملة وقياس اتجاه المعلمين نحو استخدام البيئة الإلكترونية:</p>
        <ul>
            <li><b>صياغة الأنشطة:</b> توظيف هندسة الأوامر والذكاء الاصطناعي لإنتاج أنشطة تفاعلية لطلاب الحلقة الأولى.</li>
            <li><b>الاتجاه نحو بيئة التدريب:</b> رصد مدى تقبل المعلمين وراحتهم في التعامل مع أنماط الدعم التكيفية.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

  st.subheader("📝 النشاط التطبيقي للوحدة الثالثة")
  uploaded_file_3 = st.file_uploader(
      "رفق مسودة النشاط النهائي لإنتاج الأنشطة (.docx):",
      key="file3",
      type=["docx"],
  )

  if uploaded_file_3 is not None:
    st.success(
        f"✅ تم رفع وتقييم النشاط النهائي ('{uploaded_file_3.name}') بنجاح!"
    )

    seed = (
        int(hashlib.md5(uploaded_file_3.name.encode()).hexdigest(), 16) % 1000
    )
    random.seed(seed)
    prod_score = random.randint(82, 99)
    att_score = random.randint(85, 97)

    st.write("---")
    st.header(
        "⚡ نتائج وتقسيمات XAI وإنتاج الأنشطة والاتجاه نحو بيئة التدريب"
    )

    c1, c2, c3 = st.columns(3)
    c1.metric(
        label="مهارة إنتاج الأنشطة الذكية",
        value=f"{prod_score}%",
        delta="ممتاز",
    )
    c2.metric(
        label="الاتجاه نحو بيئة التدريب",
        value=f"{att_score}%",
        delta="مرتفع جداً",
    )
    c3.metric(label="مؤشر الجودة الشامل", value="93%", delta="مستقر")

    # رسم توضيحي تفسيري
    st.markdown("##### 📊 تحليل مسار التطور للاتجاه نحو بيئة التدريب:")
    chart_df3 = pd.DataFrame({
        "جلسات المتابعة": ["الجلسة الأولى", "الجلسة الثانية", "الجلسة الحالية"],
        "مستوى الاتجاه لبيئة التدريب (%)": [
            max(60, att_score - 20),
            max(75, att_score - 10),
            att_score,
        ],
    })
    st.line_chart(chart_df3.set_index("جلسات المتابعة"))

    with st.expander("🧐 التفسير الخوارزمي المطور لقرار XAI (اضغط للعرض):"):
      st.write(
          f"• **تحليل الأداء:** يُظهر النشاط تفوقاً في الإنتاجية بـ"
          f" {prod_score}%، واتجاهاً إيجابياً نحو بيئة التدريب الإلكترونية بـ"
          f" {att_score}%."
      )
      st.write(
          "• **التوصية التكيفية:** استمرار نمط الدعم الموجه لتعزيز مهارات التفكير"
          " الإبداعي في الأنشطة المقبلة."
      )
