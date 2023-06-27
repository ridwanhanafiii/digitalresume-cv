# Import Library
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "doc" / "CV Muhammad Dandri Handian.pdf"
profile_pic = current_dir / "doc" / "Profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Muhammad Dandri Handian"
PAGE_ICON = ":wave:"
NAME = "Muhammad Dandri Handian"
DESCRIPTION = """
Perkenalkan nama saya Muhammad Dandri Handian,
saya adalah seorang anak laki – laki ke enam dari tujuh bersaudara.
Latar belakang pendidikan sistem informasi dan memiliki keahlian pemrograman.

"""
EMAIL = "muhammaddandrihandian@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/",
    "LinkedIn": "https://www.linkedin.com/",
    "GitHub": "https://github.com/",
    "Instagram": "https://instagram.com/",
}
PROJECTS = {
    "🏆 Belajar Streamlit [Dasar] - Belajar Dasar sampai Membuat Aplikasi Machine Learning": "https://www.youtube.com/",
    "🏆 Modeling For Chatbot - Web app menggunakan Python Flask": "https://www.youtube.com/",
    "🏆 Membuat Chatbot Menggunakan NLP - Web app menggunakan Python Flask": "https://www.youtube.com/",
    "🏆 Membuat Chatbot Menggunakan Streamlit - Web app menggunakan Model ChatGPT": "https://www.youtube.com/",
    "🏆 Deploy Dengan Streamlit Cloud - Web app Multi Page menggunakan Streamlit": "https://www.youtube.com/",
    "🏆 Membuat Auto Machine Learning - Web app menggunakan Streamlit": "https://www.youtube.com/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Bagian pengaturan foto profile ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=260)
    st.write("Photographer | Video Editor | Content Creator")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Curicullum Vitae",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 9 tahun berpengalaman berbagai macam video editing.
- ✔️ 5 tahun berpengalaman dalam bidang IT.
- ✔️ Berpengalaman sebai Photographer di berbagai macam Event Besar.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Editing
- 📊 Photographer
- 📚 Content Creator
- 🗄️ Leadership
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Coach Video Editor | PT Teknologi Lokal IND**")
st.write("2021 - Sekarang")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Trainer Video Editor | PT Prima Jaya Teknologi**")
st.write("2020 - 2021")
st.write(
    """
- ► Memastikan hasil video
- ► Bisa menempuh Deadline yang di inginkan client
- ► Colour grading sesuai dengan konsep yang diterima
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**IT Support Application | PT Datasynthesis**")
st.write("2019 - 2020")
st.write(
    """
- ► Menjaga dan memantau aplikasi yang ada.
- ► Dukungan mengembangkan fitur baru untuk aplikasi yang ada.
- ► Berkomunikasi dengan divisi lain mengenai masalah teknis.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Assistant Trainer | Yayasan Komunitas Open Source**")
st.write("2019 - 2019")
st.write(
    """
- ► Pelatihan dan Pengembangan SDM.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Staff Network Operations Center (NOC) | PT. Skyreach**")
st.write("2018 - 2019")
st.write(
    """
- ► Mengontrol dan Monitoring semua site.
- ► Melakukan Troubelshoot dan Membuat report.
"""
)

# --- JOB 6
st.write('\n')
st.write("🚧", "**Supervisor Produksi Premik & Supply Chain | PT. Dapur Solo Sukses Sejati**")
st.write("2009 - 2018")
st.write(
    """
- ► Bertanggung jawab terhadap hal-hal yang berhubungan dengan jalanya oprasional.
- ► Membuat laporan setiap bulan.
- ► Mengontrol proses penimbangan bumbu premik.
- ► Menjaga kualitas dan kuantitas bumbu premik.
- ► Memastikan semua oprasional berjalan dengan baik dan sesuai SOP.
"""
)


# --- Projects & Pencapaian ---
st.write('\n')
st.subheader("Projects & Pencapaian")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
