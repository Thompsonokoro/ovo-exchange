import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Wallet", callback_data="wallet"), InlineKeyboardButton("🔄 Exchange", callback_data="exchange")],
        [InlineKeyboardButton("👥 P2P Trading", callback_data="p2p"), InlineKeyboardButton("📊 Rates", callback_data="rates")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    text = (
        "Welcome to *OVO Exchange* 🇳🇬\n\n"
        "Africa Pay Platform | Wallet, Exchange & P2P for Africa\n\n"
        "Choose an option below:"
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    back = [[InlineKeyboardButton("⬅️ Back to Menu", callback_data="home")]]

    if data == "home":
        await start(update, context)
        return
    elif data == "wallet":
        msg = "💰 *Your Wallet*\n\nNGN Balance: ₦0.00\nUSDT Balance: 0.00\n\nDeposit coming soon. Tap Back to continue."
    elif data == "exchange":
        msg = "🔄 *Exchange*\n\n1 USDT = ₦1,650\n1 BTC = ₦145,000,000\n\nSelect a pair to trade. Coming soon."
    elif data == "p2p":
        msg = "👥 *P2P Trading*\n\nBuy / Sell USDT with Naira traders.\n\nNo active offers yet. Check back soon."
    elif data == "rates":
        msg = "📊 *Today's Rates*\n\nUSDT/NGN: ₦1,650\nBTC/NGN: ₦145,000,000\nETH/NGN: ₦5,200,000"
    elif data == "help":
        msg = "❓ *Help*\n\nUse /start to open menu.\nSupport: @OVOExchangeSupport"
    else:
        msg = "Coming soon."

    await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(back), parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("OVO Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
