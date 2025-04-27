# RAGtax

**A lightweight, open-source retrieval system for exploring the Internal Revenue Code — built for clarity, accessibility, and trust.**

---

## 📚 What is RAGtax?

RAGtax is a **Retrieval-Augmented Generation (RAG)** system designed to help individuals — starting with my sister — navigate federal tax law more clearly and calmly.

Rather than pretending to replace human judgment, RAGtax helps users:

- **Find** relevant tax code sections quickly
- **Summarize** dense language without distortion
- **Guide** users back to the **real source documents** — where final understanding must always come from

Built around a **retro terminal interface**, **private server retrieval**, and a **growing library of clean Markdown files** representing Title 26 of the U.S. Code (the Internal Revenue Code).

---

## 🎯 Project Goals

- 📖 **Quick retrieval**: Help users find applicable sections fast
- 🔍 **Highlight important numbers and thresholds** first
- 🧠 **Optional deeper summaries**: Offer layered understanding without overwhelming
- 🛡️ **Cite exact sources**: Always link back to original tax code text
- ⚙️ **Private, local operation**: No external cloud dependencies required
- 🌱 **Gradual expansion**: Start with the most critical sections and build outward

---

## 🚀 How It Works

1. **Lightweight Retro Terminal UI**  
   - Runs directly in the browser using WebAssembly (Wasm) + HTML/CSS/JavaScript.
2. **Private FastAPI Backend**  
   - Processes search queries and handles Markdown retrieval.
3. **Knowledge Base**  
   - Structured, cleaned Markdown files representing sections of the Internal Revenue Code.
4. **Optional Model Inference**  
   - Integrate models like **Mistral 7B** to generate guidance — *but always defer to the real text*.
5. **Transparency by Design**  
   - Every AI output links to its underlying source; users are encouraged to verify, not blindly trust.

---

## ⚙️ System Requirements

- **Basic Use (Markdown Search and Retrieval):**
  - CPU-only
  - Browser and local server (FastAPI) are sufficient

- **Optional Advanced Features (Model Inference / Summarization):**
  - Recommended GPU for efficient model inference (e.g., Mistral 7B or similar)
  - The system can offload AI summarization tasks to a local GPU if available

- **Private-first by design:**
  - No external cloud servers required
  - Full operation stays on the user's machine

---

## 📂 Repository Structure

