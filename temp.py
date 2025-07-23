import db
import models  # Make sure this line is BEFORE create_table()

# This ensures models are registered with Base before creating tables
db.create_table()
