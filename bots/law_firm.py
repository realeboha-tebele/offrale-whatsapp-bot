# In production replace with Redis or SQLite for persistence
user_states = {}

LAW_FIRM_NAME = "[Firm Name]"
LAW_FIRM_PHONE = "[Phone Number]"
LAW_FIRM_ADDRESS = "[Address]"

def law_firm_bot(text: str, phone: str) -> str:
    text = text.lower().strip()
    state = user_states.get(phone, "new")

    # Always allow reset
    if text in ["menu", "main", "back", "0"]:
        user_states[phone] = "menu"
        return show_menu()

    if state == "new" or text in ["hi", "hello", "hey", "good morning",
                                   "good afternoon", "good evening", "hola"]:
        user_states[phone] = "menu"
        return (
            f"Welcome to {LAW_FIRM_NAME}! 👋\n\n"
            "We are here to assist you with your legal needs.\n\n"
            "Please select an option:\n"
            "1️⃣  Schedule a Consultation\n"
            "2️⃣  Our Practice Areas\n"
            "3️⃣  Office Hours & Location\n"
            "4️⃣  Fees & Billing\n"
            "5️⃣  Speak to a Consultant Now\n\n"
            "_Reply with a number_"
        )

    if state == "menu":
        if text == "1":
            user_states[phone] = "booking"
            return (
                "To schedule a consultation, please reply with:\n\n"
                "• Your *full name*\n"
                "• The *nature of your matter* (brief description)\n"
                "• Your *preferred date and time*\n\n"
                "We will confirm availability within 2 hours. ✅"
            )
        elif text == "2":
            return (
                f"*{LAW_FIRM_NAME}* specialises in:\n\n"
                "⚖️  Labour Law\n"
                "📝  Contract Drafting & Review\n"
                "🏢  Commercial Law\n"
                "👨‍👩‍👧  Family Law\n"
                "🏠  Property Law\n"
                "⚠️  Litigation & Dispute Resolution\n\n"
                "Reply *menu* to go back."
            )
        elif text == "3":
            return (
                f"📍 *Location:* {LAW_FIRM_ADDRESS}\n\n"
                "⏰ *Office Hours:*\n"
                "Monday – Friday: 8:00 AM – 5:00 PM\n"
                "Saturday: 9:00 AM – 12:00 PM\n\n"
                "📞 Direct line: " + LAW_FIRM_PHONE + "\n\n"
                "Reply *menu* to go back."
            )
        elif text == "4":
            return (
                "💼 *Consultation Fees:*\n\n"
                "Initial consultation: R500 (60 min)\n"
                "Thereafter billed at our standard hourly rate.\n\n"
                "We offer flexible payment options for ongoing matters.\n\n"
                "Reply *1* to book a consultation or *menu* to go back."
            )
        elif text == "5":
            user_states[phone] = "menu"
            return (
                "A consultant will contact you shortly. 📞\n\n"
                f"If the matter is urgent, please call us directly:\n"
                f"📞 {LAW_FIRM_PHONE}\n\n"
                "Office hours: Mon–Fri 8AM–5PM"
            )
        else:
            return (
                "I did not quite catch that. Please reply with a number:\n\n"
                + show_menu()
            )

    if state == "booking":
        # They've provided their booking info — acknowledge and alert staff
        user_states[phone] = "menu"
        return (
            "Thank you! ✅ Your consultation request has been received.\n\n"
            "A member of our team will contact you within *2 business hours* "
            "to confirm your appointment.\n\n"
            f"📞 If urgent: {LAW_FIRM_PHONE}\n\n"
            "Reply *menu* anytime to see options."
        )

    return "Reply *menu* to see your options, or call us on 📞 " + LAW_FIRM_PHONE

def show_menu():
    return (
        "How can we help you today?\n\n"
        "1️⃣  Schedule a Consultation\n"
        "2️⃣  Our Practice Areas\n"
        "3️⃣  Office Hours & Location\n"
        "4️⃣  Fees & Billing\n"
        "5️⃣  Speak to a Consultant Now"
    )
