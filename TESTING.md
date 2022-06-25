# Validator Testing
Minor errors found, resolved the issues and all tests passed.

## [W3C Markup Validation Service](https://validator.w3.org/)
* Home Page:

    ![Home Page](/documentation/html-home.png)

* About Page: 

    ![About Page](/documentation/html-about.png)

* Loppises Page: 

    ![Loppises Page](/documentation/html-loppises.png)

* Advert(add) Page: 

    ![Add Page](/documentation/html-advert.png)

* Wishlist Page: 

    ![Wishlist Page](/documentation/html-wishlist.png)

* Signup Page: 

    ![Signup Page](/documentation/html-signup.png)

* Login Page: 

    ![Login Page](/documentation/html-login.png)

* Subscription Page: 

    ![Subscription Page](/documentation/html-subscription.png)

* Profile Page: 

    ![Profile Page](/documentation/html-profile.png)

* Loppis Details Page: 

    ![Loppis Details Page](/documentation/html-loppis-details.png)

## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
No errors or warnings found.

![CSS Validator](/documentation/css-validator.png)

## [JSHint Validator](https://jshint.com/)
Version wrror found. Added '/* jshint esversion: 11, jquery: true */' at the top of js file and resolved the issues.

![JSHint Validator](/documentation/jshint.png)

## PEP8 Validator Testing
Passed all PEP8 Validator testing

<details>
<summary>About App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![About app apps.py file](/documentation/pep8-about-apps.png)
urls.py       | ![About app urls file](/documentation/pep8-about-urls.png)
views.py      | ![About app views file](/documentation/pep8-about-views.png)

</details>

<details>
<summary>Advert App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![Advert app apps.py file](/documentation/pep8-advert-apps.png)
forms.py      | ![Advert app urls file](/documentation/pep8-advert-forms.png)
models.py     | ![Advert app urls file](/documentation/pep8-advert-models.png)
urls.py       | ![Advert app urls file](/documentation/pep8-advert-urls.png)
views.py      | ![Advert app views file](/documentation/pep8-advert-views.png)

</details>

<details>
<summary>Home App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![Home app apps.py file](/documentation/pep8-home-apps.png)
urls.py       | ![Home app urls file](/documentation/pep8-home-urls.png)
views.py      | ![Home app views file](/documentation/pep8-home-views.png)

</details>

<details>
<summary>Loppises App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![Loppises app apps.py file](/documentation/pep8-loppises-apps.png)
models.py     | ![Loppises app urls file](/documentation/pep8-loppises-models.png)
urls.py       | ![Loppises app urls file](/documentation/pep8-loppises-urls.png)
views.py      | ![Loppises app views file](/documentation/pep8-loppises-views.png)
widgets.py    | ![Loppises app widgets file](/documentation/pep8-loppises-widgets.png)

</details>

<details>
<summary>Profiles App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![Profiles app apps.py file](/documentation/pep8-profiles-apps.png)
urls.py       | ![Profiles app urls file](/documentation/pep8-profiles-urls.png)
views.py      | ![Profiles app views file](/documentation/pep8-profiles-views.png)

</details>

<details>
<summary>Questions App</summary>

Python files  | PEP8 result
------------- | -------------
admin.py      | ![Questions app admin.py file](/documentation/pep8-questions-admin.png)
apps.py       | ![Questions app apps.py file](/documentation/pep8-questions-apps.png)
models.py     | ![Questions app models file](/documentation/pep8-questions-models.png)
forms.py      | ![Questions app forms file](/documentation/pep8-questions-forms.png)

</details>

<details>
<summary>Newsletter Subscription App</summary>

Python files  | PEP8 result
------------- | -------------
admin.py      | ![Subscription app admin.py file](/documentation/pep8-subscription-admin.png)
apps.py       | ![Subscription app apps.py file](/documentation/pep8-subscription-apps.png)
models.py     | ![Subscription app models file](/documentation/pep8-subscription-models.png)
forms.py      | ![Subscription app forms file](/documentation/pep8-subscription-forms.png)
views.py      | ![Subscription app views file](/documentation/pep8-subscription-views.png)
urls.py       | ![Subscription app urls file](/documentation/pep8-subscription-urls.png)

</details>

<details>
<summary>Sverige Loppis Main App</summary>

Python files  | PEP8 result
------------- | -------------
wsgi.py       | ![Main app wsgi.py file](/documentation/pep8-main-wsgi.png)
urls.py       | ![Main app urls file](/documentation/pep8-main-urls.png)
views.py      | ![Main app views file](/documentation/pep8-main-views.png)

</details>

<details>
<summary>Wishlist App</summary>

