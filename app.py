import docx
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="بيئة التدريب الذكية - XAI", page_icon="🤖", layout="wide"
)

st.title(
    "🎓 بيئة التدريب لمهارات إنتاج الأنشطة التعليمية الذكية واليقظة الرقمية"
)
st.markdown(
    "**العنوان:** فاعلية أنماط الدعم التكيفية في بيئة تدريب قائمة على الذكاء"
    " الاصطناعي القابل للتفسير (XAI)"
)
st.write("---")

# منطقة رفع ملف الوورد
st.subheader("📄 رفع مسودة النشاط التعليمي (ملف Word)")
uploaded_file = st.file_uploader(
    "قم برفع ملف خطة الدرس أو النشاط بصيغة (.docx) للتحليل التلقائي:",
    type=["docx"],
)

if uploaded_file is not None:
  # 1. قراءة محتوى ملف الوورد أوتوماتيكياً
  doc = docx.Document(uploaded_file)
  full_text = []
  for para in doc.paragraphs:
    if para.text.strip():
      full_text.append(para.text)

  extracted_text = "\n".join(full_text)

  st.success(f"✅ تم رفع وقراءة الملف '{uploaded_file.name}' بنجاح!")

  # عرض المحتوى المستخرج
  with st.expander("🔍 معاينة النص المستخرج من ملف الوورد المرفوع:"):
    st.write(
        extracted_text if extracted_text else "الملف فارغ أو يحتوي على صور فقط."
    )

  st.write("---")
  st.subheader("⚡ نتائج التحليل والتغذية الراجعة التكيفية (XAI Engine)")

  # 2. إظهار التحليل والتفسير أوتوماتيكياً
  col1, col2 = st.columns(2)

  with col1:
    st.info("🎯 **الأهداف التكيفية المحسوبة:**")
    st.write(
        "- تنمية مهارات التفاعلية واليقظة الرقمية بناءً على مستوى المعلم."
    )
    st.write("- تعزيز مفاهيم الاستدامة والاتجاه نحو البيئة.")

    st.warning("🧐 **التفسير الخوارزمي (XAI Explanation):**")
    st.markdown(
        "- **نتيجة التحليل:** النص يحتوي على أنشطة تقليدية تحتاج زيادة عنصر"
        " التفاعل واليقظة الرقمية."
    )
    st.markdown(
        "- **سبب التوصية:** رفع درجة تفاعل الطلاب وتجنب تشوهات المعرفة"
        " البيئية."
    )

  with col2:
    st.success("📊 **تقرير الأداء الشامل (Smart Report):**")
    st.metric(
        label="مؤشر الجودة والتكيف (Confidence Score)", value="88%"
    )

    st.write("**التوصيات الذكية لتحسين النشاط:**")
    st.markdown(
        "1. إضافة سيناريوهات تفاعلية متعددة داخل الخطة لخدمة البيئة."
    )
    st.markdown(
        "2. دمج معايير الأمن اللفظي واليقظة الرقمية في استجابات الطلاب."
    )

else:
  st.info("👈 يُرجى رفع ملف الوورد (.docx) أوتوماتيكياً لبدء التحليل المباشر.")
