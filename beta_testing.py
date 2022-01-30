#https://www.albumartexchange.com/covers?q=&fltr=ALL&sort=SCORE&status=RDY&size=any&apply-filter=#
#https://www.thepythoncode.com/article/extracting-image-metadata-in-python
import bs4
from bs4 import *
from bs4 import BeautifulSoup as soup
import tqdm
from tqdm import tqdm
import requests
import os
import time
import icecream
from icecream import ic
# CREATE FOLDER
def folder_create(images,folder_name):
    try:
        folder_name = str(folder_name)
        # folder creation
        try:
            os.mkdir(folder_name)
        except Exception as e: # if there are problems then save with a 2 on it.
            os.mkdir(folder_name + "2")
    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        #folder_create(images) #! this recursion may not be necessary

    # image downloading start
    download_images(images)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images):

    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["view-details-link"]
                ic(image_link)

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                ic()
                try:
                    ic()
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    ic()
                    try:
                        ic()
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            ic()
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass
                            ic()

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                ic()
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

# MAIN FUNCTION START
def main():

    # go to the link and we will iterate multiple times with this same url...
    pages_total = 644664//36
    for page_num in tqdm(range(1,pages_total)):
        url = f'https://www.albumartexchange.com/covers?q=&fltr=ALL&sort=SCORE&status=RDY&size=any&apply-filter=&page={page_num}'
        ic(url)
        # content of URL
        r = requests.get(url)

        # Parse HTML Code
        soup = BeautifulSoup(r.text, 'html.parser')

        # find all images in URL
        images = soup.findAll('view-details-link')

        download_images(images)

        # Call folder create function
        folder_create(images,str(page_num))
        time.sleep(1)
        print(f'completed epoch {page_num}')


# CALL MAIN FUNCTION
main()
