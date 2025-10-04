# !pip install playwright nest_asyncio faker > /dev/null
# !playwright install chromium > /dev/null

import asyncio
import nest_asyncio
import os, json, random, datetime
from faker import Faker
from playwright.async_api import async_playwright

nest_asyncio.apply()
fake = Faker()

# Generate fake passenger details
def generate_passenger():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone": fake.msisdn()[:10],
        "email": fake.email(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 60)
    }

# Main booking flow
async def run_booking_flow(site="demo", selection_criteria="price", headless=True):
    passenger = generate_passenger()
    travel_date = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%d/%m/%Y")
    result = {}

    try:
        async with async_playwright() as p:
            print("[INFO] Launching browser...")
            browser = await p.chromium.launch(headless=headless)
            context = await browser.new_context()
            page = await context.new_page()

            # DEMO site instead of MakeMyTrip/Goibibo (real sites block automation)
            html = f"""
            <html>
              <body>
                <h3>Available Flights DEL → BOM</h3>
                <table border="1">
                  <tr><th>Airline</th><th>Departure</th><th>Arrival</th><th>Duration</th><th>Price</th></tr>
                  <tr><td>IndiGo</td><td>08:00</td><td>09:45</td><td>1h 45m</td><td>₹3500</td></tr>
                  <tr><td>SpiceJet</td><td>10:30</td><td>12:05</td><td>1h 35m</td><td>₹3200</td></tr>
                  <tr><td>Air India</td><td>14:00</td><td>16:00</td><td>2h 00m</td><td>₹4000</td></tr>
                </table>
              </body>
            </html>
            """
            html_path = "demo_flights.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)

            await page.goto("file://" + os.path.abspath(html_path))
            await page.screenshot(path="outputs/demo_flights.png")

            # Extract flights
            rows = await page.locator("table tr").all()
            flights = []
            for row in rows[1:]:
                cols = await row.locator("td").all_inner_texts()
                flights.append({
                    "airline": cols[0],
                    "departure_time": cols[1],
                    "arrival_time": cols[2],
                    "duration": cols[3],
                    "price": cols[4]
                })

            # Select flight
            if selection_criteria == "price":
                chosen = min(flights, key=lambda x: int(x["price"].replace("₹","").strip()))
            else:
                chosen = min(flights, key=lambda x: int(x["duration"].split("h")[0])*60 + int(x["duration"].split("h")[1].replace("m","").strip()))

            # Save final result
            result = {
                "site": site,
                "booking_status": "ready_for_payment",
                "passenger": passenger,
                "travel_date": travel_date,
                **chosen,
                "screenshot": "outputs/demo_flights.png"
            }

            os.makedirs("outputs", exist_ok=True)
            with open("outputs/final_result.json", "w") as f:
                json.dump(result, f, indent=2)

            await browser.close()
            print("[INFO] Browser closed successfully.")

    except Exception as e:
        print(f"[ERROR] {e}")

    return result

# Helper to run in Colab/Jupyter
def run_async(coro):
    try:
        return asyncio.run(coro)
    except RuntimeError:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro)

# Execute
if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    final_result = run_async(run_booking_flow(site="demo", selection_criteria="price", headless=True))
    print("\n==== Final Result ====")
    print(json.dumps(final_result, indent=2))

