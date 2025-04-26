# RAG_ma_tax

**A lightweight, open-source retrieval system for exploring the Internal Revenue Code — built for clarity, accessibility, and trust.**

---

## 📚 What is RAG_ma_tax?

RAG_ma_tax is a **Retrieval-Augmented Generation (RAG)** system designed to help individuals — starting with my sister — navigate federal tax law more clearly and calmly.

Rather than pretending to replace human judgment, RAG_ma_tax helps users **find** relevant tax code sections quickly, **summarize** dense language without distortion, and **guide** them back to the **real source documents** — where the final understanding must always come from.

Built around a **retro terminal interface**, **private server retrieval**, and a **growing library of clean markdown files** representing Title 26 of the U.S. Code (the Internal Revenue Code).

---

## 🎯 Project Goals

- 📖 **Help users quickly find applicable tax law sections**
- 🔍 **Highlight important information (especially numbers) first**
- 🧠 **Provide optional, deeper summaries for those who want more clarity**
- 🛡️ **Always cite exact sources and invite users to verify**
- ⚙️ **Allow private, local operation (no cloud dependencies)**
- 🌱 **Expand gradually — growing from critical sections outward**

---

## 🚀 How It Works

1. **Lightweight Retro Terminal UI** runs in your browser (Wasm + HTML/JS/CSS).
2. **FastAPI backend** hosted privately processes search queries and retrieval.
3. **Knowledge Base** of structured markdown files powers fast, focused retrieval.
4. **Model Inference** (Mistral 7B or others) refines answers if enabled.
5. **User control and transparency** at every step — *no black box answers*.

---

## 📂 Repository Structure

