import time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="test vs 01", bucket_key="TestVS01", access_key="wG71Gvo3snZBIpLvdzVHqcjmtJAzWEmx", debug_level=2)

streamer.log("My Messages", "Stream Starting")
for num in range(1, 20):
    time.sleep(0.1)
    streamer.log("My Numbers", num)
    print(num)
streamer.log("My Messages", "Stream Done")
streamer.close()
