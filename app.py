import streamlit as st

st.title("🎬 Travel Coach - Movie Price Checker")

# Step 1: Input from user
location = st.selectbox("📍 Select Your City", ["Mumbai", "Delhi", "Ahmedabad"])
movie = st.selectbox("🎥 Choose Movie", ["Furiosa", "IF", "Bad Boys", "Inside Out 2"])
date = st.date_input("📅 Select Date")
compare = st.button("Compare Ticket Prices")

# Step 2: Simulated response (mock)
if compare:
    st.subheader(f"🎟️ Price Comparison for {movie} on {date} in {location}")
    st.write("""
    - INOX (Phoenix Mall): ₹250
    - PVR Cinemas: ₹220
    - Cinepolis: ₹200 (Best Price)
    - Carnival: ₹230
    """)
    st.success("✅ Recommended: Cinepolis (₹200)")
