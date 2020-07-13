from src.app import *
from src.config import *
from src.controllers.get import *
from src.controllers.create import *

app.run("0.0.0.0", PORT, debug=True)