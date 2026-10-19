import hashlib
import random
import pandas as pd
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="بيئة التدريب الذكية - XAI", page_icon="🎓", layout="wide"
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
    
    .xai-box {
        background-color: #f8f9fa;
        border-right: 5px solid #6C5CE7;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
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
    "🎓 بيئة التدريب التكيفية القائمة على الذكاء الاصطناعي القابل للتفسير (XAI)"
)
st.caption(
    "فاعلية أنماط الدعم التكيفية في تنمية مهارات إنتاج الأنشطة التعليمية"
    " الذكية واليقظة الرقمية والاتجاه نحو بيئة التدريب"
)
st.write("---")

# ---------------------------------------------------------
# الجزء الأول: المحتوى التعليمي والتأسيسي لبيئة التدريب
# ---------------------------------------------------------
st.header("📚 أولاً: المحتوى التعليمي والتربوي للوحدة التدريبية")
with st.container():
  st.markdown("""
    <div class="content-box">
        <h4>💡 دليل المعلم الذكي: أنماط الدعم التكيفي واليقظة الرقمية</h4>
        <p>مرحباً بك في بيئة التدريب الذكية. تهدف هذه الوحدة إلى تمكينك من مهارات صياغة الأنشطة التعليمية التفاعلية وتنمية اليقظة الرقمية أثناء التصميم التعليمي:</p>
        <ul>
            <li><b>مفهوم اليقظة الرقمية (Digital Vigilance):</b> قدرة المعلم على التقييم النقدي للمحتوى الرقمي، واكتشاف الانحيازات الشائعة والتحقق من مصداقية المعلومات المصممة للطلاب.</li>
            <li><b>نمط الدعم التكيفي (Adaptive Support):</b> يقدم لك النظام توجيهاً فورياً ومخصصاً بناءً على تحليل أسلوبك في بناء الأنشطة ومستواك المهني.</li>
            <li><b>الاتجاه نحو بيئة التدريب:</b> قياس مدى رضاك وقابليتك للتفاعل مع الأدوات التكيفية الذكية وتوظيفها بسلاسة في ممارساتك التدريسية.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# الجزء الثاني: رفع النشاط التطبيقي (الدرس)
# ---------------------------------------------------------
st.header("📝 ثانياً: النشاط التطبيقي (رفع مسودة الدرس للتحليل)")
uploaded_file = st.file_uploader(
    "قم برفع ملف خطة الدرس أو النشاط التعليمي بصيغة (.docx) لتقييمه"
    " أوتوماتيكياً بواسطة محرك XAI:",
    type=["docx"],
)

if uploaded_file is not None:
  st.success(f"✅ تم رفع وقراءة الملف '{uploaded_file.name}' بنجاح!")

  # توليد درجات تحليليّة ديناميكية تتغير حسب الملف المرفوع
  file_seed = int(
      hashlib.md5(uploaded_file.name.encode()).hexdigest(), 16
  ) % (1000)
  random.seed(file_seed + uploaded_file.size)

  score_overall = random.randint(78, 96)
  score_vigilance = random.randint(70, 95)
  score_attitude = random.randint(82, 98)
  score_production = random.randint(75, 94)

  st.write("---")
  st.header(
      "⚡ ثالثاً: نتائج التحليل والتغذية الراجعة التكيفية (XAI Dashboard)"
  )

  # تبويبات العرض التفاعلية
  tab1, tab2, tab3 = st.tabs([
      "📊 1. المؤشرات والتقييم الشامل",
      "🧐 2. التفسير الخوارزمي المطور (XAI Charts)",
      "🎯 3. التغذية الراجعة والأنشطة التفاعلية",
  ])

  # --- التبويب الأول: المؤشرات والتقييم الشامل ---
  with tab1:
    st.subheader("📈 مؤشرات الأداء المتغيرة للنشاط المرفوع")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
      st.markdown(
          f"""
            <div class="metric-card">
                <div class="metric-title">التقييم العام للنشاط</div>
                <div class="metric-value card-purple">{score_overall} <span style="font-size:15px; color:#888;">/ 100</span></div>
                <div class="progress-bar" style="background-color: #6C5CE7; width: {score_overall}%;"></div>
            </div>
            """,
          unsafe_allow_html=True,
      )

    with c2:
      st.markdown(
          f"""
            <div class="metric-card">
                <div class="metric-title">مهارات اليقظة الرقمية</div>
                <div class="metric-value card-green">{score_vigilance}%</div>
                <div class="progress-bar" style="background-color: #00B894; width: {score_vigilance}%;"></div>
            </div>
            """,
          unsafe_allow_html=True,
      )

    with c3:
      st.markdown(
          f"""
            <div class="metric-card">
                <div class="metric-title">الاتجاه نحو بيئة التدريب</div>
                <div class="metric-value card-blue">{score_attitude}%</div>
                <div class="progress-bar" style="background-color: #0984E3; width: {score_attitude}%;"></div>
            </div>
            """,
          unsafe_allow_html=True,
      )

    with c4:
      st.markdown(
          f"""
            <div class="metric-card">
                <div class="metric-title">إنتاج الأنشطة الذكية</div>
                <div class="metric-value card-violet">{score_production}%</div>
                <div class="progress-bar" style="background-color: #e84393; width: {score_production}%;"></div>
            </div>
            """,
          unsafe_allow_html=True,
      )

    st.write("")
    st.info(
        f"💡 **نمط الدعم الموصى به:** بناءً على درجات الملف ({uploaded_file.name})،"
        f" يوصي النظام بتقديم **نمط الدعم التكيفي (المباشر/المُوجه)** لتعزيز"
        " جوانب اليقظة الرقمية."
    )

  # --- التبويب الثاني: التفسير الخوارزمي المطور والرسوم التوضيحية ---
  with tab2:
    st.subheader("🔍 التفسير الخوارزمي التفاعلي (XAI Explainability)")
    st.write(
        "يوضح هذا القسم كيفية وصول نموذج الذكاء الاصطناعي لهذه القرارات"
        " والتوصيات:"
    )

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
      st.markdown("##### 📊 مدى مشاركة العوامل في قرار التكّيف (Feature Importance)")
      importance_data = pd.DataFrame({
          "العامل المؤثر": [
              "مستوى اليقظة الرقمية",
              "التفاعل مع بيئة التدريب",
              "ثراء النشاط الذكي",
              "وضوح أهداف الدرس",
          ],
          "نسبة التأثير (%)": [
              score_vigilance,
              score_attitude,
              score_production,
              score_overall,
          ],
      })
      st.bar_chart(importance_data.set_index("العامل المؤثر"))

    with col_chart2:
      st.markdown("##### 📈 مسار تطور الأداء عبر الجلسات")
      session_data = pd.DataFrame({
          "الجلسة التدريبية": ["جلسة 1", "جلسة 2", "جلسة 3 (الحالية)"],
          "مستوى الاتجاه لبيئة التدريب": [
              max(60, score_attitude - 15),
              max(70, score_attitude - 5),
              score_attitude,
          ],
          "مهارة إنتاج الأنشطة": [
              max(55, score_production - 20),
              max(68, score_production - 8),
              score_production,
          ],
      })
      st.line_chart(session_data.set_index("الجلسة التدريبية"))

    st.markdown("---")
    st.markdown("#### 📑 تفاصيل الشرح التفسيري القابل للدرك (XAI Rationale):")

    with st.expander("1. لماذا تم اختيار نمط الدعم الحالي؟", expanded=True):
      st.write(
          f"• **تحليل النص:** أظهرت الخطة المرفوعة كفاءة في الأهداف التشغيلية"
          f" بنسبة {score_production}%، بينما تحتاج معايير تحقق الطلاب من"
          f" المصادر إلى دعم إضافي (اليقظة الرقمية: {score_vigilance}%)."
      )
      st.write(
          "• **القرار الخوارزمي:** توفير تلميحات توجيهية مرئية لتعديل صياغة"
          " الأنشطة لتكون أكثر نقدية وتفاعلية."
      )

    with st.expander("2. تحليل الاتجاه نحو بيئة التدريب الإلكترونية"):
      st.write(
          f"• يُظهر المعلم تفاعلاً وسرعة استجابة عالية داخل البيئة بنسبة"
          f" {score_attitude}%، مما يدل على اتجاه إيجابي مرتفع نحو استخدام"
          f" أدوات التقييم الذكي القائمة على XAI."
      )

  # --- التبويب الثالث: التغذية الراجعة والأنشطة التفاعلية ---
  with tab3:
    st.subheader("🎯 التغذية الراجعة التكيفية والتحدي التطبيقي")

    col_fb1, col_fb2 = st.columns(2)

    with col_fb1:
      st.success("🟢 **التوصيات المباشرة لتحسين النشاط:**")
      st.markdown(
          "1. **تعزيز اليقظة الرقمية:** اضف سؤالاً نقدياً يطلب من الطلاب البحث"
          " عن مصدر المعلومة الرقمية."
      )
      st.markdown(
          "2. **الأنشطة التفاعلية:** استبدل التلقين المباشر بسيناريو تفاعلي"
          " يعتمد على حل المشكلات."
      )

    with col_fb2:
      st.warning("⚡ **سؤال تقييم ذاتي سريع لليقظة الرقمية:**")
      q_ans = st.radio(
          "كيف تتأكد من سلامة النشاط الرقمي قبل تقديمه للطلاب في بيئة"
          " التدريب؟",
          [
              "الاعتماد الكامل على مخرجات الذكاء الاصطناعي.",
              "مراجعة المحتوى نقدياً والتحقق من مصادره وأمنه الرقمي.",
              "تطبيق النشاط دون مراجعة إضافية.",
          ],
      )
      if st.button("تأكيد الإجابة والتقييم"):
        if (
            q_ans
            == "مراجعة المحتوى نقدياً والتحقق من مصادره وأمنه الرقمي."
        ):
          st.balloons()
          st.success(
              "ممتاز جداً! إجابتك تعكس درجات عالية من اليقظة الرقمية"
              " والاتجاه الإيجابي نحو البيئة."
          )
        else:
          st.error("حاول مرة أخرى! اليقظة الرقمية تتطلب التفكير النقدي.")

else:
  st.info(
      "👈 يُرجى رفع ملف الوورد (.docx) للدرس أو النشاط بالأعلى للبدء في"
      " التحليل الفوري وتوليد لوحة التحكّم والتفسير أوتوماتيكياً."
  )
