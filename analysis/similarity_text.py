# orginal_text = "This is a test for student writing again"
# user_speech_text = "This is a student for student speeching test writing again"

# Output: "This is a [uncorrect][student][test] for student [uncorrect][speeching test][] writing again"

import difflib


def highlight_differences(original_text, user_speech_text):
    # Split both texts into words
    original_words = original_text.split()
    user_speech_words = user_speech_text.split()

    # Use difflib to compare the two lists of words
    diff = list(difflib.ndiff(original_words, user_speech_words))

    # Build the result string
    result = []
    for word in diff:
        if word.startswith(" "):
            result.append(word[2:])  # Correct word
        elif word.startswith("-"):
            result.append(f"[missing][{word[2:]}]")  # Missing word in user's text
        elif word.startswith("+"):
            result.append(f"[uncorrect][{word[2:]}]")  # Extra word in user's text

    return " ".join(result)


# Example usage:
original_text = "This is a test for student writing again"
user_speech_text = "This is a student1 student for student speeching test writing again"

output = highlight_differences(original_text, user_speech_text)
print(output)
