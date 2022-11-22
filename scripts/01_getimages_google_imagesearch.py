import os
import requests
from bs4 import BeautifulSoup
import tqdm
from tqdm import tqdm
import time

google_image = (
    "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"
)
wikipedia_image = ""
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}


def main():
    """
    main function to run the script
    """
    totals = 0
    iterations = 0  # counts so that we keep the engine from smoking
    data = input("What are you looking for? ")
    # folder_subname = input('name for your subfolder:')
    from_year = int(input("from what year at the earliest? "))
    to_year = int(input("to what year at the latest? "))
    n_images = int(input("How many images do you want? (80 is limit per page) "))
    aspect_two = input("what MUST be included in the search?")
    aspect_three = input("what would you like to leave out of the search? ")

    dataline = (
        data
        + ' "in the year '
        + " (years go here) "
        + '"'
        + f'" {aspect_two} "'
        + f"-{aspect_three}"
    )
    print(
        f"retrieving {to_year-from_year} years worth of photos related to {data}\ndataline:{dataline}\nthis is {(to_year-from_year)*n_images} images in {to_year-from_year} folders.\n"
    )
    for this_year in tqdm(range(int(from_year), int(to_year))):
        # update folder info
        print("google extraction for the year...")
        saved_folder = f"../images/{this_year}"
        if not os.path.exists(saved_folder):
            os.mkdir(saved_folder)
        iterations, totals = download_images(
            data,
            this_year,
            n_images,
            iterations,
            saved_folder,
            aspect_two,
            aspect_three,
            totals,
        )
        # wikipedia extraction for the year as well


def download_wiki_images(this_year, saved_folder, iterations, n_images):
    """
    download_wiki_images

    Parameters

    :param this_year: year to search for
    :type this_year: int
    :param saved_folder: folder to save images to
    :type saved_folder: str
    :param iterations: number of iterations to keep track of
    :type iterations: int
    :return: iterations
    :rtype: int
    :param n_images: number of images to download
    :type n_images: int
    """
    aspect_one = this_year

    iterations = iterations + 1
    if iterations % 20 == 0:
        time.sleep(15)

    wikipedia_image = (
        f"https://commons.wikimedia.org/wiki/Category:{str(this_year)}_photographs"
    )
    print("\n", wikipedia_image)
    response = requests.get(wikipedia_image, headers=user_agent)
    # print(response)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    results = soup.findAll("div", {"class": "gallerytext"})

    count = 1
    links = []
    for result in results:
        try:
            link = result["data-src"]
            links.append(link)
            count += 1
            if count > n_images:
                break

        except KeyError:
            continue
    # totals = totals + len(links)
    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + "/" + data + str(i + 1) + ".jpg"

        with open(image_name, "wb") as fh:
            fh.write(response.content)
    # print(f'Running total of collected images:{totals}')
    return iterations


def download_images(
    data,
    this_year,
    n_images,
    iterations,
    saved_folder,
    aspect_two,
    aspect_three,
    totals,
):
    """
    download_images searches google for images of the data string and saves them to the saved_folder

    Parameters

    :param data: string of what you are looking for
    :type data: str
    :param this_year: year to search for
    :type this_year: int
    :param n_images: number of images to download
    :type n_images: int
    :param iterations: number of iterations to keep track of
    :type iterations: int
    :param saved_folder: folder to save images to
    :type saved_folder: str
    :param aspect_two: string to include in search
    :type aspect_two: str
    :param aspect_three: string to exclude from search
    :type aspect_three: str
    :param totals: total number of images downloaded
    :type totals: int
    :return: iterations, totals
    :rtype: int, int
    """
    aspect_one = this_year
    apsect_one = int(aspect_one)
    if aspect_three != "":
        data = (
            '"'
            + data
            + '" in "the year '
            + str(aspect_one)
            + '"'
            + f' "{aspect_two}"'
            + f"-{aspect_three}"
            + "imagesize:500x500"
        )
    else:
        data = (
            '"'
            + data
            + '" in "the year '
            + str(aspect_one)
            + '"'
            + f' "{aspect_two}" '
            + "imagesize:500x500"
        )
    print("\n", data)

    print("searching...")
    iterations = iterations + 1
    if iterations % 20 == 0:
        time.sleep(15)

    search_url = google_image + "q=" + data

    response = requests.get(search_url, headers=user_agent)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    results = soup.findAll("img", {"class": "rg_i Q4LuWd"})

    count = 1
    links = []
    for result in results:
        try:
            link = result["data-src"]
            links.append(link)
            count += 1
            if count > n_images:
                break

        except KeyError:
            continue
    totals = totals + len(links)
    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + "/" + data + str(i + 1) + ".jpg"

        with open(image_name, "wb") as fh:
            fh.write(response.content)
    print(f"Running total of collected images:{totals}")
    return iterations, totals

if __name__ == "__main__":
    main()
