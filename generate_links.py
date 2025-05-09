import os
import time

BASE_URL = "https://sou9-nft.github.io/flutter-flow-assets/"
INDEX_FILE = "index.html"
README_FILE = "redme.md"  # Note the filename as seen in the workspace
ASSETS_FOLDER = "assets"

# Generate links for all assets in the assets folder


def generate_links():
    links = []
    for root, _, files in os.walk(ASSETS_FOLDER):
        for file in files:
            relative_path = os.path.relpath(
                os.path.join(root, file), ASSETS_FOLDER)
            links.append(
                f"<li><a href=\"{BASE_URL}{ASSETS_FOLDER}/{relative_path}\">{relative_path}</a></li>")
    return links

# Write the links to the index.html file


def write_index_file(links):
    timestamp = int(time.time())  # Generate a timestamp
    with open(INDEX_FILE, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"en\">\n")
        f.write("<head>\n")
        f.write("    <meta charset=\"UTF-8\">\n")
        f.write(
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        f.write(
            "    <meta http-equiv=\"Cache-Control\" content=\"no-cache, no-store, must-revalidate\">\n")
        f.write("    <meta http-equiv=\"Pragma\" content=\"no-cache\">\n")
        f.write("    <meta http-equiv=\"Expires\" content=\"0\">\n")
        f.write(f"    <meta name=\"version\" content=\"{timestamp}\">\n")
        f.write(f"    <title>Asset Links v?={timestamp}</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("    <h1>Asset Links</h1>\n")
        f.write("    <ul>\n")
        f.write("\n".join(links))
        f.write("    </ul>\n")
        f.write("</body>\n")
        f.write("</html>\n")

# Update the README.md file with the index link as a title


def update_readme_file():
    timestamp = int(time.time())
    index_url = f"{BASE_URL}{INDEX_FILE}?v={timestamp}"

    with open(README_FILE, "w") as f:
        f.write(f"# [Asset Links]({index_url})\n\n")
        f.write("This repository contains assets used for Flutter Flow projects.\n")
        f.write(
            f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n\n")
        f.write("## Available Assets\n\n")
        f.write(
            f"View all available assets at the [Asset Links Index]({index_url}).\n")

# Clear the list section in the index.html file


def clear_index_file():
    timestamp = int(time.time())  # Generate a timestamp
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang=\"en\">\n")
            f.write("<head>\n")
            f.write("    <meta charset=\"UTF-8\">\n")
            f.write(
                "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
            f.write(
                "    <meta http-equiv=\"Cache-Control\" content=\"no-cache, no-store, must-revalidate\">\n")
            f.write("    <meta http-equiv=\"Pragma\" content=\"no-cache\">\n")
            f.write("    <meta http-equiv=\"Expires\" content=\"0\">\n")
            f.write(f"    <meta name=\"version\" content=\"{timestamp}\">\n")
            f.write(f"    <title>Asset Links v?={timestamp}</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("    <h1>Asset Links</h1>\n")
            f.write("    <ul>\n")
            f.write("    </ul>\n")
            f.write("</body>\n")
            f.write("</html>\n")


if __name__ == "__main__":
    clear_index_file()
    links = generate_links()
    write_index_file(links)
    update_readme_file()  # Added the call to update the README file
