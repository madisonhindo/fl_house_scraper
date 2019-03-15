# fl_house_scraper
## What I did
I created a scraper to get the name, district, political party and contact information for each member of the Florida House of Representatives. The link to the list of current representatives can be found [here](https://www.myfloridahouse.gov/Sections/Representatives/representatives.aspx).

## How I did it
I used multiple functions to do this. The **get_rep_profiles()** function was used to grab links to the profile of every representative and store them into a list.

The **get_contact_link()** function was used to cycle through the list created by the get_rep_profiles() function and find the link to each representative’s contact page. The link to their contact pages were on each profile page.

The **get_names_and_district()** function scraped the name, district, and party affiliation from the profile page of each representative.

The **get_contact_info()** function scraped the phone number and address for each representative’s office in Tallahassee. 

The **clean()** function was used to solve a problem with the HTML formatting of the site. strip() was not enough to clean the HTML because there was a large amount of whitespace in the middle of the elements I scraped. 

## Problems I encountered
After I scraped everything I needed, I ran into the problem of figuring out how to display the information in a logical way. After running all of the functions, I had a list that included each representative’s name, district and party and a separate list of each representative’s contact information. To fix this, I created a variable that combined all of this information for each person based on their index in the two lists. A new list called together_list was created to hold the correctly formatted information for each representative. Each time a for loop ran, a new representative’s information was added to the new list.