Python files  | PEP8 result
------------- | -------------
apps.py       | ![Wishlist app apps.py file](/documentation/pep8-wishlist-apps.png)
contexts.py   | ![Wishlist app contexts.py file](/documentation/pep8-wishlist-contexts.png)
urls.py       | ![Wishlist app urls file](/documentation/pep8-wishlist-urls.png)
views.py      | ![Wishlist app views file](/documentation/pep8-wishlist-views.png)

</details>

## Lighthouse
* Testing results for desktop:

    ![Lihghthouse Desktop](/documentation/lighthouse-desktop.png)

* Testing results for mobile:

    ![Lihghthouse Desktop](/documentation/lighthouse-mobile.png)

## User Story Testing
Please find all my defined user stories [here](https://github.com/MerveKucukzoroglu/sverigeloppis/issues?q=is%3Aclosed+label%3AUSER-STORY)

### Member User:
* As a member user I want to be able to login or logout so that I can access my personal account information.

    <details>
    <summary>View Images</summary>

    ![Login](/documentation/login.png)

    ![Login Success](/documentation/login-success.png)

    ![Logout](/documentation/logout.png)

    ![Logout Success](/documentation/logout-success.png)

    </details>
    <br>

* As a user I want to be able to easily recover my password in case I forget it so that I can recover access to my account.

    <details>
    <summary>View Images</summary>

    ![Password Reset](/documentation/password-reset.png)
    ![Password Reset](/documentation/password-email-sent.png)
    ![Password Reset](/documentation/password-reset-email.png)
    ![Password Reset](/documentation/change-password.png)
    ![Password Reset](/documentation/password-change-success.png)

    </details>
    <br>

* As a user I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.

    <details>
    <summary>View Images</summary>

    ![Verify Email Registration](/documentation/email-verify.png)
    ![Verify Email Registration](/documentation/email-verify-alert.png)
    ![Verify Email Registration](/documentation/email-confirm-mail.png)
    ![Verify Email Registration](/documentation/email-confirm-link.png)
    ![Verify Email Registration](/documentation/email-verify-success-alert.png)

    </details>
    <br>

* As a user I want to be able to have a personalised profile page so that I can manage my account, add/edit or delete loppises that I published.

    <details>
    <summary>View Images</summary>

    ![Profile Page](/documentation/profile-page.png)
    ![My loppises Page](/documentation/my-loppises.png)
    </details>
    <br>

* As a member user I want to be able to ask question to the loppis owner if I want to have more information regarding their loppis.

    <details>
    <summary>View Images</summary>

    ![Question](/documentation/question-1.png)
    ![Question](/documentation/question-2.png)
    </details>
    <br>

### Seller:
* As a seller I want to be able to add my own loppis announcement so that I can get buyers to come to my loppis and purchase.

    <details>
    <summary>View Images</summary>

    ![Add](/documentation/add-page.png)
    </details>
    <br>

* As a seller I want to be able to make payment with card so that my ad is successfully published in loppis list.

    <details>
    <summary>View Images</summary>

    ![Add](/documentation/payment.png)
    </details>
    <br>

* As a seller I want to be able to view my loppis information I entered just before payment so that I can make sure all the information I have entered are correct.
* As a seller I want to be able to adjust my loppis just before payment so that I can correct any mistakes before the payment.
* As a seller I want to be able to easily enter my payment information so that I can checkout smoothly.

    <details>
    <summary>View Images</summary>

    ![Add](/documentation/add-page.png)
    </details>
    <br>

* As a seller I want to be able to see the amount of each announcement so that I can decide to proceed with payment or not.

    <details>
    <summary>View Images</summary>

    ![Add](/documentation/add-intro.png)
    ![Add](/documentation/payment.png)
    </details>
    <br>

* As a seller I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the information to make the payment.

    <details>
    <summary>View Images</summary>

    ![Add](/documentation/add-intro.png)
    ![About](/documentation/about-3.png)
    </details>
    <br>

* As a seller I want to be able to view a success page (payment and ad confirmation) so that I can verify that I haven't made any mistakes.

    <details>
    <summary>View Images</summary>

    ![Success](/documentation/success-page.png)
    </details>
    <br>

* As a seller I want to be able to receive an email confirmation after checkout so that I can keep the confirmation of my payment and to keep a record of it if I want.

    <details>
    <summary>View Images</summary>

    ![Success Email](/documentation/confirmation-email.png)
    </details>
    <br>

* As a seller I want to be able to edit any loppis announcement I have added so that I can update/add or change any important information.

    <details>
    <summary>View Images</summary>

    ![Edit](/documentation/loppis-details-seller.png)
    ![Edit](/documentation/edit-1.png)
    ![Edit](/documentation/edit-2.png)
    </details>
    <br>

* As a seller I want to be able to delete any loppis announcement I have added so that I can be in control of my items posted.

    <details>
    <summary>View Images</summary>

    ![Delete](/documentation/loppis-details-seller.png)
    ![Delete](/documentation/delete-modal.png)
    </details>
    <br>

### General Site visitor:
* As a site user I want to be able to view all loppis announcments so that I can save and consider going to loppis.

    <details>
    <summary>View Images</summary>

    ![Loppis List](/documentation/loppis.png)
    ![Loppis List](/documentation/loppis-details-visitor.png)
    </details>
    <br>

* As a site user I want to be able to find the menu easily so that I can know what content is available on the site.
* As a site user I want to be able to navigate through the site so that I can view the desired content.

    <details>
    <summary>View Images</summary>

    ![Menu](/documentation/navbar.png)
    ![Menu](/documentation/mobile-nav.png)
    </details>
    <br>

* As a user I want to be able to easily register an account so that I can I can create and add my own loppis announcements.

    <details>
    <summary>View Images</summary>

    ![Register](/documentation/register.png)
    </details>
    <br>

* As a site user I want to be able to view the loppis details so that I can make an informed decision for my needs.

    <details>
    <summary>View Images</summary>

    ![Loppis details](/documentation/loppis-details-visitor.png)
    </details>
    <br>

* As a user I want to be able to filter loppis by County so that I can find the ones that are closer to me.
    <details>
    <summary>View Images</summary>

    ![County](/documentation/counties.png)

    ![County](/documentation/county-tag.png)

    ![County](/documentation/county-tag-details.png)

    ![County](/documentation/county-search.png)
    </details>
    <br>

* As a user I want to be able to see the loppis date and time so that I can go to the flea markets(loppises) that are available during open hours.

    <details>
    <summary>View Images</summary>

    ![Loppis details](/documentation/loppis-details-visitor.png)
    </details>
    <br>

* As a user I want to be able to save the announcements so that I can view the details later.

    <details>
    <summary>View Images</summary>

    ![Wishlist](/documentation/wishlist.png)
    </details>
    <br>

* As a user I want to be able to see the availability status of loppis so that I can know if it is expired.

    <details>
    <summary>View Images</summary>

    ![Availability Status](/documentation/available-details.png)

    ![Availability Status](/documentation/available-loppis.png)

    ![Availability Status](/documentation/ended-details.png)

    ![Availability Status](/documentation/ended-loppis.png)

    </details>
    <br>

* As a user I want to be able to search by title, description or county so that I can I can find easily to the one I want to go.

    <details>
    <summary>View Images</summary>

    ![Search](/documentation/navbar.png)

    ![Search](/documentation/mobile-nav.png)

    ![Search](/documentation/search-0.png)

    ![Search](/documentation/search.png)
    </details>
    <br>

* As a user I want to be able to subscribe to newsletter so that I am informed about any loppises or announcements made.

    <details>
    <summary>View Images</summary>

    ![Subscribe](/documentation/subscribe-footer.png)

    ![Subscribe](/documentation/newsletter-subscription.png)

    ![Subscribe](/documentation/subscribed-success-message.png)

    ![Subscribe](/documentation/newsletter-subscription-confirmation-email.png)

    </details>
    <br>

### Admin
* As an admin I want to be able to have a support email so that I can I can be in control of any kind of support needed.

    <details>
    <summary>View Images</summary>

    ![Admin contact mail](/documentation/footer.png)
    </details>
    <br>

* As an admin I want to be able to in control of django admin panel so that I can I can take necessary actions for any misconduct or issue reported.

    <details>
    <summary>View Images</summary>

    ![Admin contact mail](/documentation/admin-django.png)
    </details>
    <br>

## BUGS
* There is no unsolved bug in my site (as far as I know).
* Throughout the development process, I faced minor issues but resolved them after several tries. 
* I had one bug that I struggled with:
    * Problem Statement - "Whenever the payment is completed, django sends me emails from myself rather than the address of the user."
    * You can view my process with this bug in [Github Projects](https://github.com/MerveKucukzoroglu/sverigeloppis/issues/64) 
    * I did a deep search in Google, [Stack Overflow](https://stackoverflow.com/) and [Django Documentations](https://www.djangoproject.com/).
    * I first added the sending email function. At first the problem I faced was the sender email received the emails so it was never being sent to the user.
    * Then I tried getting the value of email from Django user model.
    * I used "User.email" for that, the email got sent successfully in the terminal however the users email was mentioned as "deferred attribute object".
    * I have talked to Code Institute tutors and my Mentor about this issue. If the email is not successfully sent it fails the stripe payment as it is placed in stripe webhook class, it needs successful email for stripe to complete it's function.
    * With Code Institute's Tutor Gemma and Mentor Tim suggestions I have created a separate function within advert/views, and called this inside advert_success function.
    * By removing the webhooks and adding a email function within the views solved the bug.
    * Now the user successfully recieves confirmation emails for their payment and loppis advertisement.