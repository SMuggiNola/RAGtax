# RAGtax

RAGtax is a system for converting official IRS tax code PDFs into structured Markdown files.

- 💾 Stores the tax code in a clean, AI-friendly, human-readable format
- ✍️ Smart formatting: Adds indentations for subsections (a), (1), (A)
- 🚀 Ready for search, retrieval, and lightweight RAG applications
- 📚 Built to help people (like tax preparers) navigate the law more easily

## How to Use
- Extract text from IRS PDFs using the `ragtax_pdf_to_markdown.py` script
- The script automatically spaces, indents, and structures the text
- Markdown files are saved in `/markdown_sections/`

## Future Plans
- Add simple search terminal
- Add batch PDF processing
- Add fine-grained metadata tagging for easier AI retrieval
