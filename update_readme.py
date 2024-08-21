import os
import re

SOLUTIONS_DIR = '.'

LANG_EXTENSIONS = {
    'C++': '.cpp',
    'Java': '.java',
    'Python': '.py',
    'JavaScript': '.js',
    'Go': '.go',
}

PROBLEM_INFO_PATTERN = re.compile(r'//\s*leetcode\s+(.+?)\s+(\d+)\s+(\w+)\s+challenge')
PROBLEM_URL_PATTERN = re.compile(r'//\s*(https://leetcode\.com/problems/[\w-]+/?)')

def parse_solution_files():
    entries = []
    for root, dirs, files in os.walk(SOLUTIONS_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            language = None
            for lang, lang_ext in LANG_EXTENSIONS.items():
                if ext == lang_ext:
                    language = lang
                    break
            if not language:
                continue  

            print(f"Processing file: {file_path}")
            with open(file_path, 'r') as f:
                lines = f.readlines()
                if len(lines) < 2:
                    print(f"Skipping {file_path}: not enough lines for comments")
                    continue  
                info_match = PROBLEM_INFO_PATTERN.match(lines[0].strip())
                url_match = PROBLEM_URL_PATTERN.match(lines[1].strip())
                if info_match and url_match:
                    title = info_match.group(1).strip()
                    problem_number = int(info_match.group(2))
                    difficulty = info_match.group(3).capitalize()
                    url = url_match.group(1)
                    relative_path = os.path.relpath(file_path, SOLUTIONS_DIR)
                    print(f"Matched: {problem_number}, {title}, {difficulty}, {relative_path}")
                    entries.append({
                        'number': problem_number,
                        'title': title,
                        'url': url,
                        'solution_path': relative_path.replace('\\', '/'),
                        'language': language,
                        'difficulty': difficulty
                    })
                else:
                    print(f"No match for {file_path}: info_match={info_match}, url_match={url_match}")
    return entries

def generate_readme(entries):
    """Generates README.md content from entries."""
    if not entries:
        print("No entries found. README will be empty.")
    entries.sort(key=lambda x: x['number'])
    readme_lines = [
        '# LeetCode Solutions',
        '',
        'This repository contains my solutions to LeetCode problems.',
        '',
        '| # | Title | Solution | Difficulty |',
        '|---| ----- | -------- | ---------- |'
    ]
    for entry in entries:
        line = f"|{entry['number']}|[{entry['title']}]({entry['url']})|[{entry['language']}]({entry['solution_path']})|{entry['difficulty']}|"
        readme_lines.append(line)
    return '\n'.join(readme_lines)

if __name__ == "__main__":
    entries = parse_solution_files()
    readme_content = generate_readme(entries)
    with open('README.md', 'w') as f:
        f.write(readme_content)
    print("README.md has been updated successfully.")
