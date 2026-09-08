import os
import streamlit as st
from google import genai

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="StudySense AI",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# GEMINI CONNECTION
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None


def ask_ai(prompt):
    """Send a prompt to Gemini and return the answer."""

    if not client:
        return "⚠️ Gemini API key is not connected."

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🧠 StudySense AI")
st.sidebar.write("Your Personal AI Study Mentor")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "📄 Notes Analyzer",
        "🧠 Quiz Generator",
        "📅 Study Planner",
        "🤖 AI Mentor"
    ]
)

st.sidebar.divider()
st.sidebar.success("🟢 AI System Ready")


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.title("🧠 StudySense AI")
    st.subheader("Your Personal AI-Powered Study Mentor")

    st.write(
        "StudySense AI uses artificial intelligence to help "
        "students understand notes, practice questions, "
        "plan their studies and improve learning."
    )

    st.divider()

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Subjects", "5")

    with col2:
        st.metric("🧠 Quiz Score", "82%")

    with col3:
        st.metric("🎯 Weak Topics", "3")

    with col4:
        st.metric("🔥 Study Streak", "7 Days")

    st.divider()

    st.header("🚀 AI Learning Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "📄 **AI Notes Analyzer**\n\n"
            "Paste your notes and let AI identify "
            "important concepts and create a simple summary."
        )

        st.success(
            "🧠 **AI Quiz Generator**\n\n"
            "Generate practice questions from any subject "
            "or topic."
        )

    with col2:
        st.warning(
            "📅 **Smart Study Planner**\n\n"
            "Create a personalized study schedule based "
            "on your available time."
        )

        st.error(
            "🤖 **AI Study Mentor**\n\n"
            "Ask questions and get explanations from your "
            "personal AI mentor."
        )

    st.divider()

    st.caption(
        "StudySense AI • Learn smarter, not harder 🚀"
    )


# =========================================================
# NOTES ANALYZER
# =========================================================

elif page == "📄 Notes Analyzer":

    st.title("📄 AI Notes Analyzer")

    st.write(
        "Paste your study notes below and AI will analyze them."
    )

    notes = st.text_area(
        "📝 Enter your notes",
        height=300,
        placeholder="Example:\nPhotosynthesis is the process by which green plants..."
    )

    if st.button("✨ Analyze Notes", use_container_width=True):

        if not notes.strip():
            st.warning("Please enter some notes first.")

        else:

            with st.spinner("🧠 AI is analyzing your notes..."):

                prompt = f"""
You are an expert study mentor.

Analyze the following student notes.

Give the answer in these sections:

1. 📌 Simple Summary
2. ⭐ Important Concepts
3. 🎯 Exam Important Points
4. ❓ Questions the student should practice
5. 💡 Easy Memory Trick

Use simple student-friendly language.

STUDENT NOTES:
{notes}
"""

                result = ask_ai(prompt)

            st.success("Analysis completed!")

            st.markdown(result)


# =========================================================
# QUIZ GENERATOR
# =========================================================

elif page == "🧠 Quiz Generator":

    st.title("🧠 AI Quiz Generator")

    st.write(
        "Generate practice questions using artificial intelligence."
    )

    topic = st.text_input(
        "📚 Enter a topic",
        placeholder="Example: Operating Systems"
    )

    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    number = st.slider(
        "Number of questions",
        3,
        10,
        5
    )

    if st.button("🚀 Generate Quiz", use_container_width=True):

        if not topic.strip():

            st.warning("Please enter a topic.")

        else:

            with st.spinner("🧠 Generating your quiz..."):

                prompt = f"""
Create a {difficulty} level quiz for a college student.

Topic: {topic}

Create {number} multiple-choice questions.

For every question provide:

Question
A)
B)
C)
D)

Then provide the correct answer and a short explanation.

Make the questions educational and useful for exams.
"""

                result = ask_ai(prompt)

            st.success("Quiz generated!")

            st.markdown(result)


# =========================================================
# STUDY PLANNER
# =========================================================

elif page == "📅 Study Planner":

    st.title("📅 Smart Study Planner")

    st.write(
        "Tell AI about your study goals and available time."
    )

    subjects = st.text_input(
        "📚 Subjects",
        placeholder="Example: DBMS, Java, Operating Systems, AI"
    )

    hours = st.slider(
        "⏰ Available study hours per day",
        1,
        12,
        3
    )

    days = st.slider(
        "📅 Number of days",
        1,
        30,
        7
    )

    goal = st.text_input(
        "🎯 Your goal",
        placeholder="Example: Prepare for semester exams"
    )

    if st.button("✨ Create Study Plan", use_container_width=True):

        if not subjects.strip():

            st.warning("Please enter your subjects.")

        else:

            with st.spinner("📅 Creating your personalized plan..."):

                prompt = f"""
You are an intelligent academic study planner.

Create a practical study plan for a student.

Subjects:
{subjects}

Available study time:
{hours} hours per day

Number of days:
{days}

Goal:
{goal}

Create:

1. 📅 Daily schedule
2. 📚 Subject allocation
3. 🔄 Revision strategy
4. 🧠 Practice strategy
5. 💡 Tips to stay consistent

Keep the schedule realistic and easy to follow.
"""

                result = ask_ai(prompt)

            st.success("Your study plan is ready!")

            st.markdown(result)


# =========================================================
# AI MENTOR
# =========================================================

elif page == "🤖 AI Mentor":

    st.title("🤖 AI Study Mentor")

    st.write(
        "Ask StudySense anything related to your studies."
    )

    question = st.text_area(
        "💬 Ask your question",
        height=180,
        placeholder="Example: Explain deadlock in Operating Systems in simple words."
    )

    if st.button("💡 Ask StudySense", use_container_width=True):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner("🤖 StudySense is thinking..."):

                prompt = f"""
You are StudySense AI, a friendly and intelligent
college study mentor.

Answer the student's question clearly.

Student question:
{question}

Rules:
- Use simple language.
- Explain difficult concepts with examples.
- Use bullet points where useful.
- Focus on helping the student understand the concept.
"""

                result = ask_ai(prompt)

            st.success("Here's your answer:")

            st.markdown(result)