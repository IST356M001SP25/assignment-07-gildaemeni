import re
import os
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    import os

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Use archived version of the site
    page.goto("https://web.archive.org/web/20241111165815/https://www.tullysgoodtimes.com/menus/")
    page.wait_for_selector("h3.foodmenu__menu-section-title", timeout=10000)
    print("Page loaded, starting scrape...")

    menu_data = []

    headers = page.query_selector_all("h3.foodmenu__menu-section-title")
    print(f"Found {len(headers)} section headers")

    for header in headers:
        category = header.inner_text()
        print("SECTION:", category)

        # Get the second next sibling element (div.row)
        first_sibling = header.query_selector("~ *")
        second_sibling = first_sibling.query_selector("~ *") if first_sibling else None

        if not second_sibling:
            print("  ⚠️ Skipped section due to missing item block")
            continue

        item_blocks = second_sibling.query_selector_all("div.foodmenu__menu-item")
        print(f"  Found {len(item_blocks)} items in this section")

        for block in item_blocks:
            raw = block.inner_text()
            item = extract_menu_item(category, raw)
            if item:
                menu_data.append(item.to_dict())
                print("   ✔️", item.name)

    print("TOTAL ITEMS SCRAPED:", len(menu_data))

    os.makedirs("cache", exist_ok=True)
    df = pd.DataFrame(menu_data)
    df.to_csv("cache/tullys_menu.csv", index=False)

    context.close()
    browser.close()



if __name__ == "__main__":
    with sync_playwright() as playwright:
        tullyscraper(playwright)
