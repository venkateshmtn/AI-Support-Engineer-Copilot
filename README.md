# 🤖 AI Support Engineer Copilot

An intelligent, multi-agent customer support automation system built with **LangGraph**, **FAISS vector search**, and **Claude (Anthropic)**. The system processes support tickets end-to-end — from triage and root cause analysis to resolution recommendations and escalation decisions — and surfaces everything through an interactive **Streamlit** dashboard.

---

## ✨ Key Features

- **Multi-Agent Pipeline** — Nine specialized AI agents work in sequence, each responsible for a distinct stage of ticket resolution
- **Semantic Retrieval (RAG)** — FAISS vector store with Sentence Transformers retrieves the most relevant support documentation for each ticket
- **Automated Triage** — Classifies tickets by category, priority, and customer sentiment in real time
- **Root Cause Analysis** — Matches retrieved knowledge to known failure patterns (fraud blocks, expired cards, bank rejections, etc.)
- **Smart Escalation Logic** — Factors in customer plan tier, open ticket count, confidence score, and issue type
- **Customer Context Enrichment** — Pulls live customer profile data to personalize every response
- **Streamlit Dashboard** — Clean, recruiter-friendly UI with metrics, progress bars, and a generated case summary report

---

## 🏗️ Architecture

The pipeline is orchestrated by **LangGraph** as a directed state graph. Each node is a focused agent that reads from and writes to a shared `SupportState` object.

```
Ticket Input
     │
     ▼
┌─────────────┐
│   Triage    │  → Category, Priority, Sentiment
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Customer Context │  → Name, Plan, Open Tickets
└──────┬───────────┘
       │
       ▼
┌───────────────┐
│   Retrieval   │  → FAISS semantic search over support docs
└──────┬────────┘
       │
       ▼
┌─────────────┐
│  Root Cause │  → Maps retrieved docs to known failure patterns
└──────┬──────┘
       │
       ▼
┌────────────┐
│ Resolution │  → Step-by-step fix recommendations
└──────┬─────┘
       │
       ▼
┌────────────┐
│ Escalation │  → Confidence score + escalation decision
└──────┬─────┘
       │
       ▼
┌────────────────┐
│ Final Response │  → Full case summary report
└────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangGraph (StateGraph) |
| Vector Store | FAISS + `faiss-cpu` |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Frontend | Streamlit |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
├── app/
│   ├── agents/
│   │   ├── triage_agent.py           # Category, priority, sentiment detection
│   │   ├── customer_context_agent.py # Customer profile enrichment
│   │   ├── retrieval_agent.py        # FAISS semantic document search
│   │   ├── root_cause_agent.py       # Pattern-based root cause mapping
│   │   ├── resolution_agent.py       # Resolution step generation
│   │   ├── escalation_agent.py       # Confidence scoring & escalation logic
│   │   └── final_response_agent.py   # Case summary report generation
│   ├── graph/
│   │   └── support_graph.py          # LangGraph pipeline definition
│   ├── models/
│   │   └── state.py                  # Shared TypedDict state schema
│   ├── tools/
│   │   ├── customer_tool.py          # Customer profile lookup
│   │   └── knowledge_tool.py         # Support docs retrieval
│   └── vectorstore/
│       └── faiss_store.py            # FAISS index load & semantic search
├── data/
│   ├── customers/                    # Customer profile data
│   └── support_docs/                 # Support documentation & FAISS index
├── build_index.py                    # One-time script to build FAISS index
└── streamlit_app.py                  # Streamlit frontend
```

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/ai-support-copilot.git
cd ai-support-copilot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Build the FAISS vector index**
```bash
python build_index.py
```

**4. Launch the app**
```bash
streamlit run streamlit_app.py
```

---

## 💡 How It Works

1. A support agent pastes a customer ticket into the dashboard
2. The **Triage Agent** classifies the issue and detects sentiment
3. The **Customer Context Agent** fetches the customer's profile (plan, open tickets, etc.)
4. The **Retrieval Agent** runs a semantic similarity search against indexed support docs using FAISS
5. The **Root Cause Agent** maps the top result to a known failure pattern
6. The **Resolution Agent** generates a prioritized list of fix steps
7. The **Escalation Agent** computes a confidence score and decides whether to escalate, considering customer tier and issue severity
8. The **Final Response Agent** compiles everything into a structured case summary

---

## 📊 Example Output

```
SUPPORT CASE SUMMARY

Customer:     Jane Smith
Plan:         Enterprise
Category:     Payment
Priority:     High
Sentiment:    Frustrated
Root Cause:   Fraud Detection Block

Recommended Actions:
• Verify customer identity
• Confirm billing information
• Retry payment
• Escalate if issue persists

Confidence Score:  70%
Escalation:        YES — Customer has multiple open tickets.
```

---

## 🧠 Design Decisions

**Why LangGraph?** LangGraph's `StateGraph` makes the agent pipeline explicit, testable, and easy to extend. Adding a new agent is as simple as adding a node and an edge.

**Why FAISS over a hosted vector DB?** FAISS keeps the project fully local and dependency-light, making it easy to demo without cloud credentials.

**Why TypedDict for state?** A typed shared state schema (`SupportState`) catches bugs early and makes the data flow between agents self-documenting.

---

## 🔮 Potential Extensions

- Swap keyword-based triage for an LLM call to handle free-form tickets
- Add a human-in-the-loop approval node for escalated cases
- Persist case history to a database for trend analysis
- Integrate with ticketing systems (Zendesk, Jira Service Management) via webhooks

---

## 👤 Author

Built as a portfolio project to demonstrate multi-agent system design, RAG pipelines, and production-ready Python architecture.
