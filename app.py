import streamlit as st
import requests
import json

st.set_page_config(page_title="SmishGuard AI", page_icon="🛡️", layout="centered")
st.title("🛡️ SmishGuard Security Shield")
st.markdown("### AI-Powered SMS Fraud & Threat Detection")
st.info("Paste a suspicious SMS message below to scan it for phishing, violence, or hate speech.")
sms_input = st.text_area("Enter SMS Text:", height=150, placeholder="Type message here...")
if st.button("🔍 Scan Message", type="primary"):
    if sms_input:
        with st.spinner("Consulting Azure AI Brain..."):
            try:
                api_url = "https://smishgaurd-app.azurewebsites.net/api/AnalyzeText" 
                payload = {"sms_text": sms_input}
                response = requests.post(api_url, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    is_suspicious = result.get("is_suspicious", False)
                    details = result.get("risk_details", [])

                    if is_suspicious:
                        st.error("🚨 THREAT DETECTED!")
                        st.write("### Risk Analysis:")
                        for item in details:
                            st.warning(f"⚠️ {item}")
                    else:
                        st.success("✅ MESSAGE IS SAFE")
                        st.balloons()
                        st.write("No harmful content detected by Azure AI.")
                
                else:
                    st.error(f"Server Error: {response.status_code}")
                    st.write(response.text)

            except Exception as e:
                st.error(f"Connection Failed: {e}")
    else:
        st.warning("Please enter some text first.")
st.markdown("---")
st.caption("Powered by Azure OpenAI & Python • Built for Imagine Cup 2026")