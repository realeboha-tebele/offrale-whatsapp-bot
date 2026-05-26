# clients.py
# Add a new client here every time you onboard one.
# You never need to create a new bot file.

CLIENTS = {

    # ── LAW FIRMS ──────────────────────────────────────────────

    "PHONE_ID_PEETJA": {
        "type": "law_firm",
        "name": "PR Peetja Attorneys Inc",
        "phone": "069 217 3099",
        "address": "88 Jorissen Street, 3rd Floor, Braamfontein",
        "services": [
            "Labour Law",
            "Contract Drafting & Review",
            "Commercial Law",
            "Family Law",
            "Litigation & Dispute Resolution"
        ],
        "hours": "Mon–Fri 8AM–5PM | Sat 9AM–12PM",
        "consultation_fee": "R500"
    },

    "PHONE_ID_KO_ATTORNEYS": {
        "type": "law_firm",
        "name": "KO Attorneys Inc",
        "phone": "011 455 7100",
        "address": "Bedfordview, Johannesburg",
        "services": [
            "Labour Law & CCMA",
            "Commercial Law",
            "Criminal Law",
            "Family Law",
            "Debt Collection"
        ],
        "hours": "Mon–Fri 8AM–5PM",
        "consultation_fee": "R600"
    },

    # ── MEDICAL PRACTICES ───────────────────────────────────────

    "PHONE_ID_SANDTON_MED": {
        "type": "medical",
        "name": "Sandton Medical Centre",
        "phone": "011 XXX XXXX",
        "address": "123 Rivonia Road, Sandton",
        "services": [
            "General Practitioner",
            "Chronic Disease Management",
            "Occupational Health Certificates",
            "Minor Procedures"
        ],
        "hours": "Mon–Fri 8AM–5PM | Sat 9AM–1PM",
        "emergency": "10177"
    },

    # ── DEALERSHIPS ─────────────────────────────────────────────

    "PHONE_ID_IRON_MOTORS": {
        "type": "dealership",
        "name": "Iron Motors",
        "phone": "011 XXX XXXX",
        "address": "456 Main Reef Road, Johannesburg",
        "hours": "Mon–Fri 8AM–6PM | Sat 8AM–4PM",
        "stock_url": "https://ironmotors.co.za/stock"
    },

}
