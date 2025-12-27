import os

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def get_itinerary(query: str) -> str:
    """
    Generates a travel itinerary.
    If OpenAI API quota is unavailable, returns a fallback demo itinerary.
    """

    # -------------------------------
    # 1️⃣ Try OpenAI API (if available)
    # -------------------------------
    if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
        try:
            client = OpenAI()

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
You are a professional travel planner.

Create a detailed, budget-friendly travel itinerary for the following request:

{query}

Include:
- Transport options with cost
- Budget hotels
- Day-wise plan
- Approximate total budget
""",
            )

            return response.output_text

        except Exception as e:
            # If quota exceeded or any API error → fallback
            print("OpenAI API error, switching to demo mode:", e)

    # ---------------------------------
    # 2️⃣ FALLBACK DEMO ITINERARY (SAFE)
    # ---------------------------------
    return f"""
🧳 **3-Day Budget Trip: Delhi → Goa (Demo Mode)**

✈ **Travel Options**
- Train (Sleeper / 3A): ₹1,200 – ₹2,500
- Budget Flight (IndiGo / Akasa): ₹3,000 – ₹4,500

🏨 **Stay (Budget-Friendly)**
- Hostels / Guesthouses: ₹800 – ₹1,200 per night
- Areas: Baga, Calangute, Anjuna

---

📅 **Day 1**
- Arrival in Goa
- Relax at **Baga Beach**
- Evening street food & sunset views

📅 **Day 2**
- Fort Aguada
- Anjuna Beach & Flea Market
- Beach shack dinner

📅 **Day 3**
- Basilica of Bom Jesus
- Panaji city walk
- Shopping & return journey

---

💰 **Estimated Budget (per person)**
- Travel: ₹2,000 – ₹4,000
- Stay: ₹2,500 – ₹3,500
- Food & travel: ₹2,000
- **Total:** ₹7,000 – ₹10,000

⚠ *This output is shown in demo mode due to API quota limits.*
"""
