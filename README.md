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
  
  - The favicon depicts a snake and see on the windows tab. It makes the web page more attractive to users.
  
<img src="assets/images/tabsnake.png">

- __Operator Buttons__

  - The operator buttons allow the user to choose which type of sum they want and indicates the operator that's been chosen by highlighting.
  - Simple and effective design that draws the user into interacting with the page.

<img src="assets/images/operators.png">


### Future Features

- __Score erosion__

  - Include function to reduce score when eating the wrong answer.

- __Enemy Snake__
  - Create a function where eating the wrong answer generates a snake which increases in size as more wrong answers are eaten.
  - This will need to include functionality to change direction when the real snake changes direction and the new direction will be randomly generated.
  - Add a game over function which runs if there is some specific form of contact between the snakes.

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