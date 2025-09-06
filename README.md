# AdSoft - Advertisement Management System

A comprehensive Django-based web application for managing advertisements, user accounts, and approval workflows.

## 🚀 Features

- **User Authentication**: Custom user model with mobile number-based login
- **User Management**: Registration, login, password reset functionality
- **Dashboard**: Role-based dashboard for different user types
- **Enquiry Management**: Handle and track user enquiries
- **Approval System**: Admin approval workflow for various processes
- **Responsive Design**: Bootstrap-based modern UI

## 🛠️ Technology Stack

- **Backend**: Django 5.2
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Authentication**: Custom mobile number authentication backend
- **Email**: SMTP configuration for password reset

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8+
- MySQL Server
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd softads
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient
   ```

4. **Environment Configuration**
   
   Create a `.env` file in the project root with the following variables:
   ```env
   # Database Configuration
   DB_ENGINE=django.db.backends.mysql
   DB_NAME=your_database_name
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   
   # Email Configuration (Optional)
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=1
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. **Database Setup**
   
   Create a MySQL database and run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000`

## 📁 Project Structure

```
softads/
├── accounts/                 # User authentication and management
│   ├── models.py            # Custom user model
│   ├── views.py             # Login, signup, password reset views
│   ├── forms.py             # User registration forms
│   ├── backends.py          # Custom mobile number authentication
│   └── templates/           # Authentication templates
├── dashboard/               # Main dashboard application
│   ├── views.py             # Dashboard views
│   └── urls.py              # Dashboard URL patterns
├── enquiries/               # Enquiry management system
│   ├── models.py            # Enquiry models
│   ├── views.py             # Enquiry handling views
│   └── templates/           # Enquiry templates
├── approvals/               # Approval workflow system
│   ├── models.py            # Approval models
│   ├── views.py             # Approval management views
│   └── templates/           # Approval templates
├── adsoft/                  # Main project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── templates/               # Base templates
└── manage.py                # Django management script
```

## 🔐 Authentication System

The application uses a custom authentication system with the following features:

- **Mobile Number Login**: Users can log in using their mobile number
- **Custom User Model**: Extended user model with mobile number field
- **Dual Authentication**: Supports both mobile number and username authentication
- **Password Reset**: Email-based password reset functionality

### User Types

- **Regular Users**: Can access user dashboard and submit enquiries
- **Admin Users**: Can access admin dashboard and manage approvals

## 🎯 Usage

### For Regular Users

1. **Registration**: Sign up with mobile number, email, and password
2. **Login**: Use mobile number and password to log in
3. **Dashboard**: Access personalized dashboard after login
4. **Enquiries**: Submit and track enquiries

### For Admin Users

1. **Admin Login**: Use admin credentials to access admin panel
2. **User Management**: View and manage user accounts
3. **Approval System**: Review and approve pending requests
4. **Dashboard**: Access comprehensive admin dashboard

## 🔧 Configuration

### Database Configuration

The application supports MySQL database. Configure your database settings in the `.env` file:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=adsoft_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### Email Configuration

For password reset functionality, configure SMTP settings:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=1
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

## 🚀 Deployment

### Production Settings

Before deploying to production:

1. **Security Settings**
   - Set `DEBUG = False`
   - Update `SECRET_KEY`
   - Configure `ALLOWED_HOSTS`

2. **Database**
   - Use production database credentials
   - Run migrations: `python manage.py migrate`

3. **Static Files**
   - Collect static files: `python manage.py collectstatic`

4. **Environment Variables**
   - Set all required environment variables
   - Use secure email and database credentials

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 📝 API Endpoints

### Authentication
- `POST /accounts/login/` - User login
- `POST /accounts/signup/` - User registration
- `GET /accounts/password_reset/` - Password reset request
- `POST /accounts/password_reset/` - Password reset form

### Dashboard
- `GET /dashboard/` - Main dashboard (redirects based on user type)

### Enquiries
- `GET /enquiries/` - User enquiry dashboard
- `POST /enquiries/` - Submit new enquiry

### Approvals
- `GET /approvals/` - Admin approval dashboard
- `POST /approvals/update_status/` - Update approval status

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues in the repository
2. Create a new issue with detailed description
3. Contact the development team

## 🔄 Version History

- **v1.0.0** - Initial release with basic authentication and dashboard functionality
- **v1.1.0** - Added enquiry management system
- **v1.2.0** - Implemented approval workflow system

## 📞 Contact

For support and inquiries, please contact:
- Email's:  sanjithmit@gmail.com , v.varunprashanth@gmail.com
- Project Maintainers: Sanjith M , Varun Prashanth V

---

**Note**: This is a development version. For production deployment, ensure all security settings are properly configured and environment variables are set correctly.