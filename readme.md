# Pulporo: Your Financial Freedom Companion (Pre-Alpha)

## Are you tired of juggling between ugly spreadsheets or dealing with shallow apps that offer confusing pie charts? 

Say hello to Pulporo - the go-to for startup-minded individuals seeking clarity and control. 
With Pulporo, managing finances isn't just about numbers; it's about gaining true financial freedom.

![Pulporo_Preview.png](static/photos/Pulporo_Preview.png)
<small>Disclaimer: The image displayed represents a potential appearance and features of Pulporo. Actual app appearance and functionality may vary. </small>

**Key Features:**
1. **Personal "Runway" Counter:** Visualize your financial freedom as your runway counter grows, indicating how long you can sustain without additional income.
2. **Cash Flow Log:** Seamlessly track your daily incomes and outcomes, enabling you to identify and address bottlenecks in your cash flow, ensuring financial clarity and efficiency at every step.
3. **Clear Charts:** Customize charts to your needs and gain a bird's-eye view of your expenses without sacrificing laser precision.
4. **Expense Segmentation:** Distinguish one-time expenses from subscriptions to optimize spending.
5. **Projections:** Plan ahead with income and expense projections for years to come.
6. **Payment History:** Track service price changes over time with payment history attached to subscriptions.
7. **Custom Reminders for Every Need:** Plan payments for products or services, and set reminders for anything that matters to you. From paying invoices and contractors to tracking warranty expirations, Pulporo ensures you never miss a beat.
8. **Centralized Document Management:** Attach any document to your financial operations for future reference with Pulporo. Whether it's receipts, invoices, or investment papers, keep everything in one convenient location for quick access whenever you need it.
9. **Financial Goals:** Set and track progress towards your financial goals effortlessly.
10. **Crypto Wallet Integration:** Seamlessly integrate with crypto wallets for comprehensive financial management.
11. **Bank Integration:** Connect with major banks like Bank of America, Millennium, Pekao, and more for streamlined transactions.
12. **Instant Access:** Find anything you need whenever you need it with Pulporo's intuitive search functionality.

## How to install and set up the project

### Install Python and SQLite (if needed)
If you don't have Python 3.12 or SQLite installed on your system, follow these steps:
1. **Python 3.12 Installation:**
   - Download Python 3.12 from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

2. **SQLite Installation:**
   - SQLite is included with Python, so if you installed Python 3.12, you should already have SQLite available. If not, you can download SQLite from the [official SQLite website](https://www.sqlite.org/download.html) and follow the installation instructions for your operating system.

### Project Setup (Under 1 min)
1. Clone this project
   ``` bash
   git clone https://github.com/Zimzozaur/Pulporo-API
   ```
2. Move to project
    ```
    cd Pulporo-API
    ```
3. Create virtual env in project directory 
   ```
   python -m venv venv
   ```
4. Activate virtual env:
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
5. Install dependencies from requirements.txt
   ```
   pip install -r requirements.txt
   ```
6. Set up SQLite db:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Create a fixture and load data to db 
    ```
   python manage.py load_fixture_now
    ```
8. Run app in browser
   ```
    python manage.py runserver
   ```
9. Type in browser - http://127.0.0.1:8000/

## Find a bug?

If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!


