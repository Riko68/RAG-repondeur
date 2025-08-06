📦 Step 1 – Environment Setup
 Install Ubuntu 22.04 LTS server (physical or virtual)

 Install system dependencies: ffmpeg, sox, build-essential, python3, pip, etc.

 Install Docker + Docker Compose

 Set up a compatible GPU (e.g., NVIDIA RTX 3060+) with drivers + CUDA/cuDNN

🔉 Step 2 – VoIP Server (Asterisk)
 Install Asterisk or FreeSWITCH

 Configure SIP call reception (e.g., SIP account, ports, NAT, RTP, etc.)

 Create an AGI script or REST bridge to send audio to the AI system

 Test call reception and playback of WAV files during a call

🧠 Step 3 – Local LLM
 Install Ollama

 Download and load Mistral 7B (GGUF, quantized Q4 or Q5)

 Test local generation from command line

 Integrate into FastAPI backend (/generate endpoint)

📚 Step 4 – RAG Setup
 Build an indexing pipeline using LangChain or llama-index

 Enable ingestion of: PDF, DOCX, PPTX, EML, HTML

 Generate embeddings using a local model (e.g., BAAI/bge-small)

 Store embeddings in local ChromaDB

 Create a basic admin UI to upload files and manually trigger re-indexing

🎙️ Step 5 – STT (Speech-to-Text)
 Install whisper.cpp

 Test transcription of WAV files

 Integrate STT into FastAPI backend

 Add streaming or block-based processing for fast transcription

🗣️ Step 6 – TTS (Text-to-Speech)
 Install Coqui TTS with a fast local model

 Generate WAV files from text

 Test audio playback within Asterisk using Playback or stream method

🧪 Step 7 – Local Voice Debug Mode
 Implement pipeline: Microphone → Whisper → LLM → TTS → Speaker

 Add logging for each step (STT, RAG, response, audio)

 Build a basic console interface or small UI (e.g., PyQt or Streamlit)

📅 Step 8 – Appointment Scheduling & Outlook Integration
 Create Azure app and generate Microsoft Graph credentials

 Read availability from Outlook calendar

 Create appointments in target calendar

 Implement logic for appointment booking inside LLM responses

📥 Step 9 – Logging & Notifications
 Implement interaction logging (JSON files or SQLite)

 Add automatic email notification (SMTP)

 Add optional Telegram Bot notification

🌐 Step 10 – Backend & Orchestration
 Deploy FastAPI backend with endpoints:

/stt

/generate

/tts

/index

/debug

 Add orchestration logic to chain STT → RAG → LLM → TTS

 Add task queue system to handle multiple simultaneous calls

🧪 Step 11 – Testing and Validation
 Full test in local debug mode (voice input/output)

 Test with actual SIP call → audio → AI response

 Test Outlook appointment creation

 Test logging and notification features

 Simulate up to 5 simultaneous calls