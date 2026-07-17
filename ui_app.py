import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Technical Documentation Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTextArea textarea {
            font-size: 14px;
        }
        .output-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #0066cc;
        }
        .section-header {
            color: #0066cc;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .info-box {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            border-left: 4px solid #0066cc;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="section-header">📚 Technical Documentation Generator</div>
""", unsafe_allow_html=True)

# Sidebar with instructions
with st.sidebar:
    st.header("ℹ️ Instructions")
    st.markdown("""
    ### How to use:
    1. Enter a detailed feature description
    2. Click "Generate Documentation"
    3. Review the generated documentation
    4. Copy or download the result
    
    ### What it generates:
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
    """)
    
    # Settings
    st.markdown("---")
    st.subheader("⚙️ Settings")
    temperature = st.slider(
        "Temperature (Creativity)",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.1,
        help="Lower = More deterministic, Higher = More creative"
    )

# Main content area
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("📝 Feature Description")
    
    # Example features
    example = st.selectbox(
        "Select an example or enter custom:",
        [
            "Custom",
            "User Authentication System",
            "Real-time Chat Application",
            "E-commerce Shopping Cart",
            "File Upload Service"
        ]
    )
    
    if example == "Custom":
        feature_input = st.text_area(
            "Describe your feature:",
            height=300,
            placeholder="Enter a detailed description of the feature you want documented...",
            label_visibility="collapsed"
        )
    else:
        example_descriptions = {
            "User Authentication System": "A secure user authentication system with login, registration, password reset, and two-factor authentication support.",
            "Real-time Chat Application": "A real-time messaging platform that supports direct messages, group chats, file sharing, and typing indicators.",
            "E-commerce Shopping Cart": "A shopping cart system with product selection, inventory management, discount codes, and order processing.",
            "File Upload Service": "A file upload service with virus scanning, storage management, sharing capabilities, and version control."
        }
        feature_input = st.text_area(
            "Feature Description:",
            value=example_descriptions[example],
            height=300,
            label_visibility="collapsed"
        )

with col2:
    st.subheader("📄 Generated Documentation")
    
    # Generate button
    if st.button("🚀 Generate Documentation", use_container_width=True, type="primary"):
        if not feature_input.strip():
            st.error("❌ Please enter a feature description")
        else:
            with st.spinner("✨ Generating documentation..."):
                try:
                    # Initialize LLM
                    llm = ChatOpenAI(
                        model="gpt-4o-mini",
                        temperature=temperature
                    )
                    
                    # Create prompt
                    prompt = ChatPromptTemplate.from_template("""
You are an expert Technical Documentation Generator.

Convert the following feature description into professional Markdown documentation.

Include:
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

Feature:
{feature}
""")
                    
                    # Generate documentation
                    chain = prompt | llm
                    result = chain.invoke({"feature": feature_input})
                    
                    # Store in session state
                    st.session_state.documentation = result.content
                    st.success("✅ Documentation generated successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error generating documentation: {str(e)}")

# Display generated documentation
if "documentation" in st.session_state:
    st.markdown("---")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("### 📖 Result")
    with col2:
        if st.button("📋 Copy", use_container_width=True):
            st.toast("Documentation copied to clipboard!")
    
    # Display in markdown format
    with st.container():
        st.markdown("""<div class="output-box">""", unsafe_allow_html=True)
        st.markdown(st.session_state.documentation)
        st.markdown("""</div>""", unsafe_allow_html=True)
    
    # Download option
    st.download_button(
        label="⬇️ Download as Markdown",
        data=st.session_state.documentation,
        file_name="documentation.md",
        mime="text/markdown",
        use_container_width=True
    )
