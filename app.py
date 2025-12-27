import streamlit as st
import pandas as pd
import numpy as np
from anthropic import Anthropic
import io
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Time Series Analysis BIJU",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📊 Time Series Analysis BIJU")
st.markdown("*Analyze time series data and get AI-powered insights*")

# Sidebar for API key
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input(
    "Enter your Anthropic API Key",
    type="password",
    help="Get your API key from https://console.anthropic.com"
)

if not api_key:
    st.warning("⚠️ Please enter your Anthropic API Key in the sidebar to proceed")
    st.stop()

# Initialize Anthropic client with API key from sidebar
if api_key:
    client = Anthropic(api_key=api_key)
else:
    client = None

# Main content
st.header("Upload & Analyze Time Series Data")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Excel File (.xlsx, .xls, .csv)",
    type=["xlsx", "xls", "csv"],
    help="Upload your time series data in Excel or CSV format"
)

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    
    # Read the file
    try:
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Display data preview
        st.subheader("📋 Data Preview")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        with col2:
            st.write(f"**Data Type:** {uploaded_file.name}")
        
        st.dataframe(df.head(10), use_container_width=True)
        
        # Store data in session state
        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.stop()

# Analysis section
if 'df' in st.session_state:
    df = st.session_state.df
    
    st.subheader("🔍 Analysis Options")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        analyze_button = st.button("🚀 Analyze with Claude AI", type="primary", use_container_width=True)
    
    with col2:
        show_stats = st.checkbox("Show Basic Statistics", value=True)
    
    # Basic statistics
    if show_stats:
        st.subheader("📈 Basic Statistics")
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if numeric_cols:
            stats_cols = st.columns(len(numeric_cols[:4]))  # Show first 4 numeric columns
            
            for idx, col in enumerate(numeric_cols[:4]):
                with stats_cols[idx]:
                    st.metric(
                        label=col,
                        value=f"{df[col].mean():.2f}",
                        delta=f"σ: {df[col].std():.2f}",
                        help=f"Mean: {df[col].mean():.2f}\nStd Dev: {df[col].std():.2f}"
                    )
        else:
            st.info("No numeric columns found in the dataset")
    
    # Claude Analysis
    if analyze_button:
        if not client:
            st.error("❌ API key not configured. Please enter your API key in the sidebar.")
        else:
            with st.spinner("🤖 Claude is analyzing your data..."):
                try:
                    # Prepare data summary for Claude
                    data_summary = f"""
File Name: {st.session_state.file_name}
Shape: {df.shape[0]} rows × {df.shape[1]} columns
Columns: {', '.join(df.columns.tolist())}

Statistical Summary:
{df.describe().to_string()}

First few rows:
{df.head(10).to_string()}
"""
                    
                    # Send to Claude
                    message = client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=2000,
                        messages=[
                            {
                                "role": "user",
                                "content": f"""
You are an expert data analyst specializing in time series analysis. 
Analyze the following dataset and provide:

1. **Key Performance Indicators (KPIs)**: Identify the most important metrics
2. **Trends & Patterns**: What patterns do you observe?
3. **Anomalies**: Are there any unusual data points or anomalies?
4. **Recommendations**: What actionable insights can you provide?
5. **Risk Assessment**: Any potential risks or concerns?

Dataset:
{data_summary}

Please provide a comprehensive analysis with specific recommendations for improvement.
"""
                            }
                        ]
                    )
                    
                    analysis_result = message.content[0].text
                    
                    # Display analysis results
                    st.subheader("🎯 AI Analysis Results")
                    st.markdown(analysis_result)
                    
                    # Save analysis to session state
                    st.session_state.analysis = analysis_result
                    
                    # Provide download options
                    st.subheader("📥 Download Results")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Download analysis as text
                        analysis_text = f"Time Series Analysis Report\n{'='*50}\n\nFile: {st.session_state.file_name}\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{analysis_result}"
                        st.download_button(
                            label="📄 Download Analysis (TXT)",
                            data=analysis_text,
                            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    
                    with col2:
                        # Download data with analysis
                        output = io.BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            df.to_excel(writer, sheet_name='Data', index=False)
                            analysis_df = pd.DataFrame({'Analysis': [analysis_result]})
                            analysis_df.to_excel(writer, sheet_name='Analysis', index=False)
                        
                        output.seek(0)
                        st.download_button(
                            label="📊 Download Data + Analysis (XLSX)",
                            data=output.getvalue(),
                            file_name=f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Time Series Analysis Tool • Powered by Claude AI</p>
    <small>© 2025 • Secure and Private Analysis</small>
</div>
""", unsafe_allow_html=True)
