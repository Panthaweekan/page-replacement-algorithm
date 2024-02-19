reference_string = input() # input
pages = reference_string.split()

duplicated_pages = {}

for page in range(10):
    page_str = str(page)
    count = pages.count(page_str)
    if count > 1:
        duplicated_pages[page_str] = count
print("reference string : " + reference_string)
print("Duplicated pages:")
for page, count in duplicated_pages.items():
    print("Page", page, "is duplicated", count, "times.")
