from base_de_dados.database import engine
from base_de_dados.models import Base

import base_de_dados.models

Base.metadata.create_all(engine)