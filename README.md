# BackTracker
### Intro

BackTracker is a social media website designed for users to share images, view other user's images and leave ratings. It's a multi page site that enables custom views to give users the most complete experience. BackTracker is a full-stack project utilising Django and Bootstrap frameworks, emphasising database manipulation and CRUD functionality. The project was developed as part of the Code Institute's Full-Stack Developer Bootcamp.


<img src="assets/images/mathsnakescreenshot.png">

Live link: [BackTracker](https://back-tracker-9bf98d85163a.herokuapp.com/)

Admin link - superuser login required: [BackTracker Admin](https://back-tracker-9bf98d85163a.herokuapp.com/admin/)

### Contents

- [BackTracker](#backtracker)
    - [Intro](#intro)
    - [Contents](#contents)
  - [User Experience](#user-experience)
    - [Approach](#approach)
  - [Project Planning](#project-planning)
    - [Agile Project Management](#agile-project-management)
    - [User Stories](#user-stories)
    - [Wireframe](#wireframe)
    - [Userflow](#userflow)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Features](#features)
    - [User-Type View](#user-type-view)
    - [Existing Features](#existing-features)
    - [CRUD Functionality](#crud-functionality)
    - [Future Features](#future-features)
  - [Technologies and Languages](#technologies-and-languages)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)


## User Experience

### Approach

  After a few idea trade-offs I settled on the idea of an image blogging website focusing on travel, that wouldshould allow users varied ways in which to filter and view images posted by themselves and others. The colour theme should be conisistent throughout as well as the navigation and layout.

## Project Planning

### Agile Project Management
BackTracker was planned using the agile planning method allowing the project to be broken down into manageable chunks - see [project board in GitHub](<https://github.com/users/MGW-GH/projects/4>). Employing MoSCoW priotisation meant assigning labels to each chunk based on its necessity - 'Must Have, Should Have, Could Have' and completed in that order.

### User Stories

__Must Haves__
- Login, Logout - As a registered user I can easily login and out for security
- Navigation - As a site user I can navigate between pages to access all content
- Manage Posts - As a site admin I can create, read, update and delete posts so that I can manage the site content
- Account Registration - As a site user I can register an account so that I can comment on a post
- View Posts - As a site user I can view a paginated list of posts so that I can select which post I want to view
- Open a Post - As a site user I can click on a post so that I can read all the detail
- Change Posts - As a site user I can edit or delete my own posts or ratings so that I can make desired updates

__Should Haves__
-  Location - As a site user I can update my location so that users can see my location
-  Rate Posts - As a site user I can like posts so that I can interact with other users' posts
  
__Could Haves__
- Gallery - As a site user I can view a gallery so that I can see specific users' pictures
- User Profile - As a site user I can click on my user profile so that I can see my personal view

### Wireframe

### Userflow

### Entity Relationship Diagram

## Features 

### User-Type View
For the best user experience whilst encouraging registering to the app most of the website has been developed to allow viewing reagrdless of whether the user is registered or not. 
- Registered User - Can view all of the site including their personal profile and gallery and add, edit and delete posts and ratings.
- Unregistered User - Can view most of the site such as home page, feed and individual posts but cannot add, edit and delete posts and ratings nor see a profile or gallery view.
  
### Existing Features

- __Favicon__
  
  - The favicon depicts a rucksack and can be seen on the window's tab. It makes the web page more attractive to users and relates to the site purpose and content.
  
<img src="assets/images/tabsnake.png">

- __Header & Navbar__

  - The navbar runs a consistent theme throughout the pages with circular navigation to all pages for the best user experience.
  - The navbar includes a specially designed logo as well as responsive bootstrap classes to turn the links into a burger toggle when screen size is reduced.

<img src="assets/images/operators.png">

- __Home Page__
  
  - The home page is a clean design with one background image covering the space between header and footer, relevant to the site content.
  - The search bar in the centre allows users to search for a specific country by clicking or typing.

- __Country Search__
  
  - Once a country is selected and searched a new page will appear with a continuing header and footer theme and content showing all stamp's tagged with the country searched.
  - This feature gives users a chance to see some of site content and functionality without being registered or signed in.

- __Stamp Feed__
  
  - The main feed for the website displays all stamps across a paginated design with a maximum of 8 staps on a single page oredered by date posted.
  - This page is successfully responsive to changes in device size and continues to employ the colour scheme from the headr and footer for best UX.

- __Stamp Detail__
  
  - When the title of a stamp is clicked on from the feed it wil direct the user to stamp detail page consisting solely of the stamp clicked on along with the stamp details such as country and location and date posted.
  - This view gives a clearer look at the image imporivng the depth of experience for the user.
  - This page also includes the ability to edit and delete stamps or ratings if the user viewing created them.
  
- __Ratings__
  
  - On the stamp detail page tis section allows users to leave a rating for the stamp being viewed as long as they did not post it and they haven't left a rating on the stamp previously.
  - This adds a personalised touch to engage the user to be a part of the website even if they haven't posted anything themselves.
  - The rating is applied as a percentage score and must take a value between 0 and 100.

- __Add Stamp__
  
  - This feature appears as a plus sign in a circle in the navbar and clicking it directs the user to from page where they can upload and enter details for a new stamp to be posted. Once posted the user is redirected back to the feed.
  - This is the only page that does breaks the header and footer styling but the colour theme is applied to the background.
  - This is hugely important and its functionality allows for content to be added to the website which is one of, if not the, main requirement.

- __Gallery__
  
  - The link for the gallery should only be visible in navbar to logged in users so they can view a page of all of their own stamp posts.
  - This is another feature that gives a user tailored view for greater experience.

- __Register__
  
  - Users are required to enter a username and password to create an account with the option of an email address and password criteria.
  - It also has a link to the login page if the user already has an account.

- __Login & Logout__

  - The login page enable a reigstered user to sign in using their username and password and directed to the home page.
  - The logout page is accessed by clicking the link in the navbar. The page checks the user is they're sure they want to log out and will only perform the logout when the button is selected.

- __Admin Panel__
  - Through Django's built-in Administration Panel, the Admin has full access over the data submitted to the website by registered users. To access the Admin panel the Admin user adds '/admin/' to the end of the URL.
  - It includes night and day modes as well as a custom filter within the panel to search stamps by country.

### CRUD Functionality

The CRUD functionality is in action in multiple places across the site for both admin and users. 
- Within the admin site stamps, ratings and users can be created, edited and deleted.
- Registered users can create, edit and delete stamps from the main site given certain criteria.
- Registered users can create, edit and delete ratings for stamps from the stamp detail page given certain criteria.

### Future Features

- __User Profile__

  - Include a page for a logged in user to show their profile with certain images and data from their stamps and ratings as well as extra info such as a bio and alias.

- __Tracker__
  - Based on the users posted stamps this will show a diagram or map highlighting countries visited and current location/status.

## Technologies and Languages

- HTML
- CSS
- JavaScript
- Python
- Git
- GitHub
- Django
- Cloudinary
- PostgreSQL
- Heroku

__Libraries & Frameworks__
- asgiref==3.8.1
- bootstrap==5.0.1
- cloudinary==1.41.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.16
- django-allauth==0.57.2
- django-countries==7.6.1
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- pillow==10.4.0
- psycopg==3.2.2
- PyJWT==2.9.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- urllib3==1.26.20
- whitenoise==5.3.0

__Tools__
- Lucidchart
- Balsamiq
- Brandcrowd
- GitHub Projects
- Gencraft

## Testing 
- For detailed testing please refer to the [TESTING.md](TESTING.md) file.

## Deployment

__Connecting to GitHub__

To begin the project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the Code (if this is your IDE of choice) button to generate a new workspace.

__Django Project Setup__

1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject back_tracker .```
4. Create a new app eg. ```python3 mangage.py startapp blog```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'blog',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLpostgreSQLlink>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn back_tracker.wsgi```
12. Make the necessary migrations again.

__Cloudinary API__

Cloudinary provides a cloud hosting solution for media storage. All user uploaded images and the home page image in the BackTrackers project are hosted here and converted and served as .webp.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATIC_URL = 'static/'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

__PostgreSQL Database__

A new database instance can be created using the [Code Institute Database Maker](https://dbs.ci-dbs.net/) for your project.

- Input your email address and "submit".
- You will have received an email with your new PostgreSQL database URL.
- Copy the URL.
- In your IDE terminal: pip3 install dj-database-url~=0.5 psycopg and freeze requirements.
- From your email, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


__Heroku Deployment__

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   - **PORT**:**8000**
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.


## Credits 

This section will reference any code used from other repositories as well citation for all images and text taken from other websites. 

### Content 

- Parts of the html, css, javascript and python code were taken from this [Code Institute GitHub repo](https://github.com/Code-Institute-Solutions/blog/tree/main)
- Code implemented to problem solve bugs taken from [ChatGPT](https://chatgpt.com/)
- The text font used was from [Google fonts](https://fonts.google.com/)

### Media

- The icon used for the favicon was taken from [Favicon](https://favicon.io/) 
- The icon used for the add stamp button in the navbar as well as the social media icons in the footer were taken from [Fontawesome](https://fontawesome.com/)
- The logo in the navbar was made using [Brandcrowd](https://www.brandcrowd.com/)
- The background image ioon the home page was created using [Gencraft](https://gencraft.com/)
- Images served on the feed are either taken from individuals who've contributed to the site or [Google Images](https://images.google.co.uk/)