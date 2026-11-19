import streamlit as st
import yfinance as yf

# 1. 웹페이지 제목 만들기
st.title("☀️ 매일 아침 8시! 나만의 매크로 대시보드")
st.write("밤사이 미국 시장과 원자재 흐름을 한눈에 확인하세요.")

# 2. 데이터 가져오기 (야후 파이낸스 티커 코드)
# CL=F (WTI 유가), ^TNX (미국 10년물 금리), NQ=F (나스닥 100 선물)
tickers = {
    "🛢️ WTI 유가 ($)": "CL=F",
    "🏦 미국 10년물 금리 (%)": "^TNX",
    "📈 나스닥 100 선물": "NQ=F",
}

# 화면을 3칸으로 나누기
cols = st.columns(3)

# 3. 각 지표별 데이터 뽑아서 화면에 그리기
for i, (name, ticker) in enumerate(tickers.items()):
  # 최근 1개월 치 데이터 가져오기
  data = yf.Ticker(ticker).history(period="1mo")

  # 어제와 오늘 가격 비교해서 등락률 계산
  today_price = data["Close"].iloc[-1]
  yesterday_price = data["Close"].iloc[-2]
  diff = today_price - yesterday_price

  # 화면에 숫자와 차트 띄우기
  with cols[i]:
    st.metric(
        label=name, value=f"{today_price:.2f}", delta=f"{diff:.2f} (전일 대비)"
    )
    st.line_chart(data["Close"])

# 4. 밤사이 미국 뉴스 요약 공간
st.divider()
st.subheader("📰 AI가 요약한 밤사이 미국 핵심 뉴스")
st.info("""
* **반도체 섹터 강세:** 엔비디아 실적 기대로 필라델피아 반도체 지수 상승 -> **오늘 국내 반도체 주가 긍정적 영향 예상**
* **유가 안정세:** WTI 유가 하락으로 인플레이션 우려 완화
""")