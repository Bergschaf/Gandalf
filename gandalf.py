import pause
from datetime import datetime
import os

pause.until(datetime(2023, 9, 8, 10, 52, 50))

os.system("playerctl play")
