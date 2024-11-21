from flask import Flask, request, jsonify
from fasthtml.common import *
from random import choice

# FastHTML 설정
link = Link(href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&family=Poor+Story&display=swap", rel="stylesheet")
preconnect1 = Link(rel="preconnect", href="https://fonts.googleapis.com")
preconnect2 = Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="true")

css = Style('''
    :root {
        --pico-font-size: 90%;
        --pico-font-family: 'IBM Plex Sans KR', sans-serif;
        --main-bg-color: #ffffff;
        --main-color: #39A1FC;
        --accent-color: #39A1FC;
        --button-color: #39A1FC;
        --button-text-color: white;
    }
    body {
        font-family: var(--pico-font-family);
        background-color: var(--main-bg-color);
        color: var(--main-color);
        padding: 130px;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
    }
    h1, h3 {
        text-align: center;
        color: var(--accent-color);
    }
    .description {
        color : #000;
        font-size: 18px;
        line-height: 0.6;
        text-align: center;
        margin-bottom: 20px;
    }
    .cta-button {
        display: block;
        background-color: var(--button-color);
        color: var(--button-text-color);
        padding: 10px 20px;
        text-align: center;
        border-radius: 5px;
        margin: 0 auto;
        width: 200px;
        text-decoration: none;
        font-size: 18px;
    }
    .cta-button:hover {
        background-color: #45a049;
    }
    .question {
        font-size: 20px;
        text-align: center;
        margin-top: 30px;
    }
''')

# FastHTML을 사용할 페이지 라우트
@app.route("/test")
def test_page():
    version = choice(["A", "B"])

    if version == "A":
        html_content = (Title("퓨쳐드릴 프로토타입 A 페이지"),
                        Main(H1('음성으로 당신의 소중한 기억을 간직하세요.'), cls="container"),
                        P('당신의 소중한 기억을 잃지 않도록 도와드립니다.', cls='description'),
                        P('이제, 음성으로 쉽게 기억을 기록하세요.', cls='description'),
                        P('우리의 서비스는 경증 치매를 앓고 계신 분들이 자신만의 이야기나 추억을 음성으로 남길 수 있도록 돕습니다.', cls='description'),
                        P('쉽고 간편한 인터페이스로 누구나 편안하게 사용하실 수 있습니다.', cls='description'),
                        P('모든 기억을 기록하고, 오랫동안 간직하세요.', cls='description'),
                        Form(
                            Button("알림 받기", cls="cta-button alert-button", id="alert-track-button"),
                            action="#", method="post"
                        ))
    else:
        html_content = (Title("퓨쳐드릴 프로토타입 B 페이지"),
                        Main(H3('샘 (버전 B)'), cls="container"),
                        P('가장 행복했던 순간은 언제였나요?', cls='myclass'))

    # FastHTML 객체를 Response 객체로 변환하여 반환
    return Response(str(html_content), mimetype='text/html; charset=utf-8')


# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, port=5001)
