from flask import Flask, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

school_context = """
أنت المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦).
تخدم الطالبات وأولياء الأمور والمعلمات والمجتمع المدرسي.
أجب باللغة العربية بأسلوب واضح ومهذب ومختصر.

معلومات المدرسة:
- اسم المدرسة: مدرسة عمرة بنت رواحة
- الصفوف: الخامس والسادس
- الموقع: المعبيلة الجنوبية الصناعية
- سنة الإنشاء: ٢٠٢٣
- رقم المدرسة التجريبي: ٢٤٥٠٠٠٠٠
- البريد التجريبي: amra.school@example.com

الصفوف:
- الخامس ١، الخامس ٢، الخامس ٣، الخامس ٤، الخامس ٥
- السادس ١، السادس ٢، السادس ٣، السادس ٤، السادس ٥

مربيات الصفوف:
- الخامس ١: الأستاذة مريم البلوشية
- الخامس ٢: الأستاذة نورة السعدية
- الخامس ٣: الأستاذة فاطمة الهنائية
- الخامس ٤: الأستاذة عائشة الرواحية
- الخامس ٥: الأستاذة هدى المعمرية
- السادس ١: الأستاذة سارة الشكيلية
- السادس ٢: الأستاذة منى الهاشمية
- السادس ٣: الأستاذة خولة العامرية
- السادس ٤: الأستاذة زينب الحجرية
- السادس ٥: الأستاذة ليلى السيابية

الجداول الدراسية من الأحد إلى الأربعاء، ٨ حصص يوميًا:
الأحد:
١ اللغة العربية، ٢ الرياضيات، ٣ العلوم، ٤ اللغة الإنجليزية، ٥ التربية الإسلامية، ٦ تقنية المعلومات، ٧ الرياضة المدرسية، ٨ نشاط

الإثنين:
١ الرياضيات، ٢ اللغة العربية، ٣ الدراسات الاجتماعية، ٤ العلوم، ٥ اللغة الإنجليزية، ٦ الفنون التشكيلية، ٧ تقنية المعلومات، ٨ قراءة

الثلاثاء:
١ العلوم، ٢ الرياضيات، ٣ اللغة العربية، ٤ التربية الإسلامية، ٥ اللغة الإنجليزية، ٦ المهارات الحياتية، ٧ الرياضة المدرسية، ٨ نشاط

الأربعاء:
١ اللغة الإنجليزية، ٢ الرياضيات، ٣ الدراسات الاجتماعية، ٤ العلوم، ٥ اللغة العربية، ٦ تقنية المعلومات، ٧ الفنون التشكيلية، ٨ مراجعة

جدول الاختبارات التجريبي لشهر فبراير ٢٠٢٥:
- الأحد ٢ فبراير ٢٠٢٥: اللغة العربية
- الإثنين ٣ فبراير ٢٠٢٥: الرياضيات
- الثلاثاء ٤ فبراير ٢٠٢٥: العلوم
- الأربعاء ٥ فبراير ٢٠٢٥: اللغة الإنجليزية
- الخميس ٦ فبراير ٢٠٢٥: الدراسات الاجتماعية
- الأحد ٩ فبراير ٢٠٢٥: التربية الإسلامية
- الإثنين ١٠ فبراير ٢٠٢٥: تقنية المعلومات

تنبيه مهم:
بعض البيانات تجريبية لأغراض عرض المشروع فقط.
إذا سأل المستخدم عن معلومة غير موجودة، أخبره بلطف أن المعلومة غير متوفرة حاليًا.
"""

@app.route("/")
def home():
    return """
    <html dir="rtl" lang="ar">
    <head>
        <title>المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 40px;
            }
            .container {
                background: white;
                width: 70%;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }
            input {
                width: 75%;
                padding: 12px;
                margin-top: 20px;
                border-radius: 6px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                padding: 12px 24px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 6px;
                font-size: 16px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .hint {
                color: #555;
                font-size: 14px;
                margin-top: 20px;
                line-height: 1.8;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)</h1>

            <p>
            مرحبًا بكم في المساعد الافتراضي الخاص بالمدرسة لخدمة الطالبات وأولياء الأمور والمعلمات والمجتمع المدرسي
            </p>

            <form action="/ask" method="post">
                <input type="text" name="question" placeholder="اكتب سؤالك هنا" required>
                <br><br>
                <button type="submit">إرسال</button>
            </form>

            <p class="hint">
            أمثلة للأسئلة:<br>
            أين تقع المدرسة؟<br>
            من مربية الصف الخامس ١؟<br>
            ما جدول يوم الأحد؟<br>
            ما جدول الاختبارات؟<br>
            كم عدد صفوف الخامس والسادس؟
            </p>
        </div>
    </body>
    </html>
    """

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"].strip()

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": school_context},
                {"role": "user", "content": question}
            ],
            stream=False
        )

        answer = response.choices[0].message.content

    except Exception:
        answer = "عذرًا، حدثت مشكلة مؤقتة في تشغيل المساعد. يرجى المحاولة لاحقًا."

    return f"""
    <html dir="rtl" lang="ar">
    <head>
        <title>نتيجة الاستفسار</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 40px;
            }}
            .container {{
                background: white;
                width: 70%;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                line-height: 1.8;
            }}
            a {{
                text-decoration: none;
                color: #007BFF;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h2>السؤال:</h2>
            <p>{question}</p>

            <hr>

            <h2>الإجابة:</h2>
            <p>{answer}</p>

            <br>
            <a href="/">العودة للصفحة الرئيسية</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
