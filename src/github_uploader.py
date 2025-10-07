import os
import json
import random
import logging
from datetime import datetime
from dotenv import load_dotenv
import requests
import base64

# -------------------------------
# 1️⃣ Load env
# -------------------------------
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
REPO = os.getenv("GITHUB_REPO")

if not all([GITHUB_TOKEN, USERNAME, REPO]):
    raise ValueError("⚠️ Missing GITHUB_TOKEN / USERNAME / REPO in .env")

# -------------------------------
# 2️⃣ Setup logging
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# -------------------------------
# 3️⃣ Dummy data pools
# -------------------------------
TASKS = [
    "Setup daily automation",
    "Integrate Slack notification",
    "Optimize webhook response",
    "Add DPR storage in GitHub",
    "Improve error handling and retry system",
]

ISSUES = [
    "API rate limit hit",
    "Network latency detected",
    "Minor formatting issue",
]

NEXT_PLANS = [
    "Integrate DPR dashboard in GitHub Pages",
    "Schedule daily runs via cron",
    "Send DPR to Slack channel",
]

# -------------------------------
# 4️⃣ Generate DPR
# -------------------------------
def build_dpr():
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tasks_completed": random.sample(TASKS, k=2),
        "issues_faced": random.sample(ISSUES, k=1),
        "next_plan": random.sample(NEXT_PLANS, k=2),
        "sent_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# -------------------------------
# 5️⃣ Upload to GitHub
# -------------------------------
def upload_to_github(dpr_data):
    filename = f"dpr_{dpr_data['date']}.json"
    path = f"reports/{filename}"

    content = json.dumps(dpr_data, indent=2)
    content_b64 = base64.b64encode(content.encode()).decode()

    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    data = {
        "message": f"Add DPR for {dpr_data['date']}",
        "content": content_b64
    }

    r = requests.put(url, headers=headers, json=data)
    if r.status_code in [200, 201]:
        logger.info(f"✅ DPR uploaded successfully as {path}")
    else:
        logger.error(f"❌ Upload failed: {r.status_code} - {r.text}")

# -------------------------------
# 6️⃣ Main
# -------------------------------
if __name__ == "__main__":
    logger.info("📤 Generating DPR and uploading to GitHub...")
    dpr = build_dpr()
    logger.info(json.dumps(dpr, indent=2))
    upload_to_github(dpr)
    logger.info("🏁 Process Finished.")
