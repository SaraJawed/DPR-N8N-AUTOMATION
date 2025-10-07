import os
import json
import time
import random
import logging
import requests
from datetime import datetime
from dotenv import load_dotenv

# -------------------------------
# 1️⃣ Load environment variables
# -------------------------------
load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# -------------------------------
# 2️⃣ Setup logging
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("dpr_sender.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# -------------------------------
# 3️⃣ Predefined task ideas
# -------------------------------
TASKS = [
    "Setup daily automation",
    "Test Google Sheets integration",
    "Integrate Slack notification",
    "Optimize webhook response time",
    "Add database persistence for DPR",
    "Improve error handling and logging",
    "Deploy n8n and Python app via Docker",
    "Refactor automation scripts"
]

ISSUES = [
    "Slow webhook response",
    "Docker container restart delay",
    "n8n timeout issue",
    "Environment variable not loading",
    "Invalid payload format error",
    "Webhook test mode expired"
]

NEXT_PLANS = [
    "Add Slack notifications",
    "Store DPR in PostgreSQL database",
    "Enable automatic retry system",
    "Add daily summary email",
    "Integrate with Google Sheets API",
    "Schedule DPR at 6 PM daily"
]

# -------------------------------
# 4️⃣ Generate random DPR
# -------------------------------
def build_dynamic_dpr():
    """Generates slightly different DPR each time"""
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tasks_completed": random.sample(TASKS, k=random.randint(2, 3)),
        "issues_faced": random.sample(ISSUES, k=random.randint(1, 2)),
        "next_plan": random.sample(NEXT_PLANS, k=random.randint(2, 3)),
        "sent_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# -------------------------------
# 5️⃣ Send DPR
# -------------------------------
def send_dpr_data(payload, retries=3, delay=3):
    """Send DPR data to webhook with retries"""
    if not WEBHOOK_URL:
        logger.error("Missing WEBHOOK_URL in .env file.")
        return False

    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Attempt {attempt}/{retries} sending DPR...")
            response = requests.post(WEBHOOK_URL, json=payload, timeout=10)

            if response.status_code == 200:
                logger.info("✅ DPR sent successfully!")
                logger.info(f"Response: {response.text}")
                return True
            else:
                logger.warning(
                    f"⚠️ HTTP {response.status_code}: {response.text}"
                )

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Connection error: {e}")

        time.sleep(delay)

    logger.error("🚨 All attempts failed. Check webhook or server logs.")
    return False

# -------------------------------
# 6️⃣ Main
# -------------------------------
def main():
    logger.info("📤 Starting Auto-DPR Send Process...")
    logger.info("─────────────────────────────────────────────")

    dpr_data = build_dynamic_dpr()

    logger.info("Generated DPR:")
    logger.info(json.dumps(dpr_data, indent=2))

    send_dpr_data(dpr_data)

    logger.info("─────────────────────────────────────────────")
    logger.info("🏁 Process Finished\n")

# -------------------------------
# 7️⃣ Run
# -------------------------------
if __name__ == "__main__":
    main()
