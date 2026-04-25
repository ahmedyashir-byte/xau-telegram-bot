# ─────────────────────────────────────────────

# XAUBOT CONFIGURATION

# ─────────────────────────────────────────────

# 1. Get your token from @BotFather on Telegram

BOT_TOKEN = “8309442490:AAHk1h3gCw-gS7esQjjZjpLCToxLXTOUsdA”

# 2. Your Telegram chat/user ID (get it from @userinfobot)

# Leave empty to disable auto-push; use /scan manually

CHAT_ID = “6185290624”

# ── Market Settings ──────────────────────────

SYMBOLS = [
“XAUUSD=X”,   # Gold / USD  (XAU/USD)
“EURUSD=X”,   # Euro / USD
# “GBPUSD=X”, # Uncomment to add GBP/USD
]

# Yahoo Finance interval: 1m, 5m, 15m, 30m, 1h, 1d

TIMEFRAME = “15m”

# ── Signal Settings ──────────────────────────

# Minimum signal strength (1-5 stars) to trigger an alert

MIN_SIGNAL_STRENGTH = 3

# How often to auto-scan (in minutes)

SCAN_INTERVAL_MINUTES = 15
