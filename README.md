# SVERIGE LOPPIS

# Table of Contents:

# UX
## Strategy
## User Stories
## Scope
## Structure
### Wireframes
### Databases

# UI
## Color Palette
## Fonts

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
## Saved Loppis Page
## Purchase/Advertise Function
##

# Technologies Used

# Testing

# Deployment

# Credits
## Images:
* [Freepik](www.freepik.com):
    * [Home page background image](https://www.freepik.com/vectors/flea-market) Flea market vector created by [freepik](www.freepik.com)

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

# Acknowledgements