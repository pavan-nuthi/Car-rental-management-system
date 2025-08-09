# Car Rental Management System

A web-based car rental management system built with **Streamlit** and **MySQL**.

## How It Works

The project is a simple car rental system with 4 main operations:

1. **Insert** - Add new cars and locations to the system
2. **Update** - Modify booking details (status, location, amount)
3. **Delete** - Remove bookings from the system  
4. **Query** - Run custom SQL queries for reports

## Project Structure

**Files Overview:**
- `CAR.py` - Main Streamlit app with navigation
- `OPERATIONS.py` - Business logic (insrt, updat, delet, quer functions)
- `CREATE_SCRIPTS.sql` - Database table creation
- `INSERT_SCRIPTS.sql` - Sample data insertion
- `QUERIES.sql` - Example analytical queries

## Database Tables

The system uses 5 main tables:
- `CUSTOMER_DETAILS` - Customer information
- `CAR_DETAILS` - Vehicle inventory  
- `LOCATION_DETAILS` - Pickup/drop locations
- `BOOKING_DETAILS` - Rental bookings
- `RENTS` - Links customers to cars and bookings

## Key Features

1. **Web Interface** - Easy-to-use Streamlit dashboard
2. **Car Management** - Add vehicles to fleet
3. **Location Management** - Manage rental locations
4. **Booking System** - Update/delete bookings
5. **Custom Queries** - Run SQL reports
6. **Sample Data** - Pre-loaded with test data

## Quick Setup

1. **Install Dependencies:**
```bash
pip install streamlit mysql-connector-python pandas streamlit-option-menu
```

2. **Setup Database:**
```sql
-- Step 1: Create the database
CREATE DATABASE car_rental;
USE car_rental;
```

   **Run SQL scripts in this exact order:**
   ```bash
   # Step 2: Create tables and constraints
   mysql -u root -p car_rental < CREATE_SCRIPTS.sql
   
   # Step 3: Create availability check function
   mysql -u root -p car_rental < CHECK_AVAILABILITY.sql
   
   # Step 4: Insert sample data
   mysql -u root -p car_rental < INSERT_SCRIPTS.sql
   
   # Step 5: Create trigger
   mysql -u root -p car_rental < INSERT_TRIGGER_FOR_BOOKING.sql
   ```
   
   **Or run from MySQL command line:**
   ```sql
   SOURCE CREATE_SCRIPTS.sql;
   SOURCE CHECK_AVAILABILITY.sql;
   SOURCE INSERT_SCRIPTS.sql;
   SOURCE INSERT_TRIGGER_FOR_BOOKING.sql;
   ```

3. **Configure Connection:**
Update MySQL credentials in `CAR.py`

4. **Run Application:**
```bash
streamlit run CAR.py
```
