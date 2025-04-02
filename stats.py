from collections import Counter

def get_num_words(text: str) -> int:
    return len(text.split())


def character_frequencies(text: str) -> dict[str, int]:
    """Convert characters to lowercase and remove non-alphabetic characters"""
    return dict(Counter("".join(char for char in text.lower() if char.isalpha())))


def ordered_frequencies(items: dict[str, int]) -> list[dict[str, str | int]]:
    """Sort items by decreasing frequency and return "name": character, "count": count"""
    items = sorted(items.items(), key=lambda x: x[1], reverse=True) 
    return [{"character": char, "count": count} for char, count in items]
