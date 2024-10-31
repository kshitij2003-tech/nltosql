import pandas as pd
import sqlite3

# Load the CSV file into a DataFrame
csv_file_path = "C:/Users/Kshitij/Desktop/dbmspro/sqlchatbot1/bollywood_movie.csv"  # Replace with the actual path
df = pd.read_csv(csv_file_path)

# Connect to SQLite (creates a new database file if it doesn't exist)
conn = sqlite3.connect('bollywood_movies.db')
cursor = conn.cursor()

# Insert data from DataFrame into the SQLite table, replacing if exists
df.to_sql('movies', conn, if_exists='replace', index=False)

# Commit changes
conn.commit()

# Sample Query: Retrieve top 5 movies with the highest IMDb rating
sample_query = '''
SELECT Title, IMDb_Rating, Audience_Score, Box_Office_Millions
FROM Movies
ORDER BY IMDb_Rating DESC
LIMIT 5
'''
# Execute the sample query
result = cursor.execute(sample_query).fetchall()

# Display the result
print("Top 5 Movies by IMDb Rating:")
for row in result:
    print(row)

# Close the connection
conn.close()
