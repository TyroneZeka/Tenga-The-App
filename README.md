# Tenga
## An E-commerce Website

This is a fully functional e-commerce website built with **Django 4.0** (Backend) and **Bootstrap** (Frontend). The website includes key features such as **authentication & authorization**, a **search mechanism** for filtering products, and a **payment integration** using the PayPal SDK.

## Features

- User authentication (Sign up, Login, Logout)
- Product search and filtering
- Product catalog with details (Single product view)
- Cart and checkout functionality
- PayPal integration for payments
- Responsive design with Bootstrap
- Admin panel for product management

## Prerequisites

To run this project locally, ensure you have the following installed on your system:

- **Python 3.8+**
- **Django 4.0**
- **Pip** (Python package manager)
- **Virtualenv** (recommended for isolating dependencies)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TyroneZeka/Tenga-The-App.git
cd your-tenga-app
```

### 2. Set up a Virtual Environment

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Access the website in your browser at `http://127.0.0.1:8000/`.


## Screenshots

- **Home Page**

  ![Home Page](https://github.com/TyroneZeka/Tenga-The-App/blob/main/images/home.png?raw=true)

- **Single Product View**

  ![Single Product View](https://github.com/TyroneZeka/Tenga-The-App/blob/main/images/single.png?raw=true)

- **Cart View**

  ![Cart View](https://github.com/TyroneZeka/Tenga-The-App/blob/main/images/cart.png?raw=true)

- **Checkout Page**

  ![Checkout Page](https://github.com/TyroneZeka/Tenga-The-App/blob/main/images/checkout.png?raw=true)


## Usage

- **Authentication**: Users can sign up, log in, and log out to access the site.
- **Product Search**: Use the search bar to filter products by name or category.
- **Cart and Checkout**: Add products to the cart and proceed to checkout with PayPal payment integration.
- **Admin Panel**: Visit `http://127.0.0.1:8000/admin` to manage products and orders (requires admin login).

## Payment Integration (PayPal SDK)

The PayPal integration is set up using the official PayPal SDK. Ensure that your PayPal client ID and secret are set up in your `.env` file. The sandbox mode is enabled during development for testing payments.

For more details on setting up PayPal SDK, refer to the [official PayPal documentation](https://developer.paypal.com/docs/checkout/integrate/).

## Technologies Used

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Django 4.0, Python 3.8+
- **Database**: SQLite (default Django database)
- **Payment Gateway**: PayPal SDK

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute!

## License

This project is licensed under the MIT License.