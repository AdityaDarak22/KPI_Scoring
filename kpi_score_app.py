import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("Account Executive KPI Scorecard (2024/25)")
manager_name = st.text_input("Manager Name")
exec_name = st.text_input("Account Executive Name")

if manager_name and exec_name:
    st.markdown("### 1. Business Plan Delivery (10%)")
    bp1 = st.slider("Achieve budgeted sales revenue", 0, 10)
    bp2 = st.slider("Maintain Gross/Net Margins", 0, 10)
    bp3 = st.slider("Manage client costs", 0, 10)
    bp4 = st.slider("Increase business by 2%", 0, 10)
    bp_raw = bp1 * 0.3 + bp2 * 0.3 + bp3 * 0.3 + bp4 * 0.1
    bp_score = round(bp_raw * 0.10, 2)
    st.markdown(f"**Business Plan Score: {bp_score * 10:.1f}/10.0**")

    st.markdown("### 2. Operational (60%)")
    op1 = st.slider("Clear account plans", 0, 10)
    op2 = st.slider("Monthly review meetings", 0, 10)
    op3 = st.slider("Client governance & follow-up", 0, 10)
    op4 = st.slider("Demonstrate value-add", 0, 10)
    op5 = st.slider("Benchmark competition", 0, 10)
    op6 = st.slider("1 day in trade per month", 0, 10)
    op7 = st.slider("Pursue revenue leads", 0, 10)
    op8 = st.slider("Client relationships", 0, 10)
    op9 = st.slider("2 client meetings per week", 0, 10)
    op10 = st.slider("Best-in-class folder admin", 0, 10)
    op_raw = (
        op1 * 0.10 + op2 * 0.10 + op3 * 0.10 + op4 * 0.10 +
        op5 * 0.10 + op6 * 0.10 + op7 * 0.05 + op8 * 0.15 +
        op9 * 0.10 + op10 * 0.10
    )
    op_score = round(op_raw * 0.60, 2)
    st.markdown(f"**Operational Score: {op_score * 10:.1f}/60.0**")

    st.markdown("### 3. Social Media (30%)")
    sm1 = st.slider("Set SMSP Plan", 0, 10)
    sm2 = st.slider("Execute weekly posts", 0, 10)
    sm3 = st.slider("Followers gained", 0, 10)
    sm4 = st.slider("Engagement", 0, 10)
    sm5 = st.slider("Post views", 0, 10)
    sm6 = st.slider("Impressions", 0, 10)
    sm7 = st.slider("Share of voice", 0, 10)
    sm_raw = (
        sm1 * 0.2 + sm2 * 0.4 +
        (sm3 + sm4 + sm5 + sm6 + sm7) * 0.08
    )
    sm_score = round(sm_raw * 0.30, 2)
    st.markdown(f"**Social Media Score: {sm_score * 10:.1f}/30.0**")

    total_score = round(bp_score + op_score + sm_score, 2)
    percent_score = round(total_score * 10, 1)
    st.markdown("---")
    st.markdown(f"## 🏁 Final Performance Rating: **{percent_score}/100**")

    if percent_score >= 85:
        st.success("🏆 Excellent Performance (Gold)")
        rating = "Gold"
    elif percent_score >= 70:
        st.info("👍 Good Performance (Silver)")
        rating = "Silver"
    else:
        st.warning("⚠ Needs Improvement (Bronze)")
        rating = "Bronze"

    if st.button("💾 Save Result"):
        record = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Manager": manager_name,
            "Executive": exec_name,
            "Business Score": bp_score * 10,
            "Operational Score": op_score * 10,
            "Social Score": sm_score * 10,
            "Total Score": percent_score,
            "Rating": rating
        }
        df_new = pd.DataFrame([record])
        if os.path.exists("kpi_scores_log.csv"):
            df_old = pd.read_csv("kpi_scores_log.csv")
            df = pd.concat([df_old, df_new], ignore_index=True)
        else:
            df = df_new
        df.to_csv("kpi_scores_log.csv", index=False)
        st.success("✅ Score saved to 'kpi_scores_log.csv'")
        
        # 💡 Add this part to enable download
        csv_data = df_new.to_csv(index=False)
        st.download_button(
            label="📥 Download Your KPI Report",
            data=csv_data,
            file_name=f"KPI_Score_{exec_name.replace(' ', '_')}.csv",
            mime="text/csv"
        )
