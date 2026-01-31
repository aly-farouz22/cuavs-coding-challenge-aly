import pandas as pd
import json
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def main():
    sensor1 = pd.read_csv("SensorData1.csv", dtype={"id": int})
    with open("SensorData2.json") as f:
        sensor2 = pd.DataFrame(json.load(f)).astype({"id": int})

    matches = set()

    for _, row1 in sensor1.iterrows():
        for _, row2 in sensor2.iterrows():
            distance = haversine(
                row1["latitude"],
                row1["longitude"],
                row2["latitude"],
                row2["longitude"]
            )
            if distance <= 100:
                matches.add((row1["id"], row2["id"]))

    output = pd.DataFrame(list(matches), columns=["Sensor1_ID", "Sensor2_ID"])
    output.to_csv("MatchedReadings.csv", index=False)

    print(f"Found {len(matches)} matches. Output saved to MatchedReadings.csv")

if __name__ == "__main__":
    main()
