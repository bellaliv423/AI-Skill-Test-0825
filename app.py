import streamlit as st
import random

# 점수 구간별 이름 정의
score_ranges = {
    (0, 10): "베이비 AI 돌잔치",
    (11, 20): "AI 유치원생",
    (21, 30): "AI 초등학생",
    (31, 40): "AI 중학생",
    (41, 50): "AI 고등학생",
    (51, 60): "AI 대학생",
    (61, 70): "AI 석사",
    (71, 80): "AI 박사",
    (81, 90): "AI 전문가",
    (91, 100): "AI 마스터"
}

# 테스트 질문 정의
questions = [
    "ChatGPT를 사용해 본 적이 있나요?",
    "Claude AI와 대화해 보셨나요?",
    "Google의 Gemini AI를 사용해 보셨나요?",
    "Midjourney로 이미지를 생성해 보셨나요?",
    "DALL-E로 그림을 그려보셨나요?",
    "GitHub Copilot을 코딩에 활용해 보셨나요?",
    "Canva의 AI 기능을 사용해 보셨나요?",
    "GAMMA 프레젠테이션 도구를 써보셨나요?",
    "AI 음성 합성 도구를 사용해 보셨나요?",
    "AI 번역 도구를 업무에 활용해 보셨나요?",
    "AI로 문서를 요약해 본 적이 있나요?",
    "AI 도구로 데이터 분석을 해보셨나요?",
    "AI 작문 도구로 글을 써보셨나요?",
    "AI 이미지 편집 도구를 사용해 보셨나요?",
    "AI 음악 생성 도구를 사용해 보셨나요?",
    "AI 스케줄링 도구를 활용해 보셨나요?",
    "AI 고객 서비스 챗봇을 만들어 보셨나요?",
    "AI로 개인화된 추천을 받아보셨나요?",
    "AI 음성 인식 기술을 사용해 보셨나요?",
    "AI 얼굴 인식 기술을 경험해 보셨나요?"
]

def calculate_score(answers):
    return sum(answers) * 5  # 각 질문당 5점씩, 총 100점 만점

def get_result(score):
    for (low, high), name in score_ranges.items():
        if low <= score <= high:
            return name
    return "알 수 없음"

def main():
    st.title("AI 생산성 활용 지수 레버 테스트")
    st.write("AI 도구 사용 경험을 바탕으로 당신의 AI 활용 수준을 측정합니다!")

    if 'page' not in st.session_state:
        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.start_time = None

    if st.session_state.page == 0:
        st.write("테스트를 시작하려면 '시작' 버튼을 클릭하세요.")
        if st.button("시작"):
            st.session_state.page = 1
            st.session_state.start_time = st.session_state.time()
            st.experimental_rerun()

    elif 1 <= st.session_state.page <= len(questions):
        question = questions[st.session_state.page - 1]
        st.write(f"질문 {st.session_state.page}/{len(questions)}: {question}")
        answer = st.radio("", ("예", "아니오"), key=f"q{st.session_state.page}")
        
        if st.button("다음" if st.session_state.page < len(questions) else "결과 보기"):
            st.session_state.answers.append(1 if answer == "예" else 0)
            st.session_state.page += 1
            st.experimental_rerun()

    else:
        score = calculate_score(st.session_state.answers)
        result = get_result(score)
        
        st.write(f"당신의 점수: {score}점")
        st.write(f"당신의 AI 활용 레벨: {result}")
        
        advice = "AI 기술에 더 관심을 가져보세요!" if score < 50 else "훌륭합니다! AI를 잘 활용하고 계시네요."
        st.write(advice)
        
        if st.button("다시 시작"):
            st.session_state.page = 0
            st.session_state.answers = []
            st.session_state.start_time = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()