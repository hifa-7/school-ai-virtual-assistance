from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)</title>

        <style>
            body {
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 50px;
            }

            .container {
                background: white;
                width: 60%;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }

            input {
                width: 70%;
                padding: 10px;
                margin-top: 20px;
            }

            button {
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }

            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)</h1>

            <p>
            مرحبًا بكم في المساعد الافتراضي الذكي الخاص بالمدرسة
            </p>

            <form action="/ask" method="post">

                <input
                    type="text"
                    name="question"
                    placeholder="اكتب سؤالك هنا"
                    required
                >

                <br><br>

                <button type="submit">
                    إرسال
                </button>

            </form>

        </div>

    </body>
    </html>
    """


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"].lower()

    if "الدوام" in question:
        answer = "يبدأ الدوام المدرسي الساعة 7:00 صباحًا."

    elif "الاختبارات" in question:
        answer = "يرجى متابعة إدارة المدرسة لمعرفة جداول الاختبارات."

    elif "التواصل" in question:
        answer = "يمكنكم التواصل مع إدارة المدرسة خلال أوقات الدوام الرسمي."

    elif "المعلمات" in question:
        answer = "يرجى مراجعة إدارة المدرسة للاستفسار عن المعلمات والمواد الدراسية."

    else:
        answer = "شكرًا لتواصلكم مع المساعد الافتراضي لمدرسة عمرة بنت رواحة (٥-٦)."

    return f"""
    <html>

    <head>

        <title>نتيجة الاستفسار</title>

        <style>

            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 50px;
            }}

            .container {{
                background: white;
                width: 60%;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }}

            a {{
                text-decoration: none;
                color: blue;
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
