# Product Price Alert System

## Overview

This Python script monitors the price of a product on Flipkart and sends an email alert if the price drops below a specified threshold. The script utilizes web scraping to extract product prices and an email service to send notifications.

## Packages Used

- `requests`: To make HTTP requests to the product page.
- `BeautifulSoup`: To parse HTML and extract the product price.
- `datetime`: To handle date and time operations.
- `smtplib`: To send email notifications.
- `email.mime.multipart` and `email.mime.text`: To compose and format the email.

## Author

Sachin S

## Setup Instructions

1. **Install Required Packages**

   Ensure you have Python installed. You can install the necessary packages using pip:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Configure Email**

   Update the following variables with your email details:

   - `email`: Your email address (e.g., `"your_email@gmail.com"`)
   - `email_pass`: Your email app password (e.g., `"your_app_password"`)
   - `to_email`: The recipient's email address

   Make sure to replace `"YOUR_EMAIL"`, `"YOUR_EMIL_APP_PASSWORD"`, and `"RECIPIENT_MAIL"` in the script.

3. **Modify Product Link and Target Price**

   Update the `link` variable with the URL of the product you want to monitor. Adjust the `target_amount` to set your desired price threshold.

4. **Set Daily Check Time**

   Adjust `daily_checker_time` to the time you want to run the price check each day (in `HH:MM` format).

5. **Run the Script**

   Execute the script to start monitoring the product price:

   ```bash
   python your_script_name.py
   ```

## How It Works

1. The script sends an HTTP request to the specified product page URL.
2. It parses the HTML to find the product price using BeautifulSoup.
3. The price is compared to the target amount set in `target_amount`.
4. If the price is below the target amount, an email notification is sent.
5. The script checks the current time against `daily_checker_time` to determine when to run the price check.

## Code Explanation

- **Imports**: Import necessary libraries for web scraping, date/time handling, and email functionality.
- **Variables**: Define email credentials, product URL, HTML tag and class for price extraction, target price, and daily check time.
- **Functions**:
  - `price(tag_name, aclass)`: Scrapes the product price from the HTML and appends it to `daily_price` and `price_dates` lists.
  - `sendmail()`: Composes and sends an email notification if the product price meets the target amount.
- **Main Logic**:
  - Checks the current time.
  - Scrapes the price and sends an email if the price is below the target amount.

## Notes

- Ensure that your email provider allows SMTP access and that you use an app-specific password if required.
- Modify the `div` tag and `aclass` in the `price` function if the HTML structure of the product page changes.
