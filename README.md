# court_love

colour scheme
I used colours related to tennis with a shade of blue, red and green to reflect different surfaces hard court, clay and grass. Yellow is derived from the tennis ball colour, white is the line colour, and black will be the main text colour.

fonts
I used a font recommended with my logo from Canva from Daily Creative (https://www.canva.com/design/DAGr7kiK5zA/dRQFAGHjN97D28Y8rcLtyg/edit?ui=eyJHIjp7IkQiOnsiRCI6eyJBPyI6IkYifX19fQ): IBM Plex Sans. In google fonts, it was recommended to pair it with IBM Plex Serif (https://fonts.google.com/specimen/IBM+Plex+Serif/about?preview.text=Court%20Love&query=IBM+Plex)

Image with lesson
I wanted to have images with the lesson, even though it is not neccesary. So I did not want to give the user the possibility of uploading an image, as it is not neccessary, but I still want to give some choice to the user in which image will be used. So I fount this interesting option of using choices (https://stackoverflow.com/questions/31948172/python-django-form-where-user-selects-from-a-list-of-images, by Pynchia), which seemed easy and enough for the MVP. To make this work, I also followed the instructions of Melvyn Sopacua here (https://groups.google.com/g/django-users/c/iP2TmUHwdDI). 

## Planning

### Site goals

The website aims to offer users:
- a way to book individual tennis lessons online.
- a way to keep a profile with a self-rated level.

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

#### As a site user, I can
**Website layout milestone**
- arrive at a clear landing page so that I can know what the website is about.
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

### Design
#### Database
Below is my initial database schema. I used [Lucidchart](https://lucid.app/lucidchart/2079b9e7-4f65-4200-8337-c7328cfd5e1e/edit?invitationId=inv_4a4f8b69-07b0-4019-82a4-0720dfb4bfd0&page=mkFtcNkq6Rib#) to create it.

#### Wireframes

Below are my initial wireframes for mobile and laptop screen sizes. I used [Figma](https://www.figma.com/) to create them.

#### Colour schemes
I used colours related to tennis with a shade of blue, red and green to reflect the different surfaces hard court, clay and grass. Yellow is derived from the tennis ball colour, white is the line colour, and black is used as a contrast colour.

This is my palette: https://coolors.co/047cc5-ffffff-ea592c-82b23d-000000-e3f121

#### Fonts
I used a font recommended with my logo from Canva from Daily Creative (https://www.canva.com/design/DAGr7kiK5zA/dRQFAGHjN97D28Y8rcLtyg/edit?ui=eyJHIjp7IkQiOnsiRCI6eyJBPyI6IkYifX19fQ): IBM Plex Sans. In google fonts, it was recommended to pair it with IBM Plex Serif (https://fonts.google.com/specimen/IBM+Plex+Serif/about?preview.text=Court%20Love&query=IBM+Plex)

#### Logos and images
I created the logo from a template in Canva. 

All images are free from [pixabay](https://pixabay.com/).

#### Content
All content is written by me.

## Features 

### Existing features

-__Navbar__

    - The navbar holds the logo, menu links depending on the login state of the user, the cart logo and current cost for all lessons in the cart. 

    ![Navbar logged in user]()
    ![Navbar logged out user]()

    ![Navbar compressed]()

    Project file: templates/base.html