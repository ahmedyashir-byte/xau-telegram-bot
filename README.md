# XAUBOT — Telegram Market Signal Bot

A self-hosted Telegram bot that analyzes XAU/USD and EUR/USD using
technical analysis (EMA, RSI, ATR, MACD) and delivers Buy/Sell signals
with Entry, Stop Loss, and Take Profit levels directly to your Telegram.

-----

## ⚡ Quick Start (5 minutes)

### Step 1 — Create your Telegram Bot

1. Open Telegram → search **@BotFather**
1. Send `/newbot` and follow the prompts
1. Copy the **token** it gives you (looks like `123456:ABC-DEF...`)

### Step 2 — Get your Chat ID

1. Search **@userinfobot** on Telegram → send `/start`
1. It will reply with your **Chat ID** (a number like `987654321`)

### Step 3 — Configure the bot

Open `config.py` and fill in:

```python
BOT_TOKEN = "123456:ABC-DEF..."   # from BotFather
CHAT_ID   = "987654321"           # from userinfobot
```

### Step 4 — Install dependencies

Make sure you have **Python 3.10+** installed, then:

```bash
pip install -r requirements.txt
```

### Step 5 — Run the bot

```bash
python bot.py
```

Open Telegram → find your bot → send `/start`

-----

## 📡 Bot Commands

|Command  |Description                        |
|---------|-----------------------------------|
|`/start` |Main menu with quick-action buttons|
|`/scan`  |Manually scan all markets now      |
|`/status`|View live prices for all symbols   |
|`/xauusd`|Analyze XAU/USD only               |
|`/eurusd`|Analyze EUR/USD only               |
|`/stop`  |Pause auto-scanning                |
|`/resume`|Resume auto-scanning               |
|`/help`  |Show help and signal logic         |

-----

## 📊 Signal Logic

Each signal requires **at least 3 of 5 conditions** to be true:

**BUY Signal:**

- EMA 20 crosses above EMA 50 (bullish trend)
- Price is above EMA 20
- RSI between 45–70 (momentum, not overbought)
- MACD histogram rising and positive
- Recent bullish price action (last 3 candles)

**SELL Signal:**

- EMA 20 crosses below EMA 50 (bearish trend)
- Price is below EMA 20
- RSI between 30–55 (momentum, not oversold)
- MACD histogram falling and negative
- Recent bearish price action

**SL / TP Sizing (ATR-based):**

- Stop Loss: 1.5× ATR from entry
- Take Profit 1: 2.0× ATR from entry (1:1.33 R:R)
- Take Profit 2: 3.5× ATR from entry (1:2.33 R:R)

-----

## ⚙️ Customization

Edit `config.py`:

```python
SYMBOLS = ["XAUUSD=X", "EURUSD=X"]  # Add/remove symbols
TIMEFRAME = "15m"                    # 1m, 5m, 15m, 1h, etc.
MIN_SIGNAL_STRENGTH = 3              # 1–5 stars (higher = fewer, stronger signals)
SCAN_INTERVAL_MINUTES = 15           # How often to auto-scan
```

-----

## 🚀 Run as a background service (Linux/Mac)

Create a systemd service or use `screen`:

```bash
screen -S xaubot
python bot.py
# Detach with Ctrl+A, D
```

Or with `nohup`:

```bash
nohup python bot.py > xaubot.log 2>&1 &
```

-----

## ⚠️ Disclaimer

This bot is for educational purposes only. Trading involves significant
risk. Always do your own analysis before entering any trade.

-----

## 📁 File Structure

```
xaubot/
├── bot.py          # Telegram bot & command handlers
├── analyzer.py     # Technical analysis engine
├── config.py       # Your settings & credentials
├── requirements.txt
└── README.md
```
