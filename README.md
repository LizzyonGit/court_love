# court_love


## Planning

### Site goals

The website aims to offer users:
- a way to book individual tennis lessons online.
- a way to keep a personal profile with a self-rated level.

Inspired by [Matchi](https://www.matchi.se/) and [Grands](https://playgrands.com/se).

### User stories

See [project board](https://github.com/users/LizzyonGit/projects/6/views/1) for the agile methodology followed during this project and the end result. Implemented features in the **Done** column, future features and unfixed bugs in the **Won't do** column.

#### As a site admin, I can:
**Website layout milestone**
- display contact info so that I can be contacted by users.
- offer a clear landing page so that I can persuade users to book a lesson.

**Product management**
- add lessons to the website so that I can get bookings for them.
- edit lessons so that I can update details if there are any changes.
- delete a lesson so that I can prevent booking of a lesson if it is not offered anymore.

**Book lesson milestone**
- receive payments so that I get rewarded for my services.
- prevent bookings on full lessons so that I do not get overbooked lessons leading to refunds.

#### As a site user, I can:
**Website layout milestone**
- arrive at a clear landing page so that I can know what the website is about.
- get back to the top of the page with one click when there are a lot of lessons, so that I can easily get back to the menu.

**Product information milestone**
- find neccessary information about lessons so that I can book lessons that suit my needs.
- narrow down the list of lessons to specific characteristics so that I can easily view lessons that match my needs.
- see how many have booked lesson so that I can see how many will be joining.

**Book lesson milestone**
- add lessons to my cart so that I can proceed to payment.
- see an overview of my cart so that I can see which lessons I am about to buy.
- remove lessons from the cart so that I can manage what I am about to buy.
- navigate to a checkout page so that I can pay for my lessons.
- complete a payment so that I am allowed to attend the lesson.
- see a confirmation after payment so that I know that my payment has been successfull.
- get an email after purchase so that I can review my purchase any time and see when I should go to the lesson, without the need to log in.

**Authentication milestone**
- register so that I can log in to the website.
- log in so that I can see my order history and personal details.
- log out so that I can control whether I want to be logged in or not.

**User profile milestone**
- see my order history so that I can check what lessons I have booked.
- manage my self-rated level so that I can update it along my tennis lesson journey.
- manage a profile image so that I can personalise my profile page.

### Design
#### Database
Below is my initial database schema. I used [Lucidchart](https://lucid.app/lucidchart/2079b9e7-4f65-4200-8337-c7328cfd5e1e/edit?invitationId=inv_4a4f8b69-07b0-4019-82a4-0720dfb4bfd0&page=mkFtcNkq6Rib#) to create it.

#### Wireframes

Below are my initial wireframes for mobile and laptop screen sizes. I used [Figma](https://www.figma.com/) to create them.

#### Colour schemes
I used colours related to tennis with a shade of blue, red and green to reflect the different surfaces hard court, clay and grass. Yellow is derived from the tennis ball colour, white is the line colour, and black is used as a contrast colour.

This is my palette: https://coolors.co/0366A4-ffffff-F56B41-82b23d-000000-e3f121

#### Fonts
I used a font recommended with my logo from Canva from Daily Creative (https://www.canva.com/design/DAGr7kiK5zA/dRQFAGHjN97D28Y8rcLtyg/edit?ui=eyJHIjp7IkQiOnsiRCI6eyJBPyI6IkYifX19fQ): IBM Plex Sans. In google fonts, it was recommended to pair it with IBM Plex Serif (https://fonts.google.com/specimen/IBM+Plex+Serif/about?preview.text=Court%20Love&query=IBM+Plex)

#### Logos and images
I created the logo from a template in Canva. 

All images are free from [pixabay](https://pixabay.com/).

#### Content
All content is written by me.

## Features 

### Existing features

- __Navbar__

    - The navbar holds the logo, menu links depending on the login state of the user, the cart icon (tennis rackquet) and current cost for all lessons in the cart. The logo is in the upper left corner in the expanded navbar, in the compressed navbar it is in the center.

    ![Navbar logged in user]()
    ![Navbar logged out user]()

    ![Navbar compressed]()

    Project file: templates/base.html

- __Home page__

    - Buttons **Private lessons** and **Group lesson** to go to all private or group lessons.
    - **About Court Love** section with image carousel.
    - **How does it work** and **Register** sections and single image.
    - Stacked on small screens, up to two columns on larger screens.

    Project file: home/templates/home/index.html

- __Footer__
    - **Contact** section with cancellation info, phone and email, social media links.
    - **Places we teach at** with outdoor and indoor adresses.
    - Stacked on small screens, up to two columns on larger screens.

    Project file: templates/base.html

- __All lessons page__
    - Buttons **Group - indoor**, **Group - outdoor**, **Private - indoor** and **Private - outdoor** to filter the list of lessons. Two rows with two buttons on small screens, one row with four buttons on large screens.
    - Adjusted title **All lessons** or based on which button was clicked: **All group lessons - indoor**, **All group lessons - outdoor**, **All private lessons - indoor**, or **All private lessons - outdoor**.
    - Again the adresses for indoor and outdoor, as I did not want to have that in the lesson cards, and maybe users don't read the footer. Both addresses show when you click **All lessons**, only one shows when one of the buttons for outdoor or indoor were clicked.
    - A list of lesson cards, stacked on small screens and up to three columns on large screens.
    __Lesson card__
    - Image, if selected by site admin. Images can have different sizes but it is advised to use vertical images.
    - Date and time, duration, name as heading
    - Description: descriptions can differ in length and cause some distortions between 576 and 768 px screen width when the lesson cards are displayed in rows of two with the image in the top part. The cards are set to be the same height so the card footers are always aligned, but larger descriptions can make images smaller. It is therefore advised to use roughly the same description length. On screens smaller than 576 px the cards are stacked in one column so this is not an issue, and on screens larger that 767 px, the image is places to the left of the card, so it is not an issue.
    - Place: outdoor or indoor
    - Level
    - Capacity: how many people can join
    - Places left: how many places are left to book
    - Price
    - **Add to cart** button, or when there are no places left, **Not bookable** disabled button.
    - For site admin only: **Edit** and **Delete** buttons. Intentionally this section is not styled like the rest of the card, to highlight it is part of the admin.

    Project file: lessons/templates/lessons/lessons.html

- __Cart__
  - Overview of lesson cards showing only the date, time, duration, name, category, place, and price
  - Always stacked in one column
  - **Remove** button to remove the lesson form the cart
  - Grand total
  - Button **Pay** to go to checkout
  - If no lessons are in the cart, button to go to **All lessons**
    
    Project file: cart/templates/cart/cart.html



- __Checkout__
    - Details & payment
      - **Personal details** form
      - Option to save phone number if logged in, otherwise links to **Register** and **Log in** pages
      - **Payment details** with field to fill in card number and error message field (hidden if no error)
      - Buttons **Back to cart** and **Complete payment**
      - Note on how much will be charged
    - Order summary (number of lessons)
      - Lesson cards from the **Cart** page
      - Grand total
    - Stacked on small screens, up to two columns on larger screens.
    
    Project file: checkout/templates/checkout/checkout.html


- __Order confirmation__
    - **Payment succesful** page
      - After completing the payment, the user is will see this page.
      - From **My profile**, the user also can go to **Payment successful** pages  from old orders.
      - It has an introductory text with the order number, which you should hover over to see the whole number. This is because on small screens, this large number messes up the responiveness.
      - The booked lesson cards display the same as in the **Cart** page, and are stacked on all screen sizes. 
      - The grand total
      - If the user had come from the profile, there is a **Back to profile** button.
      
      Project file: checkout/templates/checkout/checkout_success.html

    - Order confirmation email
      - After a successful payment, the user will receive the order confirmation email.
      
      Project files: checkout/templates/checkout/confirmation_emails/confirmation_email_body.txt and confirmation_email_subject.txt



- __My profile__
    - Default personal information
    - Profile image

    - Booking history

    Project file: prodiles/templates/profiles/profile.html


- __Register__
- __Log in__
- __Log out__

- __Feedback messages__

- __The 404 page__


#### Site admin only
- __Add lesson__
    - 

- __Edit lesson__

- __Delete lesson__

### Features left to implement

- Possibility to select a date range to filter the lesson list.
- Email address field on My profile with possibility to change it and prepopulate checkout form with it.
- Link directly to lesson after editing/adding a lesson, and for the user, from the cart page.
- When site admin cancels an order in admin, lessons' **Places left** is increased automatically.

#### Future ideas
- Make profile visible for others attending a lesson, so you can see each other's level and profile image. Maybe even with chat groups automatically created so you can talk with the attendees before and after a lesson. This would of course need much more security both for the image which now is only visible for the user and in admin, but also for chat messages.
- Sell gift cards for tennis lessons.
- Users can add themselves to a wait list for fully booked lessons and get notified in case someone canceled.
- Users can choose to get notified by email when new lessons have been added.
- You can only book lessons according to your level.
- Reviews page for Court Love as a company.




## Testing

See [TESTING.md](TESTING.md).

## Technologies used

### Languages

- HTML
- CSS
- Python
- JavaScript

### Frameworks - libraries - programs used

- [Django](https://www.djangoproject.com/) version 5.2.4
  - Including *django-allauth*, *django-crispy-forms*.
  - With installed whitenoise and gunicorn.
- [Bootstrap](https://getbootstrap.com/) version 5.3
- [jQuery](https://jquery.com/) version 3.5.1
- [Stripe](https://stripe.com/) for payment solution
- [Lucidchart](https://lucid.co/) for database planning
- [Figma](https://www.figma.com/) for wireframes
- [VS Code](https://code.visualstudio.com/) as IDE
- [GitHub](https://github.com/) for version control
- [Heroku](https://www.heroku.com/) for hosting
- [Cloudinary](https://cloudinary.com/) for image hosting
- [Google Fonts](https://fonts.google.com/) for my font pair and tennis racquet cart icon
- [Canva](https://www.canva.com/) for creating the logo
- Windows Paint and Windows Photo for adjusting images
- [TinyPNG](https://tinypng.com/) for compressing image size and converting to .webp
- [RealFaviconGenerator](https://realfavicongenerator.net/) for creating favicon icons and the HTML code, and checking the favicon
- Chrome DevTools for verifying responsibility and troubleshooting code
- [Am I Responsive](https://ui.dev/amiresponsive) for an image displaying the website on different screens
- [Autoprefixer](https://autoprefixer.github.io/) for adding the necessary prefixes to my CSS stylesheet

## Deployment and development

### Deployment
The site was deployed to Heroku. The steps to deploy are:

1. Go to your Heroku dashboard and create a new app.
2. In the **Deploy** tab of your new app, under **Deployment method**, click **GitHub**. 
3. Under **Connect to GitHub**, in the field next to your username on Github, type the repository name (*LizzyonGit/rates_r_us*) of the project and click **Search**. 
4. The corresponding repository name appears below, click the **Connect** button.
5. In **Settings**, under **Config Vars**, add a value for keys *SECRET_KEY*, *DATABASE_URL* and *CLOUDINARY_URL*.
6. Scroll down to **Manual deploy**, select the main branch to deploy and click **Deploy Branch**.
7. At the top of the page, click **Open app** to open the site.

### Local development
To fork the repository:
  - In the GitHub repository, click the **Fork** button in the top right corner.

To clone the repository:
  1. In the GitHub repository, click the **Code** button.
  2. In the **Local** tab, select if you want to clone with HTTPS, SSH, or GitHub CLI, and copy the link below it.
  3. Open the terminal in your code editor and change the current working directory to the location you want to clone this repository to.
  4. Type *git clone* and paste the link from step 2, and press Enter.

Set up your IDE
  1. Set up a virtual environment.
  2. Install the packages from the requirements.txt file.
  3. Create variables for *SECRET_KEY*, *DATABASE_URL* and *CLOUDINARY_URL*.
  4. Apply migrations.
  5. Collect static files.
  6. Run the development server.

## Credits 

### Media

- Free images from [pixabay](https://pixabay.com/). Logo adapted from [Canva](https://www.canva.com/).

### Resources

__Planning__
- For a font pairing idea, [Google Fonts](https://fonts.google.com/) based on font used in logo from [Canva](https://www.canva.com/).

- For getting a colour scheme, [Coolors.co](https://coolors.co).

__During development and testing__
- Inspiration and code bits from CI walkthrough projects *I think therefore I blog* and *Boutique Ado*.
- [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
- [Django documentation](https://docs.djangoproject.com/)
- [Stripe documentation](https://docs.stripe.com/)
- Forums for specific questions:
  - [Django forum](https://forum.djangoproject.com/)
  - [Stackoverflow](https://stackoverflow.com/)
  - [Reddit](https://www.reddit.com/)
  - CI Slack community.
- Informative sources for reading up on concepts:
  - [W3schools](https://www.w3schools.com/)
  - [MDN Web Docs](https://developer.mozilla.org/en-US/)
  - [Medium.com](https://medium.com/)
  - [LearnDjango](https://learndjango.com/)
  - [GeeksforGeeks](https://www.geeksforgeeks.org/)
  - [Information on bare except](https://jerrynsh.com/stop-using-exceptions-like-this-in-python/)


__Project finalisation__ 
- [Grammarly](https://www.grammarly.com/grammar-check) spellchecker.

### Acknowledgments
- My mentor Jubril for the feedback.
