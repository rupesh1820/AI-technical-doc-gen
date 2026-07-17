# 📚 AI Technical Documentation Generator

A modern web application that converts feature descriptions into professional technical documentation using OpenAI's GPT-4 and LangChain.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🚀 **One-Click Generation** - Convert feature ideas to documentation instantly
- 📝 **Template Examples** - Pre-built templates for quick start
- 🎨 **Modern UI** - Clean, responsive design that works on all devices
- 📋 **Copy & Download** - Copy to clipboard or download as Markdown
- 🎯 **Customizable** - Adjust creativity level with slider
- 🔐 **Secure** - API keys stored safely in `.env` file

## 📖 Documentation Includes

- Overview
- Objectives
- Functional Requirements
- System Architecture
- Workflow
- API Design
- Database Design
- Security
- Testing
- Deployment
- Future Enhancements

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: OpenAI GPT-4 + LangChain
- **Styling**: Responsive CSS with gradients

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/rupesh1820/Ai-technical-dec-gen.git
cd Ai-technical-dec-gen
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
```
http://localhost:5000
```

## 📁 Project Structure
```
.
├── app.py                    # Flask backend
├── templates/
│   └── index.html           # Frontend UI
├── requirements.txt         # Python dependencies
├── .env                     # API keys (not in git)
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── SETUP_HTML.md           # Detailed setup guide
```

## 🎯 How to Use

1. **Enter Feature Description**
   - Choose from templates or enter custom description
   - Be detailed for better results

2. **Adjust Settings**
   - Use creativity slider (0 = precise, 1.0 = creative)

3. **Generate**
   - Click "Generate" button
   - Wait for documentation to be created

4. **Export**
   - Copy to clipboard or
   - Download as Markdown file

## ⚙️ Configuration

### Change Port
Edit `app.py`:
```python
app.run(debug=True, port=8000)  # Change 5000 to your desired port
```

### Change AI Model
Edit `app.py`:
```python
llm = ChatOpenAI(model="gpt-4-turbo", temperature=temperature)
```

### Customize Prompt
Edit the prompt template in `app.py` to generate different documentation formats.

## 🔧 Troubleshooting

### Port Already in Use
```bash
python app.py --port 8000
```

### API Key Not Found
- Ensure `.env` file exists in root directory
- Check that `OPENAI_API_KEY` is set correctly
- Verify API key is valid at OpenAI dashboard

### Module Not Found
```bash
pip install --upgrade -r requirements.txt
```

### CORS Issues
If accessing from different origin, add CORS:
```bash
pip install flask-cors
```

Then in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Contact

GitHub: [@rupesh1820](https://github.com/rupesh1820)

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- LangChain for LLM framework
- Flask for web framework

---

Made with ❤️ by Rupesh
