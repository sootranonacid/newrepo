import psycopg2

def test_connection():
    try:
        # Establish the connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123456789",
            host="192.168.200.86",
            port="5432"  # Ensure there are no leading zeros
        )
        print("Connection successful")

        # Create a cursor object
        cursor = conn.cursor()

        # Define the employee name
        employee_name = "Khaled"

        # Execute a query to fetch the salary of the employee named "Khaled"
        cursor.execute("SELECT salary FROM employees WHERE name = %s", ("fahad",))

        # Fetch the result (assumes only one result is returned)
        result = cursor.fetchone()

        if result:
            # Print the salary if found
            print(f"Salary of {employee_name}: {result[0]}")
        else:
            print(f"No employee found with the name {employee_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    test_connection()
