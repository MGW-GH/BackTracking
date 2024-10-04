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
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)


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

## Testing 
- For detailed testing please refer to the [TESTING.md](TESTING.md) file.

## Deployment

This section describes the process we went through to deploy the project to GitHub.

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://mgw-gh.github.io/Hackathon2MW/


## Credits 

This section will reference any code used from other repositories as well citation for all images and text taken from other websites. 

### Content 

- parts of the html, css and javascript code for the canvas and game functionality were taken from YouTube (https://www.youtube.com/watch?v=baBq5GAL0_U)
- Parts of the html, css and javascript code for the operator buttons was taken from Code Institute GitHub repo (https://github.com/Code-Institute-Org/love-maths)
- Code implemented to problem solve responsivesness taken from chatGPT (https://chatgpt.com/)
- The text font used was from Google fonts (https://fonts.google.com/)

### Media

- The icon used for the favicon was taken from favicon (https://favicon.io/) 
- The icon used for the S in the header was taken from fontawesome (https://fontawesome.com/)
- Wireframe was created using Balsamiq (https://balsamiq.com/)

### Acknowledgements