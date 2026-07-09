import streamlit as st

st.set_page_config(page_title='streamlit 실습', page_icon='👻', layout='wide')

st.sidebar.title('👻강의 일정')
st.sidebar.caption('날짜를 클릭하면 그날의 실습/과제 화면으로 이동합니다.')

selected_day = st.sidebar.radio(
    '날짜를 선택하세요',
    [
        '1일차 : 7월 6일(월)',
        '2일차 : 7월 7일(화)',
        '3일차 : 7월 8일(수)',
        '4일차 : 7월 9일(목)',
        '5일차 : 7월 10일(금)',
    ],
)

st.title(selected_day)
st.divider()

tab_practice, tab_assignment1, tab_assignment2 = st.tabs(['실습', '과제1', '과제2'])

if selected_day == '1일차 : 7월 6일(월)':
    with tab_practice:
        st.header('1일차 실습예제')
        st.title("나의 첫 번째 웹앱")

        st.write("VSCode, uv, Streamlit을 이용해서 만든 웹앱입니다.")

        name = st.text_input("이름을 입력하세요", key="name1")

        if name:
            st.success(f"{name}님, 반갑습니다!")

        age1 = st.slider("나이를 선택하세요", 0, 100, 0, key='age1')

        st.write(f"선택한 나이는 {age1}세입니다.")

        st.header("관심 분야 선택")
        interest = st.selectbox(
            "관심 있는 분야를 선택하세요",
            ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]
        )
        st.write(f"선택한 관심 분야는 {interest}입니다.")

        st.write("---")
        st.title('자기소개')
        st.header('기본 정보')
        st.subheader('취미')
        st.write('저는 축구를 좋아합니다.')
        st.write("---")
        if st.button('인사하기'):
            st.write('안녕하세요!')

        st.write("---")
        st.success('성공했습니다!')
        st.info('안내 메시지입니다.')
        st.warning('주의하세요!')
        st.error('오류가 발생했습니다.')
        st.write("---")
        import random
        luck=['대박','행운','평범','조심','최고']
        if st.button('운세 보기'):
            st.write(random.choice(luck))

        st.write("---")
        #st.image('images/그림1.png')
        st.video('https://www.youtube.com/watch?v=xxxx')

        st.write("---")
        name2 = st.text_input('이름을 입력하세요', key='name2')
        if name2:
            st.write(f'{name2}님, 환영합니다!')

        age2 = st.number_input('나이', min_value=0, max_value=100, key='age2')
        st.write('내년 나이:', age2+1)

        st.write("---")
        score = st.slider('집중도', 0, 100, 50)
        st.write('현재 집중도:', score)

        st.write("---")
        subject = st.selectbox('좋아하는 과목', ['국어','수학','영어','정보'])
        st.write('선택:', subject)

        st.write("---")
        menu = st.radio('점심 메뉴', ['김밥','라면','돈가스'])
        st.write(menu, '선택!')

        st.write("---")
        if st.checkbox('축구','야구', '배구'):
            st.write('축구를 좋아합니다!')

        items = ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]

        selected_items = []

        for item in items:
            checked = st.checkbox(item)
            if checked:
                selected_items.append(item)

        st.subheader("선택한 항목")

        if selected_items:
            st.write(selected_items)
        else:
            st.write("아직 선택한 항목이 없습니다.")
            
        st.write("---")
        score = st.number_input('점수', 0, 100)
        if score >= 60:
            st.success('합격')
        else:
            st.warning('다시 도전')

        st.write("---")
        name3=st.text_input('이름', key='name3')
        age3=st.number_input('나이',0,100, key='age3')
        field3=st.selectbox('관심분야',['AI','게임','디자인'], key='field3')
        st.write(name3, age3, field3)

        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            st.write('왼쪽')
        with col2:
            st.write('오른쪽')

        st.write("---")
        menu = st.sidebar.selectbox('메뉴', ['홈','분석','설정'])
        st.write('선택한 메뉴:', menu)

        st.write("---")
        tab1, tab2 = st.tabs(['소개','실습'])
        with tab1:
            st.write('소개 화면')
        with tab2:
            st.write('실습 화면')


        st.write("---")
        if 'count' not in st.session_state:
            st.session_state.count = 0

        if st.button('증가'):
                st.session_state.count += 1

        st.write(st.session_state.count)


    with tab_assignment1:
        st.header('1일차 실습과제1')
        import random
 
        st.set_page_config(page_title="나의 프로필 & 오늘의 명언", page_icon="✨", layout="wide")
        
        quotes = [
            ("시작이 반이다.", "아리스토텔레스"),
            ("천 리 길도 한 걸음부터.", "한국 속담"),
            ("가장 큰 위험은 위험 없는 삶이다.", "작자 미상"),
            ("오늘 할 수 있는 일을 내일로 미루지 마라.", "벤저민 프랭클린"),
            ("실패는 성공으로 가는 과정일 뿐이다.", "토마스 에디슨"),
            ("배움에 있어 늦은 때는 없다.", "작자 미상"),
            ("작은 습관이 큰 변화를 만든다.", "제임스 클리어"),
            ("너 자신을 알라.", "아리스토텔레스"),
            ("안정우 바보", "류규민"),
        ]
        
        if "quote_index" not in st.session_state:
            st.session_state.quote_index = random.randrange(len(quotes))
        
        st.title("나의 프로필 & 오늘의 명언")
        st.write("")
        
        col_profile, col_quote = st.columns(2)
        
        with col_profile:
            st.header("내 프로필")
            st.subheader("류규민")
            st.write("고등학교 1학년, 미래의 정복자")
            st.write("관심사: 게임, 음악, 안정우, 운동")
            st.info("위 이름과 소개, 관심사를 자기 것으로 바꿔보세요.")
        
        with col_quote:
            st.header("오늘의 명언")
            quote_text, quote_author = quotes[st.session_state.quote_index]
            st.success(quote_text)
            st.write(f"말한 사람: {quote_author}")
        
            if st.button("다른 명언 보기"):
                st.session_state.quote_index = random.randrange(len(quotes))
                st.rerun()
    
    with tab_assignment2:
        st.header('1일차 실습과제2')
        st.set_page_config(page_title="BMI 계산기", page_icon="⚖️", layout="wide")
 
        st.title("BMI 계산기")
        st.write("키와 몸무게를 입력하고 버튼을 눌러 체질량지수(BMI)를 확인해보세요.")
        st.divider()
        
        col_input, col_result = st.columns(2)
        
        with col_input:
            st.header("정보 입력")
            height_cm = st.slider("키 (cm)", min_value=100, max_value=220, value=165)
            weight_kg = st.slider("몸무게 (kg)", min_value=30, max_value=150, value=55)
            calculate = st.button("BMI 계산하기")
        
        with col_result:
            st.header("결과")
        
            if calculate:
                height_m = height_cm / 100
                bmi = weight_kg / (height_m ** 2)
        
                # 대한비만학회(KSSO) 기준: 저체중 <18.5 / 정상 18.5~22.9 / 과체중 23~24.9 / 비만 25 이상
                if bmi < 18.5:
                    category = "저체중"
                elif bmi < 23:
                    category = "정상 체중"
                elif bmi < 25:
                    category = "과체중"
                else:
                    category = "비만"
        
                st.metric(label="나의 BMI", value=f"{bmi:.1f}", delta=category, delta_color="off")
        
                # BMI 값을 0.0~1.0 사이 진행률로 환산 (15~35 범위를 기준으로)
                scale_min, scale_max = 15, 35
                progress_value = max(0.0, min(1.0, (bmi - scale_min) / (scale_max - scale_min)))
                st.progress(progress_value, text=f"저체중 ← BMI {bmi:.1f} → 비만")
        
                if category == "저체중":
                    st.info("표준 체중보다 가벼운 편입니다. 균형 잡힌 식사가 도움이 될 수 있어요.")
                elif category == "정상 체중":
                    st.success("건강한 범위의 체중입니다. 지금처럼 잘 유지해보세요.")
                elif category == "과체중":
                    st.warning("표준보다 조금 높은 편입니다. 꾸준한 활동이 도움이 될 수 있어요.")
                else:
                    st.error("전문가와 상담을 통해 건강 관리 계획을 세워보는 것을 권장합니다.")
        
                st.caption(
                    "이 결과는 대한비만학회 성인 기준을 적용한 참고용 계산입니다. "
                    "성장기 청소년은 나이·성별별 성장도표(퍼센타일)를 함께 보는 것이 더 정확합니다."
                )
            else:
                st.info("왼쪽에서 키와 몸무게를 입력하고 'BMI 계산하기' 버튼을 눌러주세요.")

