# AI Meeting Notes Summarizer

A Generative AI-powered application that automatically summarizes meeting transcripts and extracts actionable insights including key decisions, action items, risks, and discussion points.

---

# Project Overview

This application helps businesses automate meeting documentation workflows using Natural Language Processing (NLP) and AI summarization techniques.

Users can upload meeting transcripts and instantly generate:
- Executive summaries
- Action items
- Key discussion points
- Risks & blockers
- Final decisions

The project demonstrates practical implementation of AI-driven business process automation and productivity enhancement.

---

# Features

- Upload meeting transcript files
- AI-generated meeting summaries
- Action item extraction
- Risk and blocker identification
- Executive-level concise summaries
- Download generated summaries
- Interactive web interface using Streamlit

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Web Application UI |
| HuggingFace Transformers | NLP Summarization |
| BART Large CNN | AI Summarization Model |
| Pandas | Data Handling |

---

# Project Architecture

```text
User Uploads Transcript
        ↓
Transcript Processing
        ↓
AI Summarization Model
        ↓
Generate:
- Summary
- Action Items
- Decisions
- Risks
        ↓
Display Output in Streamlit Dashboard
```

---

# Folder Structure

```text
ai-meeting-summarizer/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_transcript.txt
├── .gitignore
└── utils/
    └── summarizer.py
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/VanShi-codes/ai-meeting-summarizer.git
```

## Navigate to Project

```bash
cd ai-meeting-summarizer
```

## Create Virtual Environment

```bash
python3.11 -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python -m streamlit run app.py
```

---

# Sample Input

```text
John: Sales declined by 12% this quarter.

Sarah: We should automate customer onboarding.

Mike: Engineering can build the automation workflow within 3 weeks.

John: Let's target deployment before next month.
```

---

# Sample Output

## Executive Summary
The meeting focused on improving customer onboarding efficiency through automation initiatives.

## Action Items
- Mike to prepare technical implementation plan
- Sarah to coordinate with CRM team
- John to approve project budget

## Risks
- API dependency from CRM team
- Tight implementation timeline

---

# Business Impact

- Reduces manual documentation effort
- Improves operational productivity
- Enhances meeting tracking efficiency
- Enables faster decision-making
- Automates business communication workflows

---

# Future Improvements

- Speech-to-text integration
- Zoom/Google Meet integration
- Multi-language summarization
- Email summary export
- AI-powered sentiment analysis
- User authentication

---

# Learning Outcomes

This project demonstrates:
- NLP implementation
- Generative AI workflows
- AI integration into business operations
- Business process automation
- End-to-end application deployment
- Git & GitHub project management

---

# Author

## Vanshita Tiwari

- GitHub: https://github.com/VanShi-codes

---

# License

This project is created for educational and portfolio purposes.
