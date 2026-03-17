from sqlalchemy import *
from database import engine
from models import Base

import models

Base.metadata.create_all(engine)