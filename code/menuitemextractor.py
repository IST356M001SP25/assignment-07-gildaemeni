if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price_str: str) -> float:
    # Remove any $ or comma characters
    cleaned_value = price_str.replace("$", "").replace(",", "")
    return float(cleaned_value)


def clean_scraped_text(raw_text: str) -> list[str]:
    segments = raw_text.split("\n")
    exclude_tags = {"NEW", "NEW!", "V", "GS", "S", "P"}
    filtered = []

    for segment in segments:
        segment = segment.strip()
        if not segment or segment in exclude_tags:
            continue
        filtered.append(segment)

    return filtered


def extract_menu_item(section: str, item_text: str) -> MenuItem:
    cleaned_parts = clean_scraped_text(item_text)

    if not cleaned_parts or len(cleaned_parts) < 2:
        return None  # safety check for bad data

    item_name = cleaned_parts[0]
    item_price = clean_price(cleaned_parts[1])
    item_description = cleaned_parts[2] if len(cleaned_parts) > 2 else "No description available."

    return MenuItem(category=section, name=item_name, price=item_price, description=item_description)


if __name__ == "__main__":
    pass

