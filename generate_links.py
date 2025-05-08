import os

BASE_URL = "https://thelime1.github.io/flutter-flow-assets/"
INDEX_FILE = "index.html"
ASSETS_FOLDER = "assets"

# Generate links for all assets in the assets folder
def generate_links():
    links = []
    for root, _, files in os.walk(ASSETS_FOLDER):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), ASSETS_FOLDER)
            links.append(f"<li><a href=\"{BASE_URL}{ASSETS_FOLDER}/{relative_path}\">{relative_path}</a></li>")
    return links

# Write the links to the index.html file
def write_index_file(links):
    with open(INDEX_FILE, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"en\">\n")
        f.write("<head>\n")
        f.write("    <meta charset=\"UTF-8\">\n")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        f.write("    <title>Asset Links</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("    <h1>Asset Links</h1>\n")
        f.write("    <ul>\n")
        f.write("\n".join(links))
        f.write("    </ul>\n")
        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == "__main__":
    links = generate_links()
    write_index_file(links)
