import streamlit as st
import re

# Tiêu đề trang
st.title("Đăng ký tài khoản")

# Khởi tạo session state cho tiến trình nếu chưa có
if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Các trường thông tin
username = st.text_input("1 - Tài khoản")
password = st.text_input("2 - Mật khẩu", type="password")
confirm_password = st.text_input("3 - Nhập lại mật khẩu", type="password")
full_name = st.text_input("4 - Tên người dùng")
email = st.text_input("5 - Email")

# Kiểm tra mức độ hoàn thành
def calculate_progress():
    progress = 0
    if username:
        progress += 20
    if password:
        progress += 20
    if confirm_password:
        progress += 20
    if full_name:
        progress += 20
    if email:
        progress += 20
    return progress

# Cập nhật progress
progress = calculate_progress()
st.progress(progress)

# Kiểm tra tính hợp lệ
def validate_registration():
    if password != confirm_password:
        st.error("❌ Mật khẩu không khớp.")
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.error("❌ Email không hợp lệ.")
        return False
    return True

# Nút đăng ký
if st.button("Đăng ký"):
    if progress < 100:
        st.warning("⚠️ Vui lòng điền đầy đủ thông tin.")
    elif validate_registration():
        st.success("✅ Đăng ký thành công!")
        # Ở đây bạn có thể thêm logic lưu thông tin vào cơ sở dữ liệu
