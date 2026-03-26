import streamlit as st
import os

def render():
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)
    
    # 헤더 섹션
    st.title("농업연구개발사업 종합성과분석 및 중간평가 대응")
    st.subheader("농촌진흥청(RDA) | 2025.05 - 2025.12")
    
    st.markdown("---")
    
    # 1. 사업 개요
    st.markdown("### 1. 사업 개요")
    
    col_info, _ = st.columns([1, 1])
    with col_info:
        st.markdown("""
        <table style="width: 100%; border-collapse: collapse; border: 1px solid #e5e7eb; font-size: 14.5px;">
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937; white-space: nowrap;">발주처</th>
                <td style="padding: 10px; color: #4b5563;">농촌진흥청 (RDA)</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 역할</th>
                <td style="padding: 10px; color: #4b5563;"><b>총괄 PL (Project Leader)</b></td>
            </tr>
            <tr>
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 목적</th>
                <td style="padding: 10px; color: #4b5563;">농촌진흥청 소관 6개 R&D 사업의 '26년 국가연구개발사업 중간평가 전략적 대응 및 성과 체계화</td>
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
    
    # 농진청 보고서 기반 과업 정의
    steps = [
        ("STEP 01", "중간평가<br>대응", [
            "<b>평가 지침 분석:</b> 과기정통부 국가연구개발사업 중간평가 지침 분석 및 평가 항목별 대응 전략 수립",
            "<b>평가 논리 설계:</b> 대상 사업별 사업 추진의 타당성 및 우수성을 강조를 위한 방어 논리 개발",
            "<b>대응 시나리오 구축:</b> 과거 평가 의견 분석을 통한 사업별 맞춤형 소명 전략 및 증빙 체계 마련"
        ]),
        ("STEP 02", "성과 데이터<br>셋 분석", [
            "<b>데이터셋 고도화:</b> 사업별 데이터 취합 및 표준화 작업 수행",
            "<b>성과 무결성 검증:</b> '25년 말까지 창출된 농업 R&D 성과 실적의 목표 대비 달성도 검증",
            "<b>성과 지표 모니터링:</b> 중간평가 핵심 지표 중심의 질적 성과 및 증빙 자료 매칭"
        ]),
        ("STEP 03", "자체평가<br>보고서 집필", [
            "<b>보고서 초안 집필:</b> 사업 추진 계획 대비 효율성, 효과성, 과학기술적 타당성을 입증하는 보고서 작성",
            "<b>성과 스토리텔링:</b> 단순 정량 수치를 넘어 농업 현장의 문제 해결 및 기술 확산 성과를 정성적으로 서술",
            "<b>전문가 환류:</b> 자체평가위원회 및 외부 전문가 검토 의견을 반영한 보고서 보완 및 최종본 완성"
        ]),
        ("STEP 04", "평가 지원<br> 및 교육", [
            "<b>작성 가이드라인 배포:</b> 사업 담당자 대상 자체평가보고서 작성 매뉴얼 및 성과 증빙 관리 교육 수행",
            "<b>평가 대응 컨설팅:</b> 평가위원 예상 질의(Q&A) 도출 및 성과 미달성 지표에 대한 전략적 소명 논리 컨설팅",
            "<b>역량 강화 세미나:</b> 농촌진흥청 전문가위원회/분과위원회/총괄위원회 대상 국가 R&D 평가 체계 이해도 제고 세미나 운영"
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

    # 산출물 1
    st.markdown("#### 1. 2026년 농업연구개발사업 종합성과분석보고서")
    c1_1, c1_2 = st.columns(2)
    with c1_1: display_project_image("./RDA/4. 2026_종합성과분석보고서_농촌진흥청_지역농업연구기반및전략작목육성(지역지원)_1.png", "보고서 표지")
    with c1_2: display_project_image("./RDA/4. 2026_종합성과분석보고서_농촌진흥청_지역농업연구기반및전략작목육성(지역지원)_16.png", "보고서 내지(예시)")

    # 산출물 2
    st.markdown("#### 2. 2026년 농업연구개발사업 자체평가보고서")
    c2_1, c2_2 = st.columns(2)
    with c2_1: display_project_image("./RDA/4. 2026_자체평가보고서_농촌진흥청_지역농업연구기반및전략작목육성(RD 보조 지역지원)_1.png", "보고서 표지")
    with c2_2: display_project_image("./RDA/4. 2026_자체평가보고서_농촌진흥청_지역농업연구기반및전략작목육성(RD 보조 지역지원)_50.png", "보고서 내지(예시)")

   # 산출물 3 (단일 배치 + 2/3 크기)
    st.markdown("#### 3. 전문가/평가위원 교육")
    display_project_image("./RDA/(교육자료) 국가연구개발사업 중간평가 자체평가위원회 사전 교육(최종)_8.png", "교육 자료(예시)")