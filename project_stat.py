import streamlit as st
import os

def render():
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)
    
    # 헤더 섹션
    st.title("고급 통계 분석 및 데이터 마이닝 포트폴리오")
    st.subheader("Text Mining | Factor Analysis | SEM | General Statistics")
    
    st.markdown("---")
    
    # 1. 분석 개요
    st.markdown("### 1. 분석 개요")
    
    col_info, _ = st.columns([1, 1])
    with col_info:
        st.markdown("""
        <table style="width: 100%; border-collapse: collapse; border: 1px solid #e5e7eb; font-size: 14.5px;">
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937; white-space: nowrap;">분석 영역</th>
                <td style="padding: 10px; color: #4b5563;">사회과학 데이터(정형·비정형), 사용자 만족도, 리뷰데이터 등</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">활용 도구</th>
                <td style="padding: 10px; color: #4b5563;">Python, R, SPSS, AMOS, SmartPLS</td>
            </tr>
            <tr>
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">핵심 역량</th>
                <td style="padding: 10px; color: #4b5563;">방대한 비정형 데이터 정량화 및 다변량 분석을 통한 인과관계 규명</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 스타일 정의 (공통 사용)
    st.markdown("""
    <style>
        .process-wrapper { display: flex; align-items: flex-start; margin-bottom: 35px; }
        .process-step { 
            width: 130px; height: 130px; background-color: #f8fafc; border: 2px solid #e2e8f0; 
            border-radius: 16px; display: flex; flex-direction: column; justify-content: center; 
            align-items: center; margin-right: 25px; flex-shrink: 0; box-shadow: 0 1px 3px rgba(0,0,0,0.05); 
        }
        .process-step h4 { margin: 0; color: #2563eb; font-size: 17px; font-weight: 800; }
        .process-step p { margin: 8px 0 0 0; font-size: 15px; color: #1f2937; font-weight: 700; text-align: center; line-height: 1.3; }
        .process-content { flex-grow: 1; padding-top: 5px; }
        .process-content ul { margin: 0; padding-left: 20px; color: #4b5563; font-size: 15px; line-height: 1.7; }
        .process-content li { margin-bottom: 8px; }
        .img-placeholder {
            width: 100%; height: 150px; background: #f8fafc; border: 1px dashed #e2e8f0; 
            border-radius: 10px; display: flex; justify-content: center; align-items: center; 
            color: #94a3b8; font-size: 13px; margin-top: 5px; text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. 분석 프로세스
    st.markdown("### 2. 주요 분석 프로세스")
    
    steps = [
        ("STEP 01", "텍스트<br>마이닝", [
            "<b>비정형 데이터 정제:</b> 웹 크롤링 및 설문 데이터 대상 불용어 제거 및 형태소 분석",
            "<b>키워드 네트워크:</b> TF-IDF 기반 핵심 키워드 도출 및 단어 간 연결 중심성 분석",
            "<b>구조-토픽 모델링:</b> STM 알고리즘을 활용한 잠재적 이슈 테마 분류 및 통계 분석"
        ]),
        ("STEP 02", "타당성 및<br>요인분석", [
            "<b>문헌 및 이론 탐색:</b> 국내외 선행연구 검토를 통한 분석 요인 도출 및 측정 문항의 이론적 근거 확보",
            "<b>탐색적 요인분석(EFA):</b> 다수의 변수를 공통된 잠재 요인으로 축소 및 차원성 검정",
            "<b>확인적 요인분석(CFA):</b> 측정 모델의 수렴 타당성 및 판별 타당성 최종 확보"
        ]),
        ("STEP 03", "구조방정식<br>(SEM)", [
            "<b>경로 분석:</b> 잠재 변수 간의 직접/간접 영향력 및 총 효과 산출",
            "<b>가설 검증:</b> 연구 가설에 대한 채택 여부 판정 및 모델 적합도(GFI, CFI, RMSEA 등) 평가",
            "<b>매개/조절 효과:</b> 변수 간 매개 효과 및 집단 간 조절 효과 분석"
        ]),
        ("STEP 04", "기타<br>추론 통계", [
            "<b>T-Test 차이 검정:</b> 독립표본 t-test 및 ANOVA를 활용한 집단 간 평균 차이 및 사후 검정 수행",
            "<b>회귀 분석:</b> 다중 회귀 모델을 통한 변수 간 인과관계 규명 및 설명력 확인 및 예측",
            "<b>데이터 시각화:</b> 분석 결과를 차트 및 그래프로 도식화"
        ])
    ]

    for h, p, items in steps:
        st.markdown(f"""
        <div class="process-wrapper">
            <div class="process-step"><h4>{h}</h4><p>{p}</p></div>
            <div class="process-content"><ul>{"".join([f"<li>{i}</li>" for i in items])}</ul></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. 분석 결과 예시
    st.markdown("### 3. 분석 결과 예시")
    
    # 함수 이름을 display_project_image 로 통일!
    def display_project_image(path, caption):
        if os.path.exists(path):
            _, mid, _ = st.columns([1, 3, 1]) 
            with mid:
                st.image(path, caption=caption, use_container_width=True)
        else:
            st.markdown(f"<div class='img-placeholder'>{caption}<br>(파일 대기 중: {path})</div>", unsafe_allow_html=True)

    # 호출할 때도 display_project_image 로 사용!
    st.markdown("#### ① 텍스트 마이닝 분석 (Word Cloud & Network)")
    c1_1, c1_2 = st.columns(2)
    with c1_1: display_project_image("./STAT/her-61-3-475_1.png", "작성 논문")
    with c1_2: display_project_image("./STAT/1._포트폴리오 (1)_13.png", "분석 예시")

    # 요인분석/SEM 섹션
    st.markdown("#### ② 요인분석")
    display_project_image("./STAT/요인분석.png", "요인분석 (예시)")

    #  구조방정식
    st.markdown("#### ③ 구조방정식")
    display_project_image("./STAT/sem.png", "SEM 분석 (예시)")
