import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 타이틀 설정
st.title("QR 코드 생성기")

# 사용자 입력을 받음
input_data = st.text_input("QR 코드로 변환할 텍스트 또는 URL을 입력하세요:")

# QR 코드 생성 버튼
if st.button("QR 코드 생성"):
    if input_data:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)

        # 이미지 생성
        img = qr.make_image(fill='black', back_color='white')

        # 이미지 버퍼에 저장
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)
        image = Image.open(buf)

        # 이미지 출력
        st.image(image, caption="생성된 QR 코드", use_column_width=True)
    else:
        st.error("텍스트 또는 URL을 입력하세요.")

# 페이지 하단에 크레딧 추가
st.write("이 앱은 Streamlit과 qrcode 라이브러리를 사용하여 만들어졌습니다.")
