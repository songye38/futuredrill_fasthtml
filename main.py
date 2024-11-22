import os
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *
from datetime import datetime
import pytz

load_dotenv()

MAX_NAME_CHAR = 15
MAX_MESSAGE_CHAR = 50
TIMESTAMP_FMT = '%Y-%m-%d %I:%M:%S %p GMT'

app,rt = fast_app()

#supabase 초기화
supabase = create_client(os.getenv('SUPABASE_URL'),os.getenv('SUPABASE_KEY'))

#메세지 가져오기
def get_messages():
    response = supabase.table('MyGuestbook').select('*').order('id',desc=True).execute()
    return response.data


#내가 있는 시간대에서 지금 시간 가져오기
def get_gmt_time():
    gmt_tz = pytz.timezone('GMT')
    return datetime.now(gmt_tz)

def add_message(name,message):
    timestamp = get_gmt_time().strftime(TIMESTAMP_FMT)
    supabase.table('MyGuestbook').insert(
        {"name":name, "messgae":message,"timestamp":timestamp}
    ).execute()



def render_message(entry):
    return (
        Article(
            Header(f'Name:{entry['name']}'),
            P(entry['messgae']),
            Footer(Small(Em(f'Posted:{entry['timestamp']}'))),
        ),
    )

def render_message_list():
    messages = get_messages()
    return Div(
        *[render_message(entry) for entry in messages],
        id = 'message-list'
    )

def render_content():
    form = Form(
        Fieldset(
            Input(
                type='text',
                name='name',
                placeholder = '이름',
                required = True,
                maxlength = MAX_NAME_CHAR,
            ),
            Input(
                type='text',
                name='message',
                placeholder = '메세지',
                required = True,
                maxlength = MAX_MESSAGE_CHAR,
            ),
            Button('submit',type='submit'),
            role = 'group',
        ),
        method = 'post',
        hx_post = '/submit-message',
        hx_target = '#message-list',
        hx_swap = 'outerHTML',
        hx_on__after_request = 'this.reset()',
    )

    return Div(
        P(Em("write something nice!")),
        form,
        Div(
            "made with 💖",
            A("by sonye ",href='vsongyev.myportfolio.com',target="_blank"),
        ),
        Hr(),
        render_message_list(),
    )



@rt('/')
def get(): return Titled("My Guestbook",render_content())

@rt('/submit-message',methods=['POST'])
def post(name:str,message:str):
    add_message(name,message)
    return render_message_list()

serve()