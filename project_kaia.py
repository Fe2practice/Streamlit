import streamlit as st
import os

def render():
    st.markdown("<div id='top'></div>", unsafe_allow_html=True)
    
    # 헤더 섹션
    st.title("국토교통 R&D 성과조사·분석")
    st.subheader("국토교통과학기술진흥원(KAIA) | 2024.01 - 2025.02")
    
    st.markdown("---")
    
    # 1. 사업 개요
    st.markdown("### 1. 사업 개요")
    
    col_info, _ = st.columns([1, 1])
    with col_info:
        st.markdown("""
        <table style="width: 100%; border-collapse: collapse; border: 1px solid #e5e7eb; font-size: 14.5px;">
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937; white-space: nowrap;">발주처</th>
                <td style="padding: 10px; color: #4b5563;">국토교통과학기술진흥원 (KAIA)</td>
            </tr>
            <tr style="border-bottom: 1px solid #e5e7eb;">
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 역할</th>
                <td style="padding: 10px; color: #4b5563;"><b>총괄 PL (Project Leader)</b></td>
            </tr>
            <tr>
                <th style="width: 120px !important; background-color: #f8fafc; padding: 10px; border-right: 1px solid #e5e7eb; text-align: center; color: #1f2937;">수행 목적</th>
                <td style="padding: 10px; color: #4b5563;">국토교통 R&D 성과 중심의 효율적 관리 체계 구축 및 성과평가·기관 경영평가 적기 대응</td>
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
    
    steps = [
        ("STEP 01", "성과조사<br> 및 검증", [
            "<b>성과조사·검증 거점 운영:</b> 연구책임자 대상 성과 입력 안내 및 온/오프라인 성과조사 콜센터·검증센터 운영 총괄",
            "<b>데이터 조사·수집:</b> 범부처연구관리시스템(IRIS) 기반의 국토교통 R&D 성과 수집·관리",
            "<b>데이터 검증:</b> 입력 실적과 증빙자료 대조를 통한 오기재, 누락, 중복 실적 필터링 및 DB 확정"
        ]),
        ("STEP 02", "종합 분석", [
            "<b>달성도 분석:</b> 성과 목표 대비 실제 달성 현황 분석 및 지표별 추이 분석",
            "<b>성과 통계 DB 구축:</b> 과학적(논문 mrnIF), 기술적(특허 SMART 등급) 등 정성적 성과 현황 DB 구축",
            "<b>통계 보고서 발간:</b> 국토교통 R&D 성과편/투입편 통계 데이터 시각화 및 분석 리포트 작성"
        ]),
        ("STEP 03", "심층 분석", [
            "<b>파급효과 산출:</b> R&D 투입 예산 대비 경제적 파급효과(매출, 고용 등) 및 과학기술적 파급효과 분석",
            "<b>전문가 위원회 기획·운영:</b> 산·학·연 전문가 위원회 운영을 통한 주요 사업별 기술적 우수성 및 현장 적용성 심층 평가",
            "<b>사업·과제 효율성 분석:</b> 사업·과제별 투입 대비 성과 창출 효율성 비교 분석 및 예산 배분 근거 자료 제공"
        ]),
        ("STEP 04", "기타 지원", [
            "<b>성과활용평가 시범적용:</b> 종료 과제 대상 추적 조사를 통한 성과 활용 실태 점검 및 프레임워크 적용",
            "<b>성과 확산:</b> 국토교통 R&D 대표 우수성과 선정 프로세스 운영 및 스토리텔링 기반 우수성과 사례집 제작 지원",
            "<b>AI 활용 능동적 성과 수집:</b> Open-AI API를 활용하여 추가 성과 발굴 기획 및 실증 수행"
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
            # 🎯 2/3 크기 조절: 좌우 1/6씩 여백을 주어 중앙 4/6(약 66.6%) 사용
            _, mid, _ = st.columns([1, 3, 1])
            with mid:
                st.image(path, caption=caption, use_container_width=True)
        else:
            st.markdown(f"<div class='img-placeholder'>{caption}<br>(파일 대기 중: {path})</div>", unsafe_allow_html=True)

    # 산출물 1
    st.markdown("#### 1. 국토교통 R&D 성과편/투입편 종합분석 보고서")
    c1_1, c1_2 = st.columns(2)
    with c1_1: display_project_image("./KAIA/2024 국토교통 성과편_내지_최종_1.png", "보고서 표지")
    with c1_2: display_project_image("./KAIA/2024 국토교통 성과편_내지_최종_57.png", "보고서 내지(예시)")

    # 산출물 2
    st.markdown("#### 2. 국토교통 R&D 성과증감원인 심층분석보고서")
    c2_1, c2_2 = st.columns(2)
    with c2_1: display_project_image("./KAIA/2024 국토교통 성과증감원인분석보고서_내지_최종_1.png", "보고서 표지")
    with c2_2: display_project_image("./KAIA/2024 국토교통 성과증감원인분석보고서_내지_최종_34.png", "보고서 내지(예시)")

    # 산출물 3
    st.markdown("#### 3. 성과활용평가보고서 및 사례집")
    c3_1, c3_2 = st.columns(2)
    with c3_1: display_project_image("./KAIA/2024 국토교통 성과활용평가보고서_내지_최종_1.png", "보고서 표지")
    with c3_2: display_project_image("./KAIA/2024 국토교통 성과활용평가보고서_내지_최종_96.png", "사례집 (예시)")

    # 산출물 4 (단일 배치 + 2/3 크기)
    st.markdown("#### 4. AI 활용 프로세스 기획·개발·운영")
    display_project_image("./KAIA/도식화_인포그래픽.png", "AI 기반 성과 발굴 도식화")
    