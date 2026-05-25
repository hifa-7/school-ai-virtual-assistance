from flask import Flask, request

app = Flask(__name__)

school_info = {
    "name": "المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)",
    "school_name": "مدرسة عمرة بنت رواحة",
    "grades": "الصفان الخامس والسادس",
    "location": "المعبيلة الجنوبية الصناعية",
    "established": "٢٠٢٣",
    "phone": "٢٤٥٠٠٠٠٠",
    "email": "amra.school@example.com"
}

class_teachers = {
    "الخامس ١": "الأستاذة مريم البلوشية",
    "الخامس ٢": "الأستاذة نورة السعدية",
    "الخامس ٣": "الأستاذة فاطمة الهنائية",
    "الخامس ٤": "الأستاذة عائشة الرواحية",
    "الخامس ٥": "الأستاذة هدى المعمرية",
    "السادس ١": "الأستاذة سارة الشكيلية",
    "السادس ٢": "الأستاذة منى الهاشمية",
    "السادس ٣": "الأستاذة خولة العامرية",
    "السادس ٤": "الأستاذة زينب الحجرية",
    "السادس ٥": "الأستاذة ليلى السيابية"
}

weekly_schedule = {
    "الأحد": ["اللغة العربية", "الرياضيات", "العلوم", "اللغة الإنجليزية", "التربية الإسلامية", "تقنية المعلومات", "رياضة مدرسية", "نشاط"],
    "الإثنين": ["الرياضيات", "اللغة العربية", "الدراسات الاجتماعية", "العلوم", "اللغة الإنجليزية", "الفنون التشكيلية", "تقنية المعلومات", "قراءة"],
    "الثلاثاء": ["العلوم", "الرياضيات", "اللغة العربية", "التربية الإسلامية", "اللغة الإنجليزية", "مهارات حياتية", "رياضة مدرسية", "نشاط"],
    "الأربعاء": ["اللغة الإنجليزية", "الرياضيات", "الدراسات الاجتماعية", "العلوم", "اللغة العربية", "تقنية المعلومات", "الفنون التشكيلية", "مراجعة"]
}

exam_schedule = {
    "الأحد ٢ فبراير ٢٠٢٥": "اللغة العربية",
    "الإثنين ٣ فبراير ٢٠٢٥": "الرياضيات",
    "الثلاثاء ٤ فبراير ٢٠٢٥": "العلوم",
    "الأربعاء ٥ فبراير ٢٠٢٥": "اللغة الإنجليزية",
    "الخميس ٦ فبراير ٢٠٢٥": "الدراسات الاجتماعية",
    "الأحد ٩ فبراير ٢٠٢٥": "التربية الإسلامية",
    "الإثنين ١٠ فبراير ٢٠٢٥": "تقنية المعلومات"
}


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
                <input type="text" name="question" placeholder="اكتب سؤالك هنا مثل معلومات المدرسة أو الجدول أو الاختبارات" required>
                <br><br>
                <button type="submit">إرسال</button>
            </form>

            <p class="hint">
            أمثلة للأسئلة: أين تقع المدرسة؟ ما رقم المدرسة؟ من مربية الصف الخامس ١؟ ما جدول الاختبارات؟ ما جدول يوم الأحد؟
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"].strip().lower()

    if "معلومات" in question or "المدرسة" in question or "تقع" in question or "انشئت" in question or "إنشاؤها" in question:
        answer = f"""
        <b>معلومات المدرسة:</b><br>
        اسم المدرسة: {school_info["school_name"]}<br>
        الصفوف: {school_info["grades"]}<br>
        الموقع: {school_info["location"]}<br>
        سنة الإنشاء: {school_info["established"]}<br>
        رقم المدرسة: {school_info["phone"]}<br>
        البريد الإلكتروني: {school_info["email"]}
        """

    elif "رقم" in question or "تواصل" in question or "هاتف" in question:
        answer = f"""
        يمكنكم التواصل مع المدرسة عبر الرقم: {school_info["phone"]}<br>
        أو البريد الإلكتروني: {school_info["email"]}<br>
        ملاحظة: هذه بيانات تجريبية لأغراض عرض المشروع.
        """

    elif "مربية" in question or "مربيات" in question or "رائدة" in question:
        answer = "<b>مربيات الصفوف:</b><br>"
        for class_name, teacher in class_teachers.items():
            answer += f"{class_name}: {teacher}<br>"

    elif "اختبار" in question or "اختبارات" in question or "فبراير" in question:
        answer = "<b>جدول الاختبارات لشهر فبراير ٢٠٢٥:</b><br>"
        for date, subject in exam_schedule.items():
            answer += f"{date}: {subject}<br>"

    elif "جدول" in question or "حصص" in question:
        answer = "<b>الجداول الدراسية من الأحد إلى الأربعاء:</b><br><br>"
        for day, lessons in weekly_schedule.items():
            answer += f"<b>{day}</b><br>"
            for index, lesson in enumerate(lessons, start=1):
                answer += f"الحصة {index}: {lesson}<br>"
            answer += "<br>"

    elif "خامس" in question:
        answer = """
        تضم المدرسة خمسة صفوف للصف الخامس:<br>
        الخامس ١<br>
        الخامس ٢<br>
        الخامس ٣<br>
        الخامس ٤<br>
        الخامس ٥<br>
        ولكل صف ٨ حصص يوميًا من الأحد إلى الأربعاء.
        """

    elif "سادس" in question:
        answer = """
        تضم المدرسة خمسة صفوف للصف السادس:<br>
        السادس ١<br>
        السادس ٢<br>
        السادس ٣<br>
        السادس ٤<br>
        السادس ٥<br>
        ولكل صف ٨ حصص يوميًا من الأحد إلى الأربعاء.
        """

    elif "الدوام" in question:
        answer = "يبدأ الدوام المدرسي الساعة ٧:٠٠ صباحًا وينتهي حسب الجدول المدرسي المعتمد."

    else:
        answer = """
        شكرًا لتواصلكم مع المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦).<br>
        يمكنكم السؤال عن معلومات المدرسة أو الجداول أو مربيات الصفوف أو الاختبارات أو التواصل.
        """

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
