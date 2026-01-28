import requests
import pandas as pd
import time
import os

# ---------------- CONFIG ----------------
INPUT_CSV = "Stations.csv"
OUTPUT_CSV = "output/Fares.csv"  # SAME FILE
BASE_URL = "https://portal.upmetrorail.com/en/api/v2/route"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}

REQUEST_DELAY = 0.5
# ---------------------------------------


def build_url(from_code, to_code):
    return (
        f"{BASE_URL}/{from_code}/{to_code}"
        f"/station/station/least-distance/1970-01-01/"
    )


def main():
    df = pd.read_csv(INPUT_CSV)

    station_codes = df["station_code"].tolist()
    station_names = dict(
        zip(df["station_code"], df["station_name"])
    )

    results = []

    total_calls = len(station_codes) * (len(station_codes) - 1)
    call_count = 0

    for from_code in station_codes:
        for to_code in station_codes:
            if from_code == to_code:
                continue

            call_count += 1
            print(f"ðŸ”„ {call_count}/{total_calls} : {from_code} â†’ {to_code}")

            url = build_url(from_code, to_code)

            try:
                response = requests.get(url, headers=HEADERS, timeout=15)

                if response.status_code != 200:
                    print(f"âŒ Failed ({response.status_code})")
                    continue

                data = response.json()

                route_list = data.get("route", [])
                if not route_list:
                    continue

                # Extract full path
                path = route_list[0].get("path", [])
                station_path = [p["name"] for p in path]

                # Intermediate stations only
                intermediate_stations = station_path[1:-1]

                results.append({
                    "from_station_code": from_code,
                    "from_station_name": station_names.get(from_code),
                    "to_station_code": to_code,
                    "to_station_name": station_names.get(to_code),
                    "fare": data.get("fare"),
                    "total_time": data.get("total_time"),
                    "intermediate_station_count": len(intermediate_stations),
                    "intermediate_station_names": ", ".join(intermediate_stations)
                })

            except Exception as e:
                print(f"âš ï¸ Error: {e}")

            time.sleep(REQUEST_DELAY)

    os.makedirs("output", exist_ok=True)

    # ðŸ”¥ OVERWRITE SAME CSV FILE
    pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)

    print(f"\nâœ… CSV UPDATED (overwritten): {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
