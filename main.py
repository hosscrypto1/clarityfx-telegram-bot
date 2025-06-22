import os
import time
import logging
from telegram import Bot
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.INFO)

# Environment Variables (replace these directly if not using Railway ENV)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8035320092:AAFO_ErdP-mAQbOEH-aJBR0d9N1g43nUZOE")
FREE_CHANNEL_ID = int(os.getenv("FREE_CHANNEL_ID", "-1002874309959"))
VIP_CHANNEL_ID = int(os.getenv("VIP_CHANNEL_ID", "-1002638982457"))

bot = Bot(token=BOT_TOKEN)

def fetch_signal():
    """
    Simulates a real signal. You can upgrade this function later to pull from
    real sources, paid APIs, or MT5/TradingView.
    """
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    signal = {
        "pair": "XAUUSD (Gold)",
        "action": "BUY",
        "entry": "2345.50",
        "tp": "2352.00",
        "sl": "2340.00",
        "confidence": "✅ Confirmed | Triple Confluence",
        "time": now
    }
    return signal

def format_signal(signal, is_vip=False):
    """
    Format the message differently for Free and VIP channels.
    """
    if is_vip:
        return (
            f"🔥 VIP SIGNAL [{signal['time']}]\n"
            f"Pair: {signal['pair']}\n"
            f"Action: {signal['action']}\n"
            f"Entry: {signal['entry']}\n"
            f"TP: {signal['tp']}\n"
            f"SL: {signal['sl']}\n"
            f"{signal['confidence']}\n\n"
            f"Powered by ClarityFX ✅"
        )
    else:
        return (
            f"📢 FREE SIGNAL [{signal['time']}]\n"
            f"Pair: {signal['pair']}\n"
            f"Action: {signal['action']}\n"
            f"Entry: {signal['entry']}\n"
            f"TP/SL hidden 🔒\n"
            f"{signal['confidence']}\n\n"
            f"👉 For full details, subscribe to VIP.\n"
            f"Powered by ClarityFX"
        )

def post_to_channels():
    signal = fetch_signal()
    
    # Post to Free Channel
    free_msg = format_signal(signal, is_vip=False)
    bot.send_message(chat_id=FREE_CHANNEL_ID, text=free_msg)

    # Post to VIP Channel
    vip_msg = format_signal(signal, is_vip=True)
    bot.send_message(chat_id=VIP_CHANNEL_ID, text=vip_msg)

if __name__ == "__main__":
    logging.info("🤖 ClarityFX Bot Started...")
    
    while True:
        try:
            post_to_channels()
            logging.info("✅ Signals posted successfully.")
        except Exception as e:
            logging.error(f"Error posting signals: {e}")
        
        time.sleep(3600)  # Wait 1 hour before sending the next signal
