# Hospital Management System

A simple Django-based hospital management system for managing patients, doctors, and appointments.

## Features

- **Patient Management**: Add, edit, view, and delete patient records
- **Doctor Management**: Manage doctor information and specializations
- **Appointment Scheduling**: Schedule appointments between patients and doctors
- **Dashboard**: Overview of hospital statistics
- **Admin Interface**: Full admin panel for data management

## Installation

1. **Clone or download the project**

2. **Create a virtual environment** (if not already done):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install django
   ```

5. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel
- Access the admin panel at `/admin/`
- Use the superuser credentials you created
- Manage all data through the Django admin interface

### Main Application
- **Home**: Dashboard with statistics and quick actions
- **Patients**: View, add, edit, and delete patient records
- **Doctors**: Manage doctor information and specializations
- **Appointments**: Schedule and manage appointments

### Default Admin Credentials
- Username: `admin`
- Password: (you'll need to set this when creating the superuser)

## Models

### Patient
- Name, age, gender, phone, address
- Registration date tracking

### Doctor
- Name, specialization, phone, email
- Specializations: Cardiology, Neurology, Orthopedics, Pediatrics, General Medicine

### Appointment
- Links patients and doctors
- Date, time, status (Scheduled, Completed, Cancelled)
- Notes field for additional information

## Features

- **Responsive Design**: Works on desktop and mobile devices
- **Simple Interface**: Clean, minimal styling as requested
- **CRUD Operations**: Full Create, Read, Update, Delete functionality
- **Data Validation**: Form validation and error handling
- **Search and Filter**: Admin interface includes search and filtering
- **Relationship Management**: Proper foreign key relationships between models

## File Structure

```
hospital_management/
├── core/
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin interface configuration
│   └── templates/core/    # HTML templates
├── hospital_management/
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── manage.py              # Django management script
└── README.md              # This file
```

## Customization

The system is designed to be simple and extensible. You can:

- Add new fields to models in `core/models.py`
- Create new views in `core/views.py`
- Add new templates in `core/templates/core/`
- Modify styling in the base template

## Requirements

- Python 3.7+
- Django 4.0+

## License

This is a basic hospital management system created for educational purposes. 