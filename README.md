# SVERIGE LOPPIS

# Table of Contents:
* [User Experience (UX)](#ux)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Structure](#structure)
        * [Wireframes](#wireframes)
        * [Databases](#databases)
* [UI](#ui)
    * [Color Palette](#color-palette)
    * [Font](#fonts)
* [Marketing](#marketing)
    * [Plan](#plan)
        * [Facebook](#facebook)
        * [Newsletter](#newsletter)
    * [SEO's](#seos)
* [Features](#features)
    * [Navbar](#navbar)
    * [Footer](#footer)
    * [Home Page](#home-page)
    * [About Page](#about-page)
    * [Loppis Page](#loppis-page)
    * [Loppis Details Page](#lopppis-details-page)
    * [Personalized Account Page](#personalised-account-page)
    * [Wishlist Page](#loppis-wishlist-page)
    * [Purchase/Advertise Function](#purchaseadvertise-function)
    * [Asking a question to Loppis Owner Function](#asking-a-question-to-loppis-owner-function)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

# UX
## Strategy
## User Stories
## Scope
## Structure
### Wireframes
### Databases

# UI
## Color Palette:
![Color palatte](media/loppis-color-palatte.png)
* Color palette is chosen with keeping in mind the target audience. As Sverige Loppis' main target is Sweden, Blue and Yellow was my first choice.
* Blue color has a psychological effect on trust, offical, calm; and yellow color psychologically gives a charming, friendly effect.
* To maintain the color contrast I chose to use a softer tones of blue and yellow. 
* I have used [Coolors](https://coolors.co/) to generate my color palette.

## Fonts
* To maintain simple UI, font chosen was Montserrat from [Google Fonts](https://fonts.google.com/specimen/Montserrat?query=mont#standard-styles).

# Marketing
## Plan:
### Facebook
### Newsletter
## SEO's

# Features:
## Navbar
## Footer
## Home Page
## About Page
## Loppis Page
## Lopppis Details Page
## Personalised Account Page
## Loppis Wishlist Page
## Purchase/Advertise Function
## Asking a question to Loppis owner Function

# Technologies Used

# Testing
*Unit Testing*, *Validator Testing*, and *Bugs* are documented [here](/TESTING.md).

# Deployment

# Credits
During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:

* [Stack Overflow](https://stackoverflow.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)
* [Django Project Documentation](https://www.djangoproject.com/)
* [Code Instiute](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=581817633089&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGgmnuTJCpzeJBqKg9fy2p-7NlU8NY95XaXmoPzBpuDdIekQWqUKxocaAso5EALw_wcB) course materials and Django Boutique Ado Walkthrough Project.
* [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
* [Bootstrap Modal](https://getbootstrap.com/docs/5.1/components/modal/#tooltips-and-popovers)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [AmIResponsive](http://ami.responsivedesign.is/) for mockup of the site.

## Color Palette:
* [Coolors](https://coolors.co/) to generate my color palette.
## Images:
* [Freepik](www.freepik.com):
    * [Home page background image](https://www.freepik.com/vectors/flea-market) Flea market vector created by [freepik](www.freepik.com)
    * [Default image for loppis](https://www.freepik.com/vectors/flea-market) Designed by [freepik](www.freepik.com)

## Styles:
* [CSS Scan](https://getcssscan.com/css-box-shadow-examples): Box shadow in loppis details page is from [CSS Scan](https://getcssscan.com/css-box-shadow-examples) example number 3.

## Codes:
* Grepper: “check if date < today in django template” functionality logic is by [Grepper](https://www.codegrepper.com/code-examples/python/check+if+date+%3C+today+in+django+template).
    ```python
        {% now "Y-m-d" as todays_date %}
        {% if todays_date < someday|date:"Y-m-d" %}
            <h1>It's not too late!</h1>
        {% endif %}
    ```
* Condition date widget: 'Ensure start/end dates are not before "today", and end-date comes on/after start-date'. This logic is by Tim Nelson, mentor in Code Institute.
    ```javascript
        let now = new Date(),
        minDate = now.toISOString().substring(0,10);
        $("#id_start_date").prop("min", minDate);
        $("#id_start_date").on("change", setEndDateMin);
        $("#id_end_date").on("change", setEndDateMin);
        function setEndDateMin() {
            let startDate = $("#id_start_date").val();
            $("#id_end_date").prop("min", startDate);
        }
    ```
* Followed Code Institute's [Boutique Ado walkthrough project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) steps to add stripe and adjusted according to my sites needs.

# Acknowledgements
I would like to acknowledge and present my thanks to Tim Nelson, my mentor from Code Insitute for his guidance and constant support. It wouldn't have been possible without the amazing community in Slack, Tutors of Code insitute Tutor support, and my friends who constantly motivated and supported me. 