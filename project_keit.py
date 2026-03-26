import streamlit as st
import os

def render():
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)
    
    # 헤더 섹션
    st.title("KEIT 전담관리 R&D사업 성과평가대응")
    st.subheader("한국산업기술기획평가원(KEIT) | 2025.04 - 2026.03")
    
    st.markdown("---")
    
    # 1. 사업 개요
    st.markdown("### 1. 사업 개요")
    
    col_info, _ = st.columns([1, 1])
    with col_info:
        st.markdown("""
        <table style="width: 100%; border-collapse: collapse; border: 1px solid #e5e7eb; font-size: 14.5px;">
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937; white-space: nowrap;">발주처</th>
                <td style="padding: 10px; color: #4b5563;">한국산업기술기획평가원 (KEIT)</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 역할</th>
                <td style="padding: 10px; color: #4b5563;"><b>총괄 PL (Project Leader)</b></td>
            </tr>
            <tr>
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 목적</th>
                <td style="padding: 10px; color: #4b5563;">KEIT 전담 R&D 사업의 국가연구개발사업 성과평가 능동적 대응 및 성과관리 체계 고도화</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 스타일 정의
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

    st.markdown("### 2. 세부 과업 수행 내용")
    
    # KEIT 보고서 목차 기반 과업 정의
    steps = [
        ("STEP 01", "성과관리·<br>활용계획", [
            "<b>전략계획서 분석:</b> 과기정통부 평가 지침에 따른 사업별 전략계획서 및 성과목표 적정성 검토",
            "<b>논리모형 고도화:</b> 사업별 투입-활동-산출-성과-파급효과 간의 인과관계 재정립",
            "<b>성과관리 계획 수립:</b> 차기 성과평가 대응을 위한 연차별 성과관리 및 활용 고도화 전략 수립"
        ]),
        ("STEP 02", "효과성 분석", [
            "<b>산업적 파급효과 분석:</b> R&D 지원을 통한 매출 창출, 고용 확대 등 경제적 성과 데이터 분석",
            "<b>기술적 우수성 입증:</b> 특허 질적 수준(SMART 등급) 및 글로벌 기술 대비 우위성 분석",
            "<b>사회적 기여도 산출:</b> 정책 부합성 및 공공 분야 기여도 등 정성적 성과의 정량화 시도"
        ]),
        ("STEP 03", "성과지표 개발", [
            "<b>신산업 특화 지표 기획:</b> AI 도입, 탄소중립 등 신(新)산업 R&D 특성을 반영한 질적 성과 측정 지표 개발",
            "<b>질적 성과 측정 모델 설계:</b> 단순 수치 분석을 넘어선 연구 과정의 역량 변화 및 생태계 형성 수준 측정 모델 설계",
            "<b>품질평가회 및 세미나 기획·운영:</b> 신규 지표의 현장 적용성 및 타당성 검증을 위한 전문가 품질평가회 및 세미나 개최"
        ]),
        ("STEP 04", "평가 대응<br>컨설팅", [
            "<b>자체평가보고서 집필:</b> 과기정통부 중간평가 및 효과성 분석 대응을 위한 자체평가보고서 작성 지원",
            "<b>평가 전략 시나리오 수립:</b> 평가위원 예상 평가의견 도출 및 방어 논리 개발",
            "<b>평가 대응 교육:</b> 사업 담당자 및 연구책임자 대상 평가 대응 총괄"
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

    # 3. 주요 산출물 및 시각화
    st.markdown("### 3. 주요 산출물")
    
    def display_project_image(path, caption):
        if os.path.exists(path):
            _, mid, _ = st.columns([1, 3, 1])
            with mid:
                st.image(path, caption=caption, use_container_width=True)
        else:
            st.markdown(f"<div class='img-placeholder'>{caption}<br>(파일 대기 중: {path})</div>", unsafe_allow_html=True)

    # 산출물 1 (단일 배치 + 2/3 크기)
    st.markdown("#### 1. 과업 일정 관리")
    display_project_image("./KEIT/과업 관리.png", "과업 일정 관리")
    
    # 산출물 2
    st.markdown("#### 2. KEIT 전담관리 R&D사업 성과관리활용계획 보고서")
    c1_1, c1_2 = st.columns(2)
    with c1_1: display_project_image("./KEIT/2025_2차성과관리활용계획서_산업부_영상진단의료기기탑재용AI기반영상분석솔루션개발_1.png", "보고서 표지")
    with c1_2: display_project_image("./KEIT/2025_2차성과관리활용계획서_산업부_영상진단의료기기탑재용AI기반영상분석솔루션개발_8.png", "보고서 내지(예시)")

    # 산출물 3
    st.markdown("#### 3. KEIT 전담관리 R&D사업 효과성분석 보고서")
    c2_1, c2_2 = st.columns(2)
    with c2_1: display_project_image("./KEIT/2025_1차효과성분석보고서_산업부_산업현장핵심기술수시개발_1.png", "보고서 표지")
    with c2_2: display_project_image("./KEIT/2025_1차효과성분석보고서_산업부_산업현장핵심기술수시개발_16.png", "보고서 내지(예시)")

    # 산출물 4
    st.markdown("#### 4. AI도입·탄소중립 특화 질적 성과지표 개발보고서")
    c3_1, c3_2 = st.columns(2)
    with c3_1: display_project_image("./KEIT/1.탄소중립·AI 도입 성과지표 개발 결과보고서_260324(최종)_1.png", "보고서 표지")
    with c3_2: display_project_image("./KEIT/1.탄소중립·AI 도입 성과지표 개발 결과보고서_260324(최종)_45.png", "보고서 내지(예시)")
    