elif selected_day == '2일차 : 7월 7일(화)':
    with tab_practice:
        st.header('2일차 실습예제')

        with tab_assignment1:
            st.header('2일차 실습과제1')
            st.subheader("고등학생 진로/학습 AI 챗봇")
            st.write(
                "궁금한 진로, 공부법, 고민을 편하게 물어보세요! (Google **Gemini API** 사용 — "
                "결제수단 등록 없이 무료로 발급받은 키로 바로 테스트할 수 있어요.)"
            )
        
            with st.sidebar:
                st.markdown("### 🔑 Day5 챗봇 설정 (Gemini)")
                api_key = st.text_input(
                    "Gemini API Key",
                    type="password",
                    value="",
                    help="https://aistudio.google.com/apikey 에서 Google 계정으로 로그인 후 무료 발급. "
                        "키는 서버에 저장되지 않고 이 세션에서만 사용됩니다.",
                )
                model_name = st.selectbox(
                    "모델 선택",
                    ["gemini-2.5-flash", "gemini-2.5-flash-lite"],
                    help="Flash / Flash-Lite 계열은 무료 티어(RPM/RPD 한도 내)에서 사용할 수 있는 모델입니다.",
                )
                persona = st.selectbox(
                    "챗봇 성격 선택",
                    ["친절한 진로상담 선생님", "논리적인 스터디 코치", "유머러스한 친구 같은 챗봇"],
                )
                if st.button("Day5 대화 초기화 🔄"):
                    st.session_state.day5_chat_messages = []
                    st.session_state.pop("day5_gemini_chat", None)
                    st.session_state.pop("day5_gemini_chat_key", None)
                    st.rerun()
        
            persona_prompts = {
                "친절한 진로상담 선생님": (
                    "당신은 따뜻하고 친절한 고등학교 진로상담 선생님입니다. "
                    "학생의 눈높이에 맞춰 쉽고 구체적으로, 격려하는 말투로 답변하세요."
                ),
                "논리적인 스터디 코치": (
                    "당신은 체계적이고 논리적인 학습 코치입니다. "
                    "학생의 질문에 단계별로, 근거를 들어 명확하게 답변하세요."
                ),
                "유머러스한 친구 같은 챗봇": (
                    "당신은 학생과 친구처럼 편하게 대화하는 유쾌한 챗봇입니다. "
                    "가볍고 재미있는 말투를 쓰되, 유용한 정보는 정확히 전달하세요."
                ),
            }
        
            if "day5_chat_messages" not in st.session_state:
                st.session_state.day5_chat_messages = []
        
            for msg in st.session_state.day5_chat_messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
        
            prompt = st.chat_input("궁금한 것을 물어보세요!", key="day5_chat_input")
        
            if prompt:
                if not api_key:
                    st.error("먼저 사이드바에 Gemini API Key를 입력해주세요! 🔑 (https://aistudio.google.com/apikey)")
                    st.stop()
        
                st.session_state.day5_chat_messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
        
                try:
                    from google import genai
                    from google.genai import types
        
                    # 모델/페르소나가 바뀌면 채팅 세션을 새로 만들고, 그렇지 않으면 기존 세션(대화 맥락)을 재사용
                    chat_key = f"{model_name}::{persona}"
                    if st.session_state.get("day5_gemini_chat_key") != chat_key:
                        client = genai.Client(api_key=api_key)
                        st.session_state.day5_gemini_chat = client.chats.create(
                            model=model_name,
                            config=types.GenerateContentConfig(
                                system_instruction=persona_prompts[persona],
                            ),
                        )
                        st.session_state.day5_gemini_chat_key = chat_key
        
                    chat = st.session_state.day5_gemini_chat
        
                    with st.chat_message("assistant"):
                        placeholder = st.empty()
                        full_response = ""
                        for chunk in chat.send_message_stream(prompt):
                            if chunk.text:
                                full_response += chunk.text
                                placeholder.markdown(full_response + "▌")
                        placeholder.markdown(full_response)
        
                    st.session_state.day5_chat_messages.append({"role": "assistant", "content": full_response})
                except Exception as e:
                    st.error(f"오류가 발생했어요: {e}")
    
    with tab_assignment2:
        st.header('2일차 실습과제2')

elif selected_day == '3일차 : 7월 8일(수)':
    with tab_practice:
        st.header('3일차 실습예제')

    with tab_assignment1:
        st.header('3일차 실습과제1')
    
    with tab_assignment2:
        st.header('3일차 실습과제2')

elif selected_day == '4일차 : 7월 9일(목)':
    with tab_practice:
        st.header('4일차 실습예제')

    with tab_assignment1:
        st.header('4일차 실습과제1')
    
    with tab_assignment2:
        st.header('4일차 실습과제2')
       
elif selected_day == '5일차 : 7월 10일(금)':
    with tab_practice:
        st.header('5일차 실습예제')

    with tab_assignment1:
        st.header('5일차 실습과제1')
    
    with tab_assignment2:
        st.header('5일차 실습과제2')        