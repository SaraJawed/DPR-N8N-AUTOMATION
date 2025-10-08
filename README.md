# 🚀 Daily Progress Report (DPR) Automation using n8n

![n8n](https://img.shields.io/badge/Automation-n8n-orange)
![Docker](https://img.shields.io/badge/Containerized-Docker-blue)
![Email](https://img.shields.io/badge/Email-Gmail%20SMTP-green)

## 📋 Overview
This project automates the **Daily Progress Report (DPR)** workflow using **n8n**, an open-source automation tool.  
It collects daily progress data via a webhook, formats it, and sends a clean HTML email automatically to your inbox.

---

## 🏗️ Project Setup

### 1️⃣ Clone Repository
bash
git clone https://github.com/<your-username>/dpr-automation.git
cd dpr-automation
2️⃣ Run n8n with Docker

Make sure Docker is installed and running on your machine.

docker compose up -d


Once started, open n8n at:
👉 http://localhost:5678
⚙️ Workflow Description
🔹 Webhook Node

Endpoint example:

POST http://localhost:5678/webhook-test/dpr_trigger

---
