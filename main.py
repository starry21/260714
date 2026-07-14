import streamlit as st

# ------------------------------------------------------------------
# MBTI별 추천 직업 & 포켓몬 매칭 데이터
# 이미지는 PokeAPI 공식 스프라이트 저장소(GitHub raw)에서 URL로 바로 불러옵니다.
# ------------------------------------------------------------------

def pokemon_image_url(pokedex_id: int) -> str:
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{pokedex_id}.png"
    )

MBTI_DATA = {
    "INTJ": {
        "career": "데이터 사이언티스트 / 전략 기획자",
        "reason": "치밀한 분석력과 장기적인 전략 수립 능력이 뛰어난 유형입니다.",
        "pokemon": "뮤츠",
        "pokedex_id": 150,
        "pokemon_reason": "압도적인 지능과 냉철한 판단력을 지닌 전설의 포켓몬입니다.",
    },
    "INTP": {
        "career": "연구원 / 데이터 엔지니어",
        "reason": "논리적 사고와 끝없는 호기심으로 문제의 본질을 파고듭니다.",
        "pokemon": "폴리곤",
        "pokedex_id": 137,
        "pokemon_reason": "데이터로 만들어진 포켓몬으로, 논리와 분석을 상징합니다.",
    },
    "ENTJ": {
        "career": "경영 컨설턴트 / CEO",
        "reason": "타고난 리더십과 추진력으로 조직을 이끄는 데 강점이 있습니다.",
        "pokemon": "리자몽",
        "pokedex_id": 6,
        "pokemon_reason": "강력한 카리스마와 압도적인 파워로 무리를 이끄는 포켓몬입니다.",
    },
    "ENTP": {
        "career": "스타트업 창업가 / 기획자",
        "reason": "번뜩이는 아이디어와 임기응변 능력이 뛰어난 혁신가입니다.",
        "pokemon": "조로아크",
        "pokedex_id": 571,
        "pokemon_reason": "재치있고 영리하게 변신하며 상황을 유리하게 이끕니다.",
    },
    "INFJ": {
        "career": "심리 상담가 / 사회운동가",
        "reason": "깊은 통찰력과 타인에 대한 공감 능력이 뛰어난 유형입니다.",
        "pokemon": "뮤",
        "pokedex_id": 151,
        "pokemon_reason": "신비롭고 온화하며 모든 포켓몬의 원형이라 불리는 존재입니다.",
    },
    "INFP": {
        "career": "작가 / 예술가",
        "reason": "풍부한 상상력과 따뜻한 감성으로 창작 활동에 강점을 보입니다.",
        "pokemon": "폭야옹(브이젤·실비온)",
        "pokedex_id": 700,
        "pokemon_reason": "부드럽고 따뜻한 기운으로 주변을 감싸는 페어리 포켓몬입니다.",
    },
    "ENFJ": {
        "career": "교사 / 코치",
        "reason": "타인의 성장을 돕고 이끄는 데 열정을 쏟는 리더형입니다.",
        "pokemon": "루카리오",
        "pokedex_id": 448,
        "pokemon_reason": "아우라를 통해 상대를 이해하고 이끄는 스승 같은 포켓몬입니다.",
    },
    "ENFP": {
        "career": "마케터 / 이벤트 기획자",
        "reason": "밝은 에너지와 사교성으로 사람들을 즐겁게 이끄는 유형입니다.",
        "pokemon": "피카츄",
        "pokedex_id": 25,
        "pokemon_reason": "활발하고 친근한 에너지로 모두에게 사랑받는 포켓몬입니다.",
    },
    "ISTJ": {
        "career": "회계사 / 공무원",
        "reason": "꼼꼼하고 체계적이며 원칙을 중시하는 신뢰의 상징입니다.",
        "pokemon": "메타그로스",
        "pokedex_id": 376,
        "pokemon_reason": "정밀한 계산 능력을 지닌 강철 타입의 신뢰할 수 있는 포켓몬입니다.",
    },
    "ISFJ": {
        "career": "간호사 / 사회복지사",
        "reason": "헌신적이고 세심하게 타인을 보살피는 데 강점이 있습니다.",
        "pokemon": "럭키",
        "pokedex_id": 113,
        "pokemon_reason": "따뜻한 마음으로 다친 이를 돌보는 것으로 유명한 포켓몬입니다.",
    },
    "ESTJ": {
        "career": "프로젝트 매니저 / 관리자",
        "reason": "체계적인 관리 능력과 책임감으로 조직을 안정적으로 운영합니다.",
        "pokemon": "강철톤",
        "pokedex_id": 208,
        "pokemon_reason": "단단하고 규율 있는 강철 타입으로 안정감을 상징합니다.",
    },
    "ESFJ": {
        "career": "인사(HR) 담당자 / 이벤트 매니저",
        "reason": "따뜻한 배려심과 사교성으로 공동체를 잘 챙기는 유형입니다.",
        "pokemon": "밀탱크",
        "pokedex_id": 241,
        "pokemon_reason": "주변을 보살피고 영양을 나눠주는 다정한 포켓몬입니다.",
    },
    "ISTP": {
        "career": "엔지니어 / 정비사",
        "reason": "손재주가 뛰어나고 문제를 직접 해결하는 실용적인 유형입니다.",
        "pokemon": "로토무",
        "pokedex_id": 479,
        "pokemon_reason": "전자기기를 자유자재로 다루는 기술형 포켓몬입니다.",
    },
    "ISFP": {
        "career": "디자이너 / 사진작가",
        "reason": "섬세한 미적 감각과 자유로운 감성을 지닌 예술가형입니다.",
        "pokemon": "밀로틱",
        "pokedex_id": 350,
        "pokemon_reason": "아름다운 자태로 유명하며 예술적 영감을 주는 포켓몬입니다.",
    },
    "ESTP": {
        "career": "영업 전문가 / 사업가",
        "reason": "과감한 실행력과 순발력으로 기회를 빠르게 포착합니다.",
        "pokemon": "초염몽",
        "pokedex_id": 392,
        "pokemon_reason": "뜨거운 열정과 폭발적인 행동력을 지닌 포켓몬입니다.",
    },
    "ESFP": {
        "career": "배우 / 엔터테이너",
        "reason": "타고난 끼와 사교성으로 무대 위에서 빛나는 유형입니다.",
        "pokemon": "푸크린",
        "pokedex_id": 40,
        "pokemon_reason": "노래로 모두를 즐겁게 만드는 흥 넘치는 포켓몬입니다.",
    },
}

# ------------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------------

st.set_page_config(page_title="MBTI 직업 & 포켓몬 추천", page_icon="✨", layout="centered")

st.title("✨ MBTI 기반 직업 & 포켓몬 추천기")
st.write("MBTI를 선택하면 어울리는 직업과, 그 직업의 성격을 닮은 포켓몬을 추천해드려요!")

mbti = st.selectbox("당신의 MBTI를 선택하세요", list(MBTI_DATA.keys()))

if st.button("추천받기 🔍"):
    data = MBTI_DATA[mbti]

    st.subheader(f"🧭 {mbti} 유형 추천 직업")
    st.markdown(f"**{data['career']}**")
    st.write(data["reason"])

    st.subheader("🐾 어울리는 포켓몬")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(pokemon_image_url(data["pokedex_id"]), width=180)
    with col2:
        st.markdown(f"**{data['pokemon']}**")
        st.write(data["pokemon_reason"])

st.divider()
st.caption("포켓몬 이미지 출처: PokeAPI (raw.githubusercontent.com/PokeAPI/sprites)")
