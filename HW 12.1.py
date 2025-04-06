import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open("draft.html", "r", encoding="utf-8") as infile, \
         open(result_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            clean_line = re.sub(r'<[^>]*>', '', line)
            if clean_line.strip():
                outfile.write(clean_line)

delete_html_tags("draft.html", "new_file.txt")
