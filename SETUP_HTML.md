# Technical Documentation Generator - HTML Version

## 📋 Quick Setup

### 1. Install Flask (One-time)
```bash
pip install flask
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the App
Open your browser and go to:
```
http://localhost:5000
```

That's it! 🎉

---

## ✨ Features
- ✅ Clean, modern UI with gradient background
- ✅ Responsive design (works on mobile, tablet, desktop)
- ✅ Template examples for quick start
- ✅ Adjustable creativity slider
- ✅ Copy to clipboard functionality
- ✅ Download as Markdown file
- ✅ Loading indicators and error handling

---

## 🛠️ Troubleshooting

### Port Already in Use?
```bash
# Change port in app.py line 31: app.run(debug=True, port=5001)
```

### Module Not Found?
```bash
pip install flask langchain langchain-openai python-dotenv
```

### API Key Error?
Make sure `.env` file exists in the same directory:
```
OPENAI_API_KEY=your_api_key_here
```

---

## 📁 Project Structure
```
Project/
├── app.py                 (Flask backend)
├── templates/
│   └── index.html        (Frontend UI)
└── .env                  (API key - keep it secret)
```

## 🔄 How It Works
1. HTML form sends feature description to Flask backend
2. Flask processes the request using LangChain + OpenAI
3. Response returns as JSON
4. JavaScript displays the documentation
5. User can copy or download the result

---

## 🎯 Customization

### Change App Title
Edit `index.html` line 6: `<title>Your Title</title>`

### Change Colors
Edit `index.html` CSS section (lines 12-13):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Model
Edit `app.py` line 33:
```python
llm = ChatOpenAI(model="gpt-4-turbo", temperature=temperature)
```
