Project: Intelligent Telephone Answering System Based on AI and RAG (Retrieval-Augmented Generation)

📊 Project Objective
Create an intelligent telephone answering system for a company, capable of automatically answering incoming calls, handling FAQ-type requests, providing accurate information from an internal knowledge base, and optionally booking appointments.

This answering system will be based on a RAG architecture with a local LLM (initially Mistral 7B) and must be capable of handling multiple simultaneous calls.

🔄 Key Features
Reception of VoIP calls via a local server (Asterisk or FreeSWITCH)

Voice-to-text transcription (STT, e.g., Whisper.cpp)

Querying a local knowledge base (RAG)

Natural language response generation via a local LLM (Mistral 7B)

Real-time speech synthesis (TTS, e.g., Coqui TTS)

Playback of the voice response to the caller

Appointment scheduling via Outlook

Logging of calls and actions (email and/or Telegram)

Local debug mode (voice testing via microphone without VoIP)

📄 Knowledge Base (RAG)
Document types: PDF, Word, PowerPoint, emails, web pages

Indexing from scratch (no existing RAG)

Admin interface with a button to manually regenerate the index

Embeddings via ChromaDB or another local engine

Static pre-indexing (no automatic re-indexing)

🗓️ Appointment Scheduling
Outlook integration via Microsoft Graph API

Availability checking and appointment booking

Automatic notifications (email or Telegram)

Interaction logs with call summary and actions taken

📢 VoIP and Call Management
Up to 5 simultaneous calls

Asterisk or FreeSWITCH as SIP server

Local audio stream handling (WAV / ULAW playback)

Backend interaction (via AGI or local REST API)

🚀 Planned Tech Stack
Local LLM: Mistral 7B via Ollama (Q4/Q5 GGUF)

STT: Whisper.cpp (multilingual, quantized, real-time)

TTS: Coqui TTS or Mimic 3 (depending on latency/quality)

RAG: LangChain / llama-index + ChromaDB

Backend: FastAPI for orchestration

Admin frontend: Document upload, re-indexing button, logs

🛠️ Minimum Recommended Infrastructure
CPU: 8 cores

RAM: 32 GB

GPU: RTX 3060 or higher (for STT, LLM, TTS)

Storage: 500 GB SSD

OS: Ubuntu 22.04 LTS or similar

🔧 Debug Mode
Local testing without VoIP

Microphone + speakers to simulate a voice conversation

Ideal for development, prompt testing, response validation, and latency measurement