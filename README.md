🛒 Amazon Product Scraper (Python + Selenium + BeautifulSoup)

This project is a simple Amazon India product scraper built with Python, Selenium, and BeautifulSoup.
It searches for a product keyword, scrapes multiple pages of results, and saves product details into a CSV file.

Currently, it collects:

Product name

Price

Rating

Rating count

Product URL

The output is stored in results.csv.

🚀 Features

Automated browser control using Selenium

HTML parsing with BeautifulSoup

Extracts data from up to 20 pages of Amazon search results

Saves structured data using Pandas

Easy to customize search keywords

🧰 Tech Stack

Python 3

Selenium

BeautifulSoup4

Pandas

Chrome WebDriver

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install dependencies
pip install selenium beautifulsoup4 pandas

3. Install ChromeDriver

Download ChromeDriver matching your Chrome version:

https://sites.google.com/chromium.org/driver/

Place it in your system PATH or project folder.

▶️ How to Run

Simply run:

python main.py


By default, it searches for:

main('bags')


You can change this to any keyword:

main('laptops')

📁 Output

After execution, a file named:

results.csv


will be created containing:

| product | price | rating | rating_count | product url |
