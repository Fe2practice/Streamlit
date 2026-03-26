import os
import base64
import pandas as pd
import streamlit as st
import project_ch
import project_kaia
import project_keit
import project_rda
import project_stat

st.set_page_config(
    page_title="이철의 포트폴리오",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"] { font-family: Pretendard, sans-serif; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
.topbar { position: sticky; top: 0; z-index: 99; background: #ffffffcc; backdrop-filter: blur(6px); padding: 10px 14px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; }
.topbar a { margin: 0 8px; color: #111 !important; text-decoration: none !important; font-weight: 600; background: none !important; padding: 4px 6px; font-size: 15px; }
.topbar a:hover { color: #2563eb !important; }
.hero { padding: 50px 0 40px 0; text-align: center; background: #0f172a; color: #fff; border-radius: 16px; margin: 12px 0; }
.hero h1 { margin: 0; color: #fff; }
a { color: inherit !important; text-decoration: none !important; }
.chip { display: inline-block; padding: 6px 12px; border-radius: 999px; background: #f1f5f9; margin: 4px; font-size: 13px; font-weight: 600; color: #334155; }
.tl { border-left: 3px solid #94a3b8; padding-left: 12px; margin: 6px 0; }
table { width: 100% !important; border-collapse: collapse; border: 1px solid #e5e7eb !important; border-radius: 10px; overflow: hidden; }
th { width: 30% !important; background-color: #f8fafc !important; color: #1f2937 !important; text-align: center !important; padding: 6px 10px !important; }
td { width: 70% !important; white-space: pre-wrap !important; color: #4b5563 !important; padding: 6px 10px !important; }
td a { color: inherit !important; text-decoration: none !important; pointer-events: none; }
.logo-btn { transition: all 0.3s ease; display: block; border-radius: 8px; cursor: pointer; }
.logo-btn:hover { transform: translateY(-5px); }
.logo-btn img { transition: all 0.3s ease; }
.logo-btn:hover img { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5); border-color: #60a5fa !important; }
.logo-btn:hover p { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

try:
    section = st.query_params.get("section", "home")
    if isinstance(section, list): section = section[0]
except:
    section = "home"

valid_sections = ["home", "intro", "kaia", "keit", "rda", "stat"]
if section not in valid_sections: section = "home"

st.markdown(f"""
<div class='topbar'>
  <div><b>2026.03.20. 업데이트</b></div>
  <div>
    <a href='?section=home#top' target='_self'>홈</a>
    <a href='?section=kaia#top' target='_self'>KAIA</a>
    <a href='?section=keit#top' target='_self'>KEIT</a>
    <a href='?section=rda#top' target='_self'>RDA</a>
    <a href='?section=stat#top' target='_self'>통계분석</a>
    <a href='?section=intro#top' target='_self'>자기소개서</a>

  </div>
</div>
""", unsafe_allow_html=True)

def render_home():
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)
    
    kaia_img = get_base64_of_bin_file('KAIA_로고.png')
    keit_img = get_base64_of_bin_file('KEIT_로고.png')
    rda_img = get_base64_of_bin_file('농진청_로고.jpg')
    stat_img = get_base64_of_bin_file('통계분석_로고.png')
    intro_img = get_base64_of_bin_file('자기소개서_로고.png')
    
    st.markdown(f"""
    <div class='hero'>
      <h1>냉정한 데이터와 따듯한 스토리. 기획부터 개발, 분석까지. 준비된 융합형 인재</h1>
      <p style='opacity:.85; margin-top:10px; margin-bottom:15px;'>AI기획 · 분석기획 · 데이터전처리 · Python · 통계분석 · 자동화 · 스토리텔링</p>
      <p style='font-size: 14px; color: #94a3b8; margin-bottom: 25px;'>각 프로젝트 로고를 클릭하시면 상세 페이지로 이동합니다.</p>
      
      <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
        <a href='?section=kaia#top' target='_self' class='logo-btn' style='width: 90px;'>
          <img src='data:image/png;base64,{kaia_img}' style='width: 100%; border-radius: 8px; border: 1px solid #334155; background: white; display: block;'>
          <p style='color: #cbd5e1; font-size: 13px; font-weight: 600; margin: 8px 0 0 0;'>KAIA(PL·PA)</p>
        </a>
        <a href='?section=keit#top' target='_self' class='logo-btn' style='width: 90px;'>
          <img src='data:image/png;base64,{keit_img}' style='width: 100%; border-radius: 8px; border: 1px solid #334155; background: white; display: block;'>
          <p style='color: #cbd5e1; font-size: 13px; font-weight: 600; margin: 8px 0 0 0;'>KEIT(PL)</p>
        </a>
        <a href='?section=rda#top' target='_self' class='logo-btn' style='width: 90px;'>
          <img src='data:image/jpeg;base64,{rda_img}' style='width: 100%; border-radius: 8px; border: 1px solid #334155; background: white; display: block;'>
          <p style='color: #cbd5e1; font-size: 13px; font-weight: 600; margin: 8px 0 0 0;'>농진청(PL)</p>
        </a>
        <a href='?section=stat#top' target='_self' class='logo-btn' style='width: 90px;'>
          <img src='data:image/png;base64,{stat_img}' style='width: 100%; border-radius: 8px; border: 1px solid #334155; background: white; display: block;'>
          <p style='color: #cbd5e1; font-size: 13px; font-weight: 600; margin: 8px 0 0 0;'>통계분석</p>
        </a>
        <a href='?section=intro#top' target='_self' class='logo-btn' style='width: 90px;'>
          <img src='data:image/png;base64,{intro_img}' style='width: 100%; border-radius: 8px; border: 1px solid #334155; background: white; display: block;'>
          <p style='color: #cbd5e1; font-size: 13px; font-weight: 600; margin: 8px 0 0 0;'>자기소개서</p>
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    colA, colB, colC = st.columns([0.6, 1.4, 1.4])
    with colA: st.image("프로필.jpg", use_container_width=True)
    with colB:
        st.markdown("### 개인 소개")
        profile_data = {
            "항목": ["이름", "나이", "학력", "Email", "Phone"],
            "내용": ["이철", "만 29세(1996년생)", "성균관대학교 석사 졸업(2024)\n강원대학교 화학과 학사 졸업(2021)", "8101034@gmail.com", "010-5160-9745"]
        }
        st.table(pd.DataFrame(profile_data).set_index("항목"))
        st.markdown("### 핵심 역량")
        skills = ["AI기획","분석기획","Python","데이터전처리","통계분석","업무자동화"]
        st.markdown(" ".join([f"<span class='chip'>{s}</span>" for s in skills]), unsafe_allow_html=True)
    with colC:
        st.markdown("### 약력 요약")
        timeline = [
            ("2026", "• 농진청 성과분석 총괄 PL"),
            ("2025", "• 국토교통 R&D 성과조사·분석 총괄 PL (KAIA)<br>• (주)다윈전략컨설팅 선임연구원 진급<br>• KEIT 전담관리 R&D사업 성과평가대응 총괄 PL"),
            ("2024", "• 국토교통 R&D 성과조사·분석 연구 참여 (KAIA)<br>• (주)다윈전략컨설팅 전임연구원 입사<br>• 성균관대학교 석사 졸업<br>• (주)호시담 퇴사"),
            ("2023", "• (주)호시담 입사"),
            ("2021", "• 성균관대학교 소셜이노베이션융합전공(소비자학) 석사 입학<br>• 강원대학교 화학과 학사 졸업"),
            ("2016-2018", "• 군 복무(육군)"),
            ("2015", "• 강원대학교 화학과 학사 입학")
        ]
        for y, txt in timeline:
            st.markdown(f"<div class='tl' style='margin-top:15px;'><h4>{y}</h4><p style='line-height:1.6; margin-top:5px;'>{txt}</p></div>", unsafe_allow_html=True)

if section == "home": render_home()
elif section == "intro": project_ch.render()
elif section == "kaia":
    try: project_kaia.render()
    except ImportError: st.error("project_kaia.py 파일이 필요합니다.")
elif section == "keit":
    try: project_keit.render()
    except ImportError: st.error("project_keit.py 파일이 필요합니다.")
elif section == "rda":
    try: project_rda.render()
    except ImportError: st.error("project_rda.py 파일이 필요합니다.")
elif section == "stat":
    try: project_stat.render()
    except ImportError: st.error("project_stat.py 파일이 필요합니다.")

st.markdown("<hr><p style='text-align:center; opacity:.6;'>© 2026 이철 8101034@gmail.com</p>", unsafe_allow_html=True)
