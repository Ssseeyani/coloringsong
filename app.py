
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="자유 색칠하기")
st.title("고전 초상화 색칠하기")

# Load background image
image_path = "portrait.png"  # 이미지 파일명을 그대로 사용
img = Image.open(image_path)

# Show background image
st.write("### 색칠하려면 아래 캔버스를 사용하세요")

canvas_result = st_canvas(
    fill_color="rgba(255, 0, 0, 0.3)",  # 투명한 붓 색 기본값
    stroke_width=5,
    stroke_color="#ff0000",
    background_image=img,
    update_streamlit=True,
    height=img.height,
    width=img.width,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("그림 초기화"):
    st.experimental_rerun()

st.caption("*그림을 색칠한 후 스크린샷으로 저장하세요!*")
