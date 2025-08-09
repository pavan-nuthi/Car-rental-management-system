# Car Rental Management System

A web-based car rental management system built with **Streamlit** and **MySQL**.

## How It Works

The project is a simple car rental system with 4 main operations:

1. **Insert** - Add new cars and locations to the system
2. **Update** - Modify booking details (status, location, amount)
3. **Delete** - Remove bookings from the system  
4. **Query** - Run custom SQL queries for reports

## Project Structure

- **`CAR.py`** - Main application with Streamlit UI
- **`OPERATIONS.py`** - Contains all CRUD functions
- **SQL Files** - Database setup and sample data

## Database Tables

The system uses 5 main tables:
- `CUSTOMER_DETAILS` - Customer information
- `CAR_DETAILS` - Vehicle inventory  
- `LOCATION_DETAILS` - Pickup/drop locations
- `BOOKING_DETAILS` - Rental bookings
- `RENTS` - Links customers to cars and bookings

## Key Features

✅ **Web Interface** - Easy-to-use Streamlit dashboard
✅ **Car Management** - Add vehicles to fleet
✅ **Location Management** - Manage rental locations
✅ **Booking System** - Update/delete bookings
✅ **Custom Queries** - Run SQL reports
✅ **Sample Data** - Pre-loaded with test data

## Quick Setup

1. **Install Dependencies:**
```bash
pip install streamlit mysql-connector-python pandas streamlit-option-menu
```

2. **Setup Database:**
```sql
CREATE DATABASE car_rental;
-- Run the SQL scripts in order
```

3. **Configure Connection:**
Update MySQL credentials in `CAR.py`

4. **Run Application:**
```bash
streamlit run CAR.py
```

## Important Notes

⚠️ **Known Issues:**
- Trigger file has a bug (references wrong table)
- Custom query interface allows SQL injection
- Limited CRUD operations (Insert: CAR/LOCATION only, Update/Delete: BOOKING only)

**Files Overview:**
- `CAR.py` - Main Streamlit app with navigation
- `OPERATIONS.py` - Business logic (insrt, updat, delet, quer functions)
- `CREATE_SCRIPTS.sql` - Database table creation
- `INSERT_SCRIPTS.sql` - Sample data insertion
- `QUERIES.sql` - Example analytical queries