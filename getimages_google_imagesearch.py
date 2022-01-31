import os
import requests
from bs4 import BeautifulSoup
import tqdm
from tqdm import tqdm
import time
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"
wikipedia_image = ""
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def main():

    totals = 0
    iterations = 0 # counts so that we keep the engine from smoking
    data = input('What are you looking for? ')
    #folder_subname = input('name for your subfolder:')
    from_year = int(input('from what year at the earliest? '))
    to_year = int(input('to what year at the latest? '))
    n_images = int(input('How many images do you want? (80 is limit per page) '))
    aspect_two = input('what MUST be included in the search?')
    aspect_three = input('what would you like to leave out of the search? ')

    dataline = data + ' "in the year ' + " (years go here) " + '"' + f'" {aspect_two} "' + f'-{aspect_three}'
    print(f'retrieving {to_year-from_year} years worth of photos related to {data}\ndataline:{dataline}\nthis is {(to_year-from_year)*n_images} images in {to_year-from_year} folders.\n')
    for this_year in tqdm(range(int(from_year),int(to_year))):
        #update folder info
        print("google extraction for the year...")
        saved_folder = f'images/{this_year}'
        if not os.path.exists(saved_folder):
            os.mkdir(saved_folder)
        iterations,totals = download_images(data,this_year,n_images,iterations,saved_folder,aspect_two,aspect_three,totals)

        #wiki
        '''
        print("wikipedia extraction for the year...")
        saved_folder = f'Wiki_images/{this_year}'
        if not os.path.exists(saved_folder):
            os.mkdir(saved_folder)
        try:
            iterations = download_wiki_images(this_year,saved_folder,iterations)
        except Exception as e:
            print("error with wikipedia data pull")
            print(e)
        '''

def download_wiki_images(this_year,saved_folder,iterations):

    aspect_one = this_year

    iterations = iterations + 1
    if iterations % 20 == 0:
        time.sleep(15)

    wikipedia_image =f'https://commons.wikimedia.org/wiki/Category:{str(this_year)}_photographs'
    print('\n',wikipedia_image)
    response = requests.get(wikipedia_image, headers=user_agent)
    #print(response)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('div', {'class': 'gallerytext'})

    count = 1
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue
    #totals = totals + len(links)
    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)
    #print(f'Running total of collected images:{totals}')
    return iterations

def download_images(data,this_year,n_images,iterations,saved_folder,aspect_two,aspect_three,totals):
    aspect_one = this_year
    apsect_one = int(aspect_one)
    if aspect_three != "":
        data = '"'+data + '" in "the year ' + str(aspect_one) + '"' + f' "{aspect_two}"' + f'-{aspect_three}' + "imagesize:500x500"
    else:
        data = '"'+data + '" in "the year ' + str(aspect_one) + '"' + f' "{aspect_two}" ' + "imagesize:500x500"
    print('\n',data)

    print('searching...')
    iterations = iterations + 1
    if iterations % 20 == 0:
        time.sleep(15)

    search_url = google_image + 'q=' + data

    response = requests.get(search_url, headers=user_agent)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    count = 1
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue
    totals = totals + len(links)
    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)
    print(f'Running total of collected images:{totals}')
    return iterations,totals



'''
https://www.loc.gov/item/90707101/
https://www.loc.gov/item/90715981/
https://www.loc.gov/item/93510427/
https://www.loc.gov/item/98508522/
https://www.loc.gov/item/98508572/
https://www.loc.gov/item/98508588/
https://www.loc.gov/item/98508610/
https://www.loc.gov/item/98508631/
https://www.loc.gov/item/98508851/



# general


https://www.loc.gov/item/90707101/
https://www.loc.gov/item/90715977/
https://www.loc.gov/item/90715980/
https://www.loc.gov/item/90715981/
https://www.loc.gov/item/90716009/
https://www.loc.gov/item/90716011/
https://www.loc.gov/item/90716012/
https://www.loc.gov/item/92519204/
https://www.loc.gov/item/93500718/
https://www.loc.gov/item/93500720/
https://www.loc.gov/item/93504429/
https://www.loc.gov/item/93510427/
https://www.loc.gov/item/93510496/
https://www.loc.gov/item/93511486/
https://www.loc.gov/item/94513615/
https://www.loc.gov/item/94513619/
https://www.loc.gov/item/94514736/
https://www.loc.gov/item/96505328/
https://www.loc.gov/item/96505331/
https://www.loc.gov/item/96505333/
https://www.loc.gov/item/96505338/
https://www.loc.gov/item/96511984/
https://www.loc.gov/item/96512992/
https://www.loc.gov/item/96512994/
https://www.loc.gov/item/98507609/
https://www.loc.gov/item/98508477/
https://www.loc.gov/item/98508490/
https://www.loc.gov/item/98508503/
https://www.loc.gov/item/98508509/
https://www.loc.gov/item/98508512/
https://www.loc.gov/item/98508514/
https://www.loc.gov/item/98508515/
https://www.loc.gov/item/98508522/
https://www.loc.gov/item/98508572/
https://www.loc.gov/item/98508574/
https://www.loc.gov/item/98508577/
https://www.loc.gov/item/98508578/
https://www.loc.gov/item/98508581/
https://www.loc.gov/item/98508588/
https://www.loc.gov/item/98508605/
https://www.loc.gov/item/98508610/
https://www.loc.gov/item/98508631/
https://www.loc.gov/item/98508658/
https://www.loc.gov/item/98508851/
https://www.loc.gov/item/98509689/
https://www.loc.gov/item/98509691/
https://www.loc.gov/item/98509722/
https://www.loc.gov/item/98515951/
https://www.loc.gov/item/98515954/
https://www.loc.gov/item/98515962/




'''



if __name__ == "__main__":
    main()
