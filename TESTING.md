# Testing

TESTING file for [BackTracker](https://back-tracker-9bf98d85163a.herokuapp.com/) website.

Return to the [README.md](README.md).

## Contents  
  
- [Testing](#testing)
  - [Contents](#contents)
  - [Validation](#validation)
    - [HTML - W3C Validator](#html---w3c-validator)
    - [CSS - W3C Validator](#css---w3c-validator)
    - [JavaScript - JS Hint](#javascript---js-hint)
    - [Python - CI Python Linter](#python---ci-python-linter)
  - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)

## Validation

### HTML - W3C Validator
Due to the use of Django all of the html files contain some Jinja syntax and fail the validator if applied raw. However by right-clicking on the deployed Heroku site and inspecting page it was possible to extract just the html code to be passed through the W3C HTML validator.
<img src="static/images/home.png">
All HTML pages were validated and received a 'No errors or warnings to show' result as shown above for the home page. See following links for checks on remianing html docs:
- [login](static/images/sign_in.png)
- [feed](static/images/stamp_feed.png)
- [add stamp](static/images/add_stamp.png)
- [stamp detail](static/images/stamp_detail.png)
- [country search](static/images/country_search.png)
- [gallery](static/images/gallery.png)
- [logout](static/images/sign_out.png)

### CSS - W3C Validator
CSS was validated via the W3C Jigsaw CSS validator and returned no errors for my style.css file:
<img src="static/images/style.png">

### JavaScript - JS Hint
My ratings.js file passed through JS Hint without errors or warnings:
<img src="static/images/ratings.png">

### Python - CI Python Linter
I used CI Python Linter to check all Python code that I contributed to. Below is the validation run on my project urls file (back_tracker/urls.py) followed by links to all other .py file checks.
<img src="static/images/blog_urls.png">

__Back_Tracker project__ 
- [settings](static/images/B_T_settings.png)

__Home__
- [forms](static/images/home_forms.png)
- [models](static/images/home_models.png)
- [urls](static/images/home_urls.png)
- [views](static/images/home_views.png)

__Blog__
- [admin](static/images/blog_admin.png)
- [forms](static/images/blog_forms.png)
- [models](static/images/blog_models.png)
- [urls](static/images/blog_urls.png)
- [views](static/images/blog_views.png)

__Gallery__
- [urls](static/images/gallery_urls.png)
- [views](static/images/gallery_views.png)

__[Env](static/images/env.png)__

## Manual Testing


## Bugs