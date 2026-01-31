## Canadian UAVs Coding Challenge

This script correlates anomaly detections from two sensors using geospatial proximity.

### Approach
- Load SensorData1.csv and SensorData2.json
- Compute distance using Haversine formula
- Associate readings within 100 meters
- Output matched ID pairs to MatchedReadings.csv

### How to Run
```bash
pip install pandas
python correlate_sensors.py
