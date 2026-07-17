# Technical Documentation Generator - UI Setup

## 📋 Prerequisites
- Python 3.8+
- Virtual environment activated
- `.env` file with your OpenAI API key

## 🚀 Installation & Running

### 1. Install Streamlit
```bash
pip install streamlit
```

### 2. Verify Installation
```bash
streamlit --version
```

### 3. Run the UI Application
Navigate to the Project folder and run:
```bash
streamlit run ui_app.py
```

### 4. Access the Application
The app will open automatically in your browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually visit the URL above.

## ✨ Features

### Input Section (Left Panel)
- **Feature Description**: Enter your feature details
- **Example Templates**: Quick-start with pre-filled examples
- **Temperature Control**: Adjust AI creativity (0.0 = deterministic, 1.0 = creative)

### Output Section (Right Panel)
- **Real-time Generation**: Get instant documentation
- **Copy Button**: Quick copy to clipboard
- **Download**: Export as Markdown file

### Sidebar
- Instructions and guidance
- Settings controls
- Information about the generator

## 📝 .env File Setup

Make sure your `.env` file contains:
```
OPENAI_API_KEY=your_api_key_here
```

## 🔧 Troubleshooting

### Port Already in Use
```bash
streamlit run ui_app.py --server.port 8502
```

### Module Not Found
```bash
pip install -r requirements.txt
```

### API Key Issues
- Verify `.env` file is in the same directory
- Check API key validity at OpenAI dashboard
- Ensure `python-dotenv` is installed: `pip install python-dotenv`

## 📦 Required Dependencies
- streamlit
- langchain
- langchain-openai
- python-dotenv
- openai

All are included in your existing setup.
