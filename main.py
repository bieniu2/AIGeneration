import network_utils
import re

API_KEY: str = "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"
ARTICLE_URL: str = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"
TEXT_FILE_NAME: str = "downloaded_article.txt"
ARTICLE_FILE_NAME: str = "artykul.html"


def main():
    content: str = network_utils.download_content(ARTICLE_URL, TEXT_FILE_NAME)
    if content is None:
        print("Failed to download article")
        quit(1)
    response: str = network_utils.send_query_to_openai(API_KEY, "Generate a HTML content that can be placed into "
                                                                "<body> tags (but don't generate those tags),"
                                                                "NO CSS, NO JAVASCRIPT CODE AND NO "
                                                                "<html>/<head>/<body> TAGS"
                                                                "AT ALL, ONLY PURE HTML!!! "
                                                                "Figure out places where to add images using <img> "
                                                                "placeholder with src for image source (add the "
                                                                "source name - which must end with '.png' - to tag, "
                                                                "don't leave"
                                                                "it empty) and alt for"
                                                                "description (add description as well, don't leave "
                                                                "empty)"
                                                                "Article is based on this text: " + content)
    print(response)
    with open(ARTICLE_FILE_NAME, 'w', encoding='utf-8') as file:
        file.write(response)

    regex = re.compile("<img src=\\\"([^\"]*)\" alt=\"([^\"]*)\">")
    matches = regex.finditer(response)

    for match in matches:
        image_name: str = match.group(1)
        image_description: str = match.group(2)
        print(f"Image name will be {image_name} and {image_description}")
        image_url = network_utils.send_image_query_to_openai(API_KEY,
                                                             "Generate image basing on description: " + image_description)
        if image_url == "":
            print(f"Error generating image for {image_description}")
        else:
            print(f"Downloading image from {image_url}")
            network_utils.download_image(image_url, image_name)


if __name__ == "__main__":
    main()
