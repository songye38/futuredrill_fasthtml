from fasthtml.common import *
from random import choice

# Google Fonts에서 서체 링크 추가
link = Link(href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&family=Poor+Story&display=swap", rel="stylesheet")
preconnect1 = Link(rel="preconnect", href="https://fonts.googleapis.com")
preconnect2 = Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="true")

# CSS 스타일 추가
css = Style('''         
    :root {
        --pico-font-size: 90%;
        --pico-font-family: 'IBM Plex Sans KR', sans-serif;  /* 기본 폰트 */
        --main-bg-color: #ffffff;
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
    /* 모바일 화면 크기에서 텍스트 스타일 변경 */
    @media (max-width: 768px) {
        .description {
            font-size: 1rem; /* 글자 크기 줄이기 */
            line-height: 1.4; /* 줄 간격 조정 */
            margin-bottom: 0.8rem; /* 간격을 조금 더 줄여서 공간을 확보 */
        }
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
    .myclass {
        font-style: italic;
    }
''')

app = FastHTML(hdrs=(preconnect1, preconnect2, link, css))

@app.route("/test")
def get():
    # 랜덤으로 A 또는 B 선택
    version = choice(["A", "B"])

    if version == "A":
        return (Title("퓨쳐드릴 프로토타입 A 페이지"),
                Main(H1('음성으로 당신의 소중한 기억을 간직하세요.'), cls="container"),
                P('당신의 소중한 기억을 잃지 않도록 도와드립니다.', cls='description'),
                P('이제, 음성으로 쉽게 기억을 기록하세요.', cls='description'),
                P('우리의 서비스는 경증 치매를 앓고 계신 분들이 자신만의 이야기나 추억을 음성으로 남길 수 있도록 돕습니다.', cls='description'),
                P('쉽고 간편한 인터페이스로 누구나 편안하게 사용하실 수 있습니다.', cls='description'),
                P('모든 기억을 기록하고, 오랫동안 간직하세요.', cls='description'),
                A("알림 신청하기", href="#", cls="cta-button"))
            
                # Body(Div('인생에서 가장 소중했던 기억은 무엇인가요?', cls='question')))

    elif version == "B":
        return (Title("퓨쳐드릴 프로토타입 B 페이지"), 
                Main(H3('샘 (버전 B)'), cls="container"),
                Body(Div('가장 행복했던 순간은 언제였나요?', cls='myclass')))


# A/B 테스트를 위한 버전 정의
@app.route("/function")
def get():
    return (Title("퓨쳐드릴 프로토타입 B 페이지"), 
                Main(H3('안녕하세요 (버전 B)'), cls="container"))




# Form(Input(type="text", name="data"),
#         Button("제출"),
#         action="/", method="post"))