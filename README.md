# Sauce E-commerce Automation Test

This repository contains an automated test case for ordering an item on the Sauce Demo e-commerce website using **Python**, **Selenium**, and the **pytest** framework.  
The test covers the entire user journey: login, add to cart, checkout, and place order.

## 🧪 What’s Automated?

- **Login** to the Sauce Demo website
- **Add an item to the shopping cart**
- **Proceed to checkout**
- **Enter customer information and place the order**
- **Verify order completion**

## 🛠️ Tech Stack

- **Language:** Python
- **Automation:** Selenium WebDriver
- **Testing Framework:** pytest

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Kavita-B-tester/sauce_online_shop.git
cd sauce_online_shop
```

### 2. Install Dependencies

Make sure you have Python installed (3.7+ recommended), then install requirements:

```bash
pip install selenium
pip install pytest

```

> **Note:** Download the appropriate [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) or [geckodriver](https://github.com/mozilla/geckodriver/releases) and add it to your system PATH.

### 3. Run the Test

```bash
pytest test_e2e1framework.py
```

## 📄 Example Test Flow

The main test script performs the following actions:

1. **Opens** the Sauce Demo website
2. **Logs in** with standard credentials
3. **Adds** an item to the cart
4. **Navigates** to the cart and proceeds to checkout
5. **Fills in** customer details
6. **Places** the order
7. **Asserts** that the order was successful

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

## 📝 License

MIT.

---

**Author:** [Kavita-B-tester](https://github.com/Kavita-B-tester)
website:https://www.saucedemo.com/
