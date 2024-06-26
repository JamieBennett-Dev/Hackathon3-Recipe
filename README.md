# Welcome to Our Recipe Sharing Site Readme 

## Introduction

Our site makes it easy to find great recipes from other users, or post your own! You can see reviews and comments of each recipe so you can gage which ones you want to try. 

The site supports creating, editing, deleting of recipes, meaning it remains an up to date and dynamic envirnment. 

![Screenshot 2023-12-07 at 11 04 34](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e891dd76-414b-40aa-89f0-7e343ef8a5fa)


[Link to RecipMe website](https://recip-me-deee77afa86d.herokuapp.com/)


## User Stories

### Admin

**As an admin, I want to add, edit and delete users directly from the admin interface so that I can mange user access.**

**Acceptance Criteria:**
* Admin can access the user creation form in the admin panel.
* Admin can fill out user details and save the new user.
* Admin can access the list of users in the admin panel.
* Admin can edit user details and save the changes.
* Admin can delete a user from the user list in the admin panel.
* Admin receives a confirmation prompt before deletion.

**As an admin, I want to add, edit and delete recipes directly from the admin interface so that I can manage content efficiently.**

**Acceptance Criteria:**
* Admin can access the recipe creation form in the admin panel.
* Admin can fill out all necessary fields and save the new recipe.
* Admin can access the list of recipes in the admin panel.
* Admin can edit the details of any recipe and save the changes.
* Admin can delete a recipe from the recipe list in the admin panel.
* Admin receives a confirmation prompt before deletion.


### User

**As a user, I want to see the preparation time for a recipe so that I can plan my cooking accordingly.**

**Acceptance Criteria:**
* Recipe creator can specify preparation and cooking time.
* Total time is displayed on the recipe details page.


**As a user, I want to see the difficulty level of a recipe (e.g., easy, medium, hard) so that I can choose recipes that match my cooking skills.**

**Acceptance Criteria**
*Recipe creator can assign a difficulty level to a recipe.
*Difficulty level is displayed on the recipe details page.


**As a logged-in user, I want to mark recipes as favorites so that I can easily find them later.**

**Acceptance Criteria**
*User can add/remove recipes to/from their favorites list.
*User can view their favorite recipes in a separate section.


**As a user, I want to provide feedback on recipes so that I can share my cooking experience.**

**Acceptance Criteria**
*User can leave comments on recipe details pages.
*Comments are displayed below the recipe details.


**As a logged-in user, I want to edit my profile information so that I can keep my details up-to-date.**

**Acceptance Criteria**
*User can update their username, email, and password.
*User receives a confirmation message upon successful profile update.


**As a logged-in user, I want to view my profile details so that I can see my personal information and recipes.**

**Acceptance Criteria**
*User can view their username, email, and a list of their created recipes.


**As a user, I want to search for recipes by keyword so that I can find specific recipes quickly.**

**Acceptance Criteria**
*User can enter keywords in a search bar.
*User sees a list of recipes matching the search criteria.


**As a user, I want to browse through a list of recipes so that I can discover new dishes to try.**

**Acceptance Criteria**
*User can see a paginated list of recipes with titles and thumbnails.
*User can click on a recipe to view its details


**As a logged-in user, I want to delete a recipe so that I can remove unwanted or outdated recipes.**

**Acceptance Criteria**
*User can delete a recipe from the recipe details page or a list of recipes.
*User receives a confirmation prompt before deletion.
*Recipe is removed from the database upon confirmation.


**As a logged-in user, I want to edit an existing recipe so that I can update its details.**

**Acceptance Criteria**
*User can access an edit form pre-filled with the current recipe details.
*User can update any of the recipe details and save the changes.


**As a user, I want to view the details of a recipe so that I can follow it to cook.**

**Acceptance Criteria**
*User can click on a recipe title to view its details.
*Recipe details include title, ingredients, steps, and an image if available.


**As a logged-in user, I want to create a new recipe so that I can share my cooking creations.**

**Acceptance Criteria**
*User can fill out a form with recipe details including title, ingredients, steps, and an optional image.
*User receives a confirmation message upon successful recipe creation.

**As a logged-in user, I want to log out of my account so that I can ensure my account security.**

**Acceptance Criteria**
*User can log out from any page.
*User is redirected to the homepage or login page upon logout.


**As a registered user, I want to log in to my account so that I can access my personal recipe collection.**

**Acceptance Criteria**
*User can log in with their username/email and password.
*User is redirected to their dashboard upon successful login.


**As a new user, I want to register an account so that I can create and manage my recipes.**
*User can sign up by providing a username, email, and password.
*User receives a confirmation email after successful registration.


## Workflow
### Agile Methodology
An Agile approach was taken in the production of this site. The methodology and philosophy of Agile guided a step by step creation of the site. Collaboration, well-structure designation of tasks, and good time management allowed us to complete the minimum viable product well within the deadline, as well as some additional features.

Our workflow followed this diagram (created by [rachbry](https://github.com/rachbry))

![Workflow Diagram](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/c5ed706d-1b01-4a22-8e40-6e4ff5511e61)

I used Github projects to convert my user stories into actionable tasks.  The acceptance criteria was very helpful to ensure all necessary tasks were completed.

![Image of Kanban Board](https://github.com/JamieBennett-Dev/[path to image of kanban board]



### Models
In RecipMe I used the Django AllAuth User Model and created a custom Recipe Model.  This included the following fields:

|      Name            |     Type                   |     Key  |
|----------------------|----------------------------|----------|
|      user            |     User Model             |     FK   |
|      title           |     CharField              |          |
|      slug            |     CharField              |          |
|      description     |     CharField              |          |
|      instructions    |     RichTextField          |          |
|      ingredients     |     RichTextField          |          |
|      freezable       |     boolean                |          | 
|      serving         |     CharField              |          |
|      image           |     ResizedImageField      |          |
|      image_alt       |     CharField              |          | 
|      Recipe_type     |     CharField  dropdown    |          |
|      Cooking_method  |     CharField  dropdown    |          |
|      posted_date     |     DateTimeField          |          |

I also added a many to many field called is_favourite to enable the favourite functionality.


## Design
### Wireframes and Features
The site is fully responsive and accessible on mobile, tablet and desktop devices.


**All Users:**
- Are able to view admin added recipes
- Are able to use the search functionality

**Logged In Users:**
- Can add recipes
- Can view, edit and delete their own recipes


**The Full Recipe Page:**
Contains all the relevent information for each recipe.  Design will ensure all ingredients and instructions are available on one screen for desktop and tablet.

![Screenshot 2023-12-07 at 13 36 14](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/3e8edc07-582b-41de-8cd6-6ce59475f3be)



**Add / Edit Recipe Page:**
Front End CRUD is available to add / edit recipes for logged in users.  The form includes category dropdowns and the ability to upload an image.

![Screenshot 2023-12-07 at 13 42 11](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/42943578-41c6-4061-b0e4-e9debaa239bd)


## Design Choices (change this when done)
###  Colours

I used [coolors.co] (https://coolors.co/palette/253439-ff5757-545454-ffbd59-f5f4f3) to generate my colour palette:

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/027c781a-346b-4ed8-93ed-9a42815c0f0f)

I aimed for a clean and simple website design that keeps the focus on the content. Opting for a vibrant colour scheme, I wanted to strike a balance between minimalism and boldness. The light off-white background (#f5f4f3) keeps things simple and clean, while introducing splashes of colour add a touch of visual interest that contrasts against the neutral backdrop. This combination creates a modern look without being too over the top.

Coral and yellow form a complementary pairing, and their warmth complemented by cool grey tones, ensures a visually cohesive and balanced palette.  The neutral colours help maintain an overall sense of harmony.

The result is a carefully chosen color palette that enhances the design without overwhelming it, adding sophistication and vibrancy.





## The site (edit this when done)

### Homepage

![Screenshot 2023-12-08 at 12 03 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/7abfbfb0-59bd-4442-b208-c1ee634a79dd)


### Sign In

![Screenshot 2023-12-08 at 12 09 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ffcb1ee2-5192-4d04-8a76-0dd7d61798ea)


### Add / Edit Pages

![Screenshot 2023-12-08 at 12 20 19](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62545a43-e46b-41b8-95e3-9edece069e07)


### RecipMe, Favourites

![Screenshot 2023-12-08 at 12 30 57](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/af2e5cb7-a489-4239-96bb-fbb5e76963b4)


![Screenshot 2023-12-08 at 12 35 16](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6fdb2dd1-56c0-4c7f-9388-f22b00e5368b)


###  Personalised Home Page 

![Screenshot 2023-12-08 at 12 40 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/2049f4cc-a85e-4ed7-9010-0197f17aac23)


### Full Recipe Page

![Screenshot 2023-12-08 at 12 46 15](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/9e79d26c-09d0-43ac-96e4-cc291166ec50)




### Future Features
* While user login is implemented, we did not have time to create user profiles. These would have included the ability to add a display picture and add basic user details.
* Favourites: we wanted the user to be able to favourite, and thereby save, recipes they like. We unfortunately ran out of time.
* share: the ability to share recipes either via email or social media would be a great addition that could be added in the future.


## Testing (Edit when done)

Results of manual testing:
[Testing](testing.md)

## Responsiveness
This website has been tested and is fully responsive on Desktop, Mac book, Ipad and mobile devices.
                                

## Browser Compatibility (edit when done)

The website has been tested and is being displayed as expected on Safari, Google Chrome and Firefox as well as on android and apple devices.

| Screenshots                                                                                                                                      | Ipad and Iphone SE                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![53d76d73-ebe8-46ee-9860-8137adc34f04](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/18cdc571-d3ce-4f13-972f-9b7e98cd6936) | ![ipad](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6124121e-03e9-4085-9200-746d3aa4812c)     |
| ![IMG_0144](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62afc582-cedd-4e03-802c-9afeeb5f1c8d)                             | ![IMG_0143](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ae16c7b3-08dc-4077-8fe7-b314cd527072) |

## Bugs (edit when done)


## Technologies Used
- CSS
- Django
- HTML
- Bootstrap
- Python
- Postgres Database

- GitPod development environment used
- GitHub used for version control and code hosting
- GitHub Projects used for Agile Methodology


# Credits (edit when done)

- ChatGPT was used for troubleshooting, bug fixing and content generating.  Also used to create my persona.
- Thanks to the other members of the Bootcamp for their technical and moral support
- Recipes used were from the bbc good food website
- Hero on image home page
- Fontawesome was used for icons
- Google fonts was used
- Wireframes created in Balsamiq
- Logo and flow chart created in Canva
