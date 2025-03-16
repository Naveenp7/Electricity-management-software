import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Add missing columns to the appliances table
cursor.execute("ALTER TABLE appliances ADD COLUMN appliance_name TEXT;")
cursor.execute("ALTER TABLE appliances ADD COLUMN avg_hours_used REAL;")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Schema updated successfully.")
