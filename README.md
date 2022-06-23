# SVERIGE LOPPIS

**Sverige Loppis: The Swedish Flea Market.**
OUR GOAL is to be the biggest platform for Swedish Flea Market/Sverige Loppis.
Sverige Loppis is hoping to be a platform for all the second hand sellers and buyers.

![Am I Responsive](/documentation/ami-responsive.png)

* Organize your Loppis day, add date, time, image of your loppis, add your address.
* Find many other loppisses around you by just a click of search and filter.
* Look for what is new. Search by County. Save other loppis announcements for later.
* Easily identify the loppises that are available or ended.
* To get immediately notified on any Loppis notification, subscribe to our newsletter.

*The Live Site can be found [here](https://sverigeloppis.herokuapp.com/).*

# Table of Contents:
* [User Experience (UX)](#ux)
    * [Strategy](#strategy)
    * [Scope & User Stories](#scope--user-stories)
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
* The primary target audience for this E-commerce site is Swedish Flea Market: Loppis. Sweden has a culture for buying and selling second-hand items. 
* This platform will give users easy access to loppises around. Users can easily and safely announce their loppises.
* The target audience currently is located in Sweden. In future, other countries will be added on to Sverige Loppis.
* There is no age gap of my audience, anyone can announce their loppis to sell their second hand items, or anyone can visit the site to find loppises they wish to go.
* I designed this platform with desgin thinking approach. With only the necessary content/information. User can surf the site easily and get the information they are looking for.

## Scope & User Stories
Please find all my defined user stories [here](https://github.com/MerveKucukzoroglu/sverigeloppis/issues?q=is%3Aclosed+label%3AUSER-STORY)

### Member User:
* As a member user I want to be able to login or logout so that I can access my personal account information.
* As a user I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
* As a user I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
* As a user I want to be able to have a personalised profile page so that I can manage my account, add/edit or delete loppises that I published.
* As a member user I want to be able to ask question to the loppis owner if I want to have more information regarding their loppis.

### Seller:
* As a seller I want to be able to add my own loppis announcement so that I can get buyers to come to my loppis and purchase.
* As a seller I want to be able to make payment with card so that I can my ad is successfully published in loppis list.
* As a seller I want to be able to see the amount of each announcement so that I can decide to proceed with payment or not.
* As a seller I want to be able to view my loppis information I entered just before payment so that I can make sure all the information I have entered are correct.
* As a seller I want to be able to adjust my loppis just before payment so that I can correct any mistakes before the payment.
* As a seller I want to be able to easily enter my payment information so that I can checkout smoothly.
* As a seller I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the information to make the payment.
* As a seller I want to be able to view a success page (payment and ad confirmation) so that I can verify that I haven't made any mistakes.
* As a seller I want to be able to receive an email confirmation after checkout so that I can keep the confirmation of my payment and to keep a record of it if I want.
* As a seller I want to be able to edit any loppis announcement I have added so that I can update/add or change any important information.
* As a seller I want to be able to delete any loppis announcement I have added so that I can be in control of my items posted.

### General Site visitor:
* As a site user I want to be able to view all loppis announcments so that I can save and consider going to loppis.
* As a site user I want to be able to find the menu easily so that I can know what content is available on the site.
* As a user I want to be able to easily register an account so that I can I can create and add my own loppis announcements.
* As a site user I want to be able to view the loppis details so that I can make an informed decision for my needs.
* As a site user I want to be able to navigate through the site so that I can view the desired content.
* As a user I want to be able to filter loppis by County so that I can find the ones that are closer to me.
As a user I want to be able to see the loppis date and time so that I can go to the flea markets(loppises) that are available during open hours.
* As a user I want to be able to save the announcements so that I can view the details later.
* As a user I want to be able to see the availability status of loppis so that I can know if it is expired.
* As a user I want to be able to search by title, description or county so that I can I can find easily to the one I want to go.
* As a user I want to be able to subscribe to newsletter so that I am informed about any loppises or announcements made.

### Admin
* As an admin I want to be able to have a support email so that I can I can be in control of any kind of support needed.
* As an admin I want to be able to in control of django admin panel so that I can I can take necessary actions for any misconduct or issue reported.

## Structure
This E-Commerce site is built giving the control of the user experience to the users. 
* If the user is just site visitor, they can: 
    * Find list of loppises, 
    * Loppis details,
    * Add loppis to their wishlist,
    * Subscribe to our newsletter,
    * Join and follow our Facebook page,
    * Surf the site and use search functionality,
    * Find information in 'About Page' on how Sverige Loppis works,
    * Access to register and create account
* If the user is a registered member user, in addition to a regular site visitor features, they can:
    * Have a personalized account,
    * Create and make a safe payment to publish Loppis Ad,
    * List of loppises they own within their profile page,
    * Ability to manage (edit or delete) the loppises they own,
    * Ask question to loppis owner,

*Throughout the project development, GitHub projects is used. Click [here](https://github.com/MerveKucukzoroglu/sverigeloppis/projects/1) to view the process.*

### Wireframes
Wireframes are the initial sketches of the application, but not the last. Over the coding process, the design and features have been upgraded and developed further to enhance user experience. Wireframes have been designed using [Balsamiq Wireframes](https://balsamiq.com/).

<details>
<summary>Each pages wireframes includes mobile(small screen), tablet(medium screen), desktop(large screens).</summary>

<details>
<summary>Home page:</summary>

![Wireframes](/documentation/w-mobile-home.png)

![Wireframes](/documentation/w-tablet-home.png)

![Wireframes](/documentation/w-desktop-home.png)
</details>

<details>
<summary>About page:</summary>

![Wireframes](/documentation/w-mobile-about.png)

![Wireframes](/documentation/w-tablet-about.png)

![Wireframes](/documentation/w-desktop-about.png)
</details>

<details>
<summary>Loppis page:</summary>

![Wireframes](/documentation/w-mobile-loppis.png)

![Wireframes](/documentation/w-tablet-loppis.png)

![Wireframes](/documentation/w-desktop-loppis.png)
</details>

<details>
<summary>Loppis details page:</summary>

![Wireframes](/documentation/w-mobile-loppis-details.png)

![Wireframes](/documentation/w-tablet-loppis-details.png)

![Wireframes](/documentation/w-desktop-loppis-details.png)
</details>

<details>
<summary>Login page:</summary>

![Wireframes](/documentation/w-mobile-login.png)

![Wireframes](/documentation/w-tablet-login.png)

![Wireframes](/documentation/w-desktop-login.png)
</details>

<details>
<summary>Register page:</summary>

![Wireframes](/documentation/w-mobile-register.png)

![Wireframes](/documentation/w-tablet-register.png)

![Wireframes](/documentation/w-desktop-register.png)
</details>

<details>
<summary>Profile page:</summary>

![Wireframes](/documentation/w-mobile-profile.png)

![Wireframes](/documentation/w-tablet-profile.png)

![Wireframes](/documentation/w-desktop-profile.png)
</details>

<details>
<summary>Add Loppis page:</summary>

![Wireframes](/documentation/w-mobile-add.png)

![Wireframes](/documentation/w-tablet-add.png)

![Wireframes](/documentation/w-desktop-add.png)
</details>

<details>
<summary>Edit Loppis page:</summary>

![Wireframes](/documentation/w-mobile-edit.png)

![Wireframes](/documentation/w-tablet-edit.png)

![Wireframes](/documentation/w-desktop-edit.png)
</details>

<details>
<summary>Manage Loppis page:</summary>

![Wireframes](/documentation/w-mobile-manage.png)

![Wireframes](/documentation/w-tablet-manage.png)

![Wireframes](/documentation/w-desktop-manage.png)
</details>

<details>
<summary>Checkout page:</summary>

![Wireframes](/documentation/w-mobile-checkout.png)

![Wireframes](/documentation/w-tablet-checkout.png)

![Wireframes](/documentation/w-desktop-checkout.png)
</details>

<details>
<summary>Success page:</summary>

![Wireframes](/documentation/w-mobile-success.png)

![Wireframes](/documentation/w-tablet-success.png)

![Wireframes](/documentation/w-desktop-success.png)
</details>

</details>
<br>

### Databases
Database below is the overall schema of the models used in this project. I have used [Lucidchart](https://lucid.app/documents#/dashboard) to generate the diagram below.

![Database Chart](/documentation/database.png)

**CUSTOM MODELS**

Within this application, I have used Django User Model and created my own Custom Models for this project. Below are the details of custom models:

1. Loppis Model:
    * Loppis Model is the main model for this application. 
    * Main functionalities to create, publish, manage loppis are connected to Loppis Model.
    * This model contains 'seller' which is ForeinKey of user from django user mdoel.
    * 'title' is the name of Loppis, created by user while adding the loppis. User can edit the title later if they want to.
    * Loppis page is sequenced by the new posts at top and old posts later. To generate this, I used 'created_on' DateTimeField which is auto generated in the backend at the time loppis ad is created by user.
    * 'start_date' and 'end_date' are the DateFields that holds the loppis events' dates. These fields are uneditable, therefore users are asked to carefully decide between which dates they will have loppis. The reason for not allowing user to edit these fields are for them to create new announcement for each loppis they organize. This two field have django calender widget. Start date and end date are also linked and controlled by javascript function so that end date is always on or after start date.
    * 'start_time' and 'end_time' are the open timings of loppis. These fields can be edited later based on the sellers availability and requirements. Both these fields are generated with django timer widget.
    * 'country' field is auto-filled and forced as "Sweden" as my initial target audience is based in Sweden. However in the future, it will be upgraded and country field will be open for any other country.
    * 'postcode' field is optional.
    * 'county' field is an important field for my initial audience in Sweden. County is a Foreign Key from County Model. 
    * 'city' and 'street_address' fields are required fields for identifying location of loppises. This helps users to find available loppises close to them.
    * 'phone_number' is an optional field. If the seller wants to provide their phone phone number to their loppis visitors/customers for easy reach, they can do so.
    * 'image' and 'image_url' fields are for adding images of their loppis, so that loppis owners can personalise their advertisement. It is optional, there is a default image provided if this field is left empty. 
    * 'description' is an optional field for adding details of loppis advertisements.

2. County Model:
    * County Model has been created for localizing Swedish Loppises. I have noticed that specifying county is one of the essential part of loppis announcements in Sweden. 
    * In this Model I had to divide list of county in two fields.
    * 'county' field is the name of county.
    * County means 'län' in Sweden. While mentioning counties, it is used by word 'län'. For example, Stockholms län. 'Stockholm' is the name of county and 'län' is the word used for county. 
    * Some of the counties change name adding the letter 's' to the end when used with 'län', e.g, Jönköpings län. However in some cases there is no additional letter to the county name, such as Örebro län. Considering this change in names, I have added another field 'friendly_name' for creating a list of counties same as how Swedish locals use.

3. Question Model:
    * This models gives users the ability to ask questions about loppis to the owner directly. 
    * For getting access to this feature, and ask a question, users are supposed to be signed in and have a registered account in the site. Even if the site visitors are not registered or signed in, they can read the questions asked within the loppis details page.
    * This feature is available inside each loppis details page.
    * 'loppis' field is foreign key from Loppis Model. This connects the Question asked to that particular Loppis.
    * 'author' is the person asking the question to the seller.
    * 'email' is collected from django user model for recording purposes. 
    * 'content' is the field for user to fill in and to type their question. This field holds the content of question.
    * 'created_on' is the DateTimeField for arranging the sequence of questions and help seller to identify when that particular question was asked.  

4. Subscription (Newsletter) Model:
    * Subscription is for subscribung our site newsletter. Any site visitor can subscribe to the newsletter, they do not have to register to the site for subscribing to our newsletter.
    * Subscription model has two fields: 'email' and 'subscribed_on'.
    * Anyone can subscribe by their 'email'. Once subscribed, the subscribers will get a thank you email for subscribing to our newsletter.
    * 'subscribed_on' field is auto generated DateTimeField for recording the day and time of subscriptions.

5. Advert Model:
    * This model has 3 fields. While creating a loppis advertisement, advert model generates the 'ad_number', 'stripe_pid' and 'ad_payment_date'.


# UI
## Color Palette:
![Color palatte](/documentation/loppis-color-palatte.png)
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
## Navbar:
Fixed navbar at top of the page. Users can easily navigate through the site.

![Navbar](/documentation/navbar.png)

Navbar is styled to be responsive and collapsible for smaller screens.

![Mobile-nav](/documentation/mobile-nav.png) 

![Mobile-menu](/documentation/mobile-menu.png)

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