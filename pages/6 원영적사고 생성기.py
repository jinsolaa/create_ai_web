import streamlit as st
import google.generativeai as genai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("Google Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # API 키 설정
    genai.configure(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("원영적 사고")

    # 생성 설정
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # 모델 초기화
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # 사용자 입력 받기
    user_input = st.text_area("원영적 사고가 필요한 내용을 입력하세요.", 
                              "예: 빵이 먹고 싶어서 빵집에 갔는데 내 앞에서 진열된 빵이 다 팔려버렸어.")

    if st.button("원영적 사고 생성"):
        # 인공지능 모델을 사용하여 원영적 사고 생성
        response = model.generate_content([
            "입력한 내용을 긍정적인 사고로 바꾸어서 보여줌. 답장하는 것이 아님. 완전 럭키비키잖아.라는 멘트를 꼭 붙여야함. 예를 들어, 출력물은 내 앞에서 진열된 빵이 다 팔렸지만, 덕분에 갓나온 빵을 먹을 수 있다니 완전 럭키비키잖아💛✨ 라고 함. 그리고 이모티콘을 엄청 많이 사용해야해.",
            f"input: {user_input}",
        ])

        # 결과 출력
        st.subheader("원영적 사고")
        st.write(response.text)
else:
    st.warning("API 키를 사이드바에 입력하세요.")
