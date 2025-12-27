# Time Series Analysis BIJU 📊

A powerful Streamlit web application for analyzing time series data using Claude AI. Upload Excel or CSV files to get comprehensive analysis, KPIs, and actionable recommendations.

## Features ✨

- 📤 **File Upload**: Support for Excel (.xlsx, .xls) and CSV files
- 🤖 **Claude AI Analysis**: Leverages Claude AI for deep insights
- 📊 **KPI Extraction**: Automatically identifies key performance indicators
- 📈 **Trend Analysis**: Detects patterns and trends in your data
- ⚠️ **Anomaly Detection**: Identifies unusual data points
- 💡 **Recommendations**: Actionable insights for improvement
- 📥 **Download Results**: Export analysis as text or Excel

## Installation 🛠️

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/bijubaladevan/AI-PROJECT-TIME-SERIES-ANALYSIS.git
cd AI-PROJECT-TIME-SERIES-ANALYSIS
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

### Run Locally

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository
5. Deploy!

## Getting Your API Key 🔑

1. Visit [Anthropic Console](https://console.anthropic.com)
2. Sign up or log in
3. Generate a new API key
4. Copy and paste it in the sidebar of the application

## How It Works 🧠

1. **Upload Data**: Select and upload your Excel or CSV file
2. **Data Preview**: View your data in the application
3. **Click Analyze**: Start Claude AI analysis
4. **Get Insights**: Receive:
   - Key Performance Indicators
   - Trends & Patterns
   - Anomaly Detection
   - Risk Assessment
   - Recommendations
5. **Download**: Export results as text or Excel

## File Structure 📁

```
AI-PROJECT-TIME-SERIES-ANALYSIS/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## Technologies Used 🛠️

- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Anthropic Claude**: AI Analysis
- **OpenPyXL**: Excel file handling

## Environment Variables 🔐

The application requires:
- `ANTHROPIC_API_KEY`: Your Anthropic API key (provided via UI)

## Troubleshooting 🔧

### Issue: "ModuleNotFoundError"
**Solution**: Make sure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### Issue: "API Key not found"
**Solution**: Enter your Anthropic API key in the sidebar before uploading a file

### Issue: File upload fails
**Solution**: Ensure your Excel/CSV file:
- Has a valid format
- Is not corrupted
- Has proper column headers

## Contributing 🤝

Feel free to fork this repository and submit pull requests for any improvements.

## License 📜

This project is open source and available under the MIT License.

## Author 👤

**Biju Baladevan**
- GitHub: [@bijubaladevan](https://github.com/bijubaladevan)
- Email: bijubaladevan@gmail.com

## Support 💬

For issues and questions, please open an issue on GitHub.

## Changelog 📝

### Version 1.0.0 (2025-12-27)
- Initial release
- File upload functionality
- Claude AI integration
- KPI extraction
- Analysis export

---

**Last Updated**: December 27, 2025
