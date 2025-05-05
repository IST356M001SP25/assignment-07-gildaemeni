# Reflection

Student Name:  Gilda Emeni
Sudent Email:  gemeni@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This assignment taught me how to use Playwright with Python to perform web scraping on real-world websites, specifically extracting structured data from HTML using CSS selectors. I learned how to navigate sibling elements in the DOM using `query_selector("~ *")` and how important it is to wait for elements to load on dynamic pages like those from the Wayback Machine.

One area I struggled with was figuring out why my scraper wasn’t producing the expected output file. It turned out that the issue wasn’t with my scraping logic, but with how Python treats package imports when running scripts from different folders. I had to debug import errors like `ModuleNotFoundError: No module named 'code.menuitem'`, which helped me better understand Python’s module system and the use of `__init__.py` files. I also learned how to resolve path issues using `PYTHONPATH=.` when executing scripts.

I still want more practice with writing robust scraping logic that handles slow-loading or incomplete pages. I also realized that testing scraping scripts requires carefully checking selectors and print statements to verify that items are being collected correctly before writing to a CSV.

Overall, this assignment helped me build confidence in combining multiple tools such as Playwright, Pandas, and dataclasses into a working ETL pipeline. I feel more prepared for data extraction tasks in future projects.

