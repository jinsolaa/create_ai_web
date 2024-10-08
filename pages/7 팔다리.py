import streamlit as st
from openai import OpenAI

# 교사에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("DALL-E 3 이미지 생성기")

    # 사용자 입력 받기
    favorite_object = st.text_input("좋아하는 물건을 입력하세요", "teddy bear")
    # 프롬프트 설정 (팔다리와 눈 추가, 이미 팔다리나 눈이 있는 물건은 제외)
    if "bear" in favorite_object.lower() or "cat" in favorite_object.lower() or "dog" in favorite_object.lower() or "doll" in favorite_object.lower():
        prompt = favorite_object
    else:
        prompt = f"{favorite_object} with simple, cute hand-drawn style arms, legs, and eyes"

    # 버튼을 클릭했을 때 이미지 생성
    if st.button("이미지 생성"):
        # OpenAI API를 사용하여 이미지 생성
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # 생성된 이미지 URL 가져오기
        image_url = response.data[0].url

        # 이미지 출력
        st.image(image_url, caption=f"Generated Image: {prompt}")


    