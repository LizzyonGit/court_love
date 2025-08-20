# Court Love - Testing

[Live link to website](https://court-love-8302d0b2e53d.herokuapp.com/)


## Automated testing


### HTML validator
No current errors in the [HTML validator](https://validator.w3.org/). Below I list some of the fixed issues.

- Some issue came up about h2 tags on the **All lessons** page. This is because I adjust the heading content depending on which button is clicked, and I did not separate the h2 per category or place, so this resulted in either an empty h2 tag or a trailing h2 tag. So I fixed this with separate h2 blocks and added a class to display them on one line next to each other. So in case there is both a category and a place, there is a correct heading visible, that consists of two h2 blocks next to each other.

- On the **My profile** page, I got an error about a duplicate id attribute, caused by the django widget handling the image upload. [Slack](https://code-institute-room.slack.com/archives/C026VTHQDNY/p1683142277576629) helped me to understand the issue, so I replaced the id "new-image" I set with a class of the same name, and updated the jQuery for this. This worked and the error dissapeared.

  Another issue on the same page was that I had set a placeholder for a select element (**level**), I found a similar error on [Slack](https://code-institute-room.slack.com/archives/C026VTHQDNY/p1714631167308539). I decided to remove the code about placeholders (this was copied and adapted from other fields) because it actually only was applicable to the **Phone number** field, which already had a label. So the error also dissapeared.

- 


### CSS validator
No errors, only mention of variables not being checked and that the border-color and background-color are the same for a checkbox, which is intentional.

### Python validator
Before running my code through the [CI Python Linter](https://pep8ci.herokuapp.com/) I fixed the relevant Flake8 issues raised in VS Code about too long lines, bare except usage, unused imports and whitespaces.

I ran the following pages through the validator:

#### Cart app
No errors: contexts.py, views.py, urls.py, apps.py.

#### Checkout app
No errors: admin.py, apps.py, forms.py, models.py, signals.py, urls.py, views.py, webhook_handler.py, webhooks.py

#### Home app
No errors: apps.py, urls.py, views.py

#### Lessons app
No errors: admin.py, apps.py, urls.py
Ignored *line too long* because of url in comment: forms.py, models.py views.py

#### Profiles app
No errors: admin.py, apps.py, forms.py, urls.py, views.py, widgets.py
Ignored *line too long* because of long url in comment, and indented comment which I think should not be split: models.py



### Javascript validator
Checking the JavaScript and jQuery in [JSHint](https://jshint.com/), I get some undefined variables for *Stripe* and *bootstrap*, which can be ignored as they are coming from the Stripe and Bootstrap scripts.

### Lighthouse testing
I had some contrast issues with my main background colour and white and yellow text. I chose to change my blue from #047cc5 to a darker shade #0366A4, and any black text I had I changed to white. 
For my red **Delete** buttons, the contrast was also not good, so I changed from #ea592c to a lighter shade of red #F56B41. 

https://court-love-8302d0b2e53d.herokuapp.com/lessons/

A remaining accessibility issue for **All lessons** is that I have hidden form input that foes not have a label, but it is hidden so I ignore this issue.

Best practices warns about third party cookies from Stripe, and about issues logged to the Issue panel, also related to Stripe, so I cannot change that. Actuelly, in incognito mode, this is gone and 100%.

Performance testing did not give issues that I can fix, because I already cut down the size of my images so they would still be good at all screens sizes. So I'm happy with 90%.

https://court-love-8302d0b2e53d.herokuapp.com/checkout/

I get an accessibility warning *[aria-hidden="true"] elements contain focusable descendents*, but it refers to a Stripe element which I can not change.




For some pages I get an issue about the footer's heading not being in descending order. This is because the footer is written in the base template, so it can not consider the heading on each page. Also, not all pages have an h2 heading, but some have, so my footer is set to ahve h3 headings. I kept this like it is.

### Favicon testing
In [RealFaviconGenerator's favicon checker](https://realfavicongenerator.net/favicon-checker) my favicon gets no warnings. The only issue is a missing touch web app title, but then the website's title will be used so it is no problem.

## Manual testing


### User story testing

|   User story                                                            | How it is achieved    |
|  -----------                                                             | -----------           |
|**As a site admin, I can:**|
|display contact info so that I can be contacted by users,|Added social media links, email address and phone number in footer, and email address in confirmation email.|
|offer a clear landing page so that I can persuade users to book a lesson,|**About Court Love**, **How does it work** and **Register** sections, photo carousel, buttons to lessons.|
|add lessons to the website so that I can get bookings for them,|**Add lesson** page where you add more lessons to display on the **All lessons** page.|
|edit lessons so that I can update details if there are any changes,|**Edit** button on each lesson, leading to the **Edit lesson** form where you can edit the lesson and update it.|
|delete a lesson so that I can prevent booking of a lesson if it is not offered anymore,|**Delete** button on each lesson, opening a modal asking for confirmation before deleting the lesson. After deleting, the lesson is removed from the website, but may still be in admin, depending on if it was booked before. The site admin is informed about this in the modal.|
|receive payments so that I get rewarded for my services,|Working Stripe integration.|
|prevent bookings on full lessons so that I do not get overbooked lessons leading to refunds.|When adding a lesson, there is a field for **Capacity** and **Places left**. If you don't fill in **Places left**, it will be set to the **Capacity** amount. Each purchase the **Places left** will count down, when it is zero, the lesson can not be added to the cart anymore, or it will be removed from there if it was already added. If a user would pass the cart view and go direclty to checkout via the url, the user would be reverted back to the updated cart if there was a lesson with zero places left in the checkout, so it is not possible to book it.|
| | |
|**As a site user, I can:**|
|arrive at a clear landing page so that I can know what the website is about.|**About Court Love**, **How does it work** and **Register** sections, photo carousel, buttons to lessons.|
|get back to the top of the page with one click when there are a lot of lessons, so that I can easily get back to the menu.|A little icon with an arrow up which you can click at any time on the bottom right of the **All lessons** page, taking you to the top of the page|
|find neccessary information about lessons so that I can book lessons that suit my needs.|The lesson cards with date, time, duration, description, place, level, capacity and price, and the addresses on top of the **All lessons** page, and in the footer.|
|narrow down the list of lessons to specific characteristics so that I can easily view lessons that match my needs.|From the home page, you can click **Private lessons** and **Group lessons**, to filter on those categories. On the **All lessons** page, there are buttons to filter on **Group - Indoor**, **Group - Outdoor**, **Private - Indoor** or **Private - Outdoor**.|
|see how many have booked lesson so that I can see how many will be joining.|**Places left** on the lesson cards, and in the booking history when you go to an old order confirmation, the updated **Places left** is there as well.|
|add lessons to my cart so that I can proceed to payment.|**Add to cart** button on each lesson card, if not fully booked already.|
|see an overview of my cart so that I can see which lessons I am about to buy.|**Cart** page via the tennis racquet icon to the right in the navigation bar, or via the button in the toast messages coming up after adding a lesson to the cart.|
|remove lessons from the cart so that I can manage what I am about to buy.|**Remove** button on each lesson card in the **Cart** page.|
|navigate to a checkout page so that I can pay for my lessons.|On the **Cart** page, there is a **Pay** button taking you to the **Checkout** page. The **Checkout** page hase|
|complete a payment so that I am allowed to attend the lesson.|**Complete payment** button on the **Checkout** page, **Stripe** integrations and webhooks in case something goes wrong, so the order is still added.|
|see a confirmation after payment so that I know that my payment has been successfull.|**Checkout successful** page and toast message after payment.|
|get an email after purchase so that I can review my purchase any time and see when I should go to the lesson, without the need to log in.| Order confirmation email sent after payment.|
|register so that I can log in to the website.|**Register** page.|
|log in so that I can see my order history and personal details.|**Log in** page.|
|log out so that I can control whether I want to be logged in or not.|**Log out** page.|
|see my order history so that I can check what lessons I have booked|**My profile** page with **Booking history** column.|
|manage my self-rated level so that I can update it along my tennis lesson journey|**Level** field on the **My profile** page.|
|manage a profile image so that I can personalise my profile page.|**Select image**  and **Update** buttons on **My profile** to add or update an image, **Remove current profile image after Update** checkbox to remove an image.|


### Issues

#### Capacity handler
To handle the capacity number going down after someone booking a lesson, I tried several approaches. Initially, I thought the capacity number on the lesson model could just go down, but capacity is actually a foreign key to the Capacity model, because I wanted site admins to be able to add their own capacity values in admin with that model. So I tried implementing something like [this](https://stackoverflow.com/questions/61310901/how-to-update-a-value-from-table-accessed-via-foreign-key-django-orm), but this did not work as the Capacity model itself was changed, so 4 would just change 3 for example, and with that all lessons initially having 4 capacity would change to 3. I thought about changing the foreign key field to a normal field, but I also wanted to have two values, so that you could see the original capacity and how many places were booked or free. That was a much easier solution to have a separate field for **Places left** in the Lesson model, so I added that. This way, Capacity could just remain the same and all calculations could be done on the new field **Places left**. I put in a code to set **Places left** to the same initial value as **Capacity**, but a site admin can also manually adjust this for any reason. Then the **Places left** values decreases when the order line item is created either in the view, or via a webhook. 

There is an unfixed issue which is when something goes wrong when creating an order via a webhook, and the order is deleted after an updated lesson with a new **Places left** value is saved, this would not be reversed. The reason for this is that I can not test this situation at this point, so I would rather not add any code that could break the webhook flow.

#### Cart update when lesson is not bookable anymore
I wanted to address the possibilty of a user having lessons in the cart that have been fully booked in the meantime, so **Places left** is 0, so the user should not be able to book those kinds of lessons. They can not be added to the cart, but they could have been there already. I tried to delete those order line items in the checkout, but I got an error message. I tried also to just removed the items from the order summary, but then you could go back to the cart and have the items there again. So I moved this logic to the card instead, and instead of directing to the checkout directly from the cart logo, which I wanted initially, I changed the cart logo link to go to the cart page. Now the order summary can just be taken from the cart, so checkout does not need the logic to remove these unbookable items. Now there was only an issue if the user would use the checkout url and not go via the cart at all, so I simply wrote in a code to go back to the cart in case there is a lesson with 0 places left. The user then gets the feedback message in the cart about the removed items.

#### Delete functionality
I had implemented the same delete functionality as in Boutique Ado, but faced issues accessing orders containing only deleted lessons. Opening order lines with a deleted lesson or orders with only deleted lessons resulted in a 500 error in admin. I tried to change the OrderLineItem model setting deleted lessons to Null, but this did not fix it. So I went for a 'soft delete', as suggested on [Stackoverflow](https://stackoverflow.com/questions/42954063/storing-products-in-order-product-is-deleted-after-order-placed). So now from the frontend, site admins can delete a lesson but it will just set the *deleted* field to True, and it will not appear on the website. The site admin will still receive a notification when deleting a lesson that already has been booked before, so they can go to admin and find the order and user details to inform the user about the deletion. They simply go to Order line items, find the order line items with the delete lesson, and go to the orders via the eye ball on the order line item pages.

To prevent issues when a site admin 'hard deletes' a lesson in admin, I set *on_delete=models.PROTECT* for the lesson foreign key on the OrderLineItem model, so site admins should first manually delete order lines/orders if they want to delete a lesson. 

But then I realised that this may not fulfill the CRUD functionality, so in the end, I opted for a combination of the two. When a lesson has been booked, the site admin can not remove it from the database before deleting the connected orders in admin. But when there are no connected orders, the lesson can be permanently deleted from the database with the **Delete** button on the frontend. The modal's content after clicking on **Delete** on a lesson, informs the site admin about which of the two it will be.

#### Date range (unfixed)
I wanted to give the user the possibility to show lessons within a specified date range. I found *DateFromToRangeFilter* which should work with my DateTimeFields, but I could not get it to work. Hence the user story *As a site user, I can select a date range in which I want to see offered lessons so that I can easily adapt the list of lessons on dates I can attend* could not be omplemented. It is a *could have* story, because users can scroll, so it is up to the site admin to not have lessons published over too large of a date span. The real life case this project was based on, Matchi, also does not have this date range selection per venue, only when lessons from all venues are listed. Example [here](https://www.matchi.se/facilities/salk), when you scroll down to *Activities*.

#### Lesson images
I wanted to have images with the lesson, even though it is not neccesary. So I did not want to give the user the possibility of uploading an image, as it is not neccessary, but I still want to give some choice to the user in which image will be used. So I fount this interesting option of using choices (https://stackoverflow.com/questions/31948172/python-django-form-where-user-selects-from-a-list-of-images, by Pynchia), which seemed easy and enough for the MVP. To make this work, I also followed the instructions of Melvyn Sopacua here (https://groups.google.com/g/django-users/c/iP2TmUHwdDI). 

#### Whitespace validation
The **Add lesson** form has the CharField **Name** and TextField **Description**. They are requered fields, but when I tested to fill in white spaces and click **Add lesson**, it did not give an error. I searched for this issue and found that Django does allow Char- and TextFields to have an empty string even if they are required (i.e. https://forum.djangoproject.com/t/charfield-not-enforcing-null-constraint/35127). So I looked at a solution with customising the form field for these two fields, adding a validator to check for a minimum length of 1 (*validators=[MinLengthValidator(1)]*). But this did not change anything. I then retested the form and treid to fill in the other fields and whitespaces in the **Name** and **Description** field, and then I actually got errors on those fields that they are required. So apparently, these errors are not triggered when most of the fields are empty, but they are triggered when a few are empty.

#### Profile image
The checkbox to remove an image on the **My profile** page, had an issue when I tried to change the background colour when checked. It stayed blue when selected, I suspect this has something to do with bootstrap. In the Chrome devtools, the correct background colour was set on the element when I selected this checkbox, but it was actually blue. Even though I managed to override it in the checkout form to green, I did not manage to change it to red in the profile. So I changed this element to a white background with red text, like I have used in the checkout form as well.

Because my image solution is different than in the walkthrough, which has different views for adding and editing, I had an issue since updating and adding the image is in one and the same view, and I needed to refresh the page to see the remove checkbox, or to see it removed when it should not be there. So I tried with JavaScript to toggle this checkbox without the need of refreshing the page, but that did not work. In the end, a simple redirect to profile url fixed this issue, now the remove option is gone directly after removing an image, and it is added directly after adding an image, without the need for manually refreshing, since it is already done automatically.

Something that caused some concern is that if a user would upload a very large image, this would need to be cropped down by the website to display, which I knew causes performance issues. So I found the same concern [here on Slack](https://code-institute-room.slack.com/archives/C026PTF46F5/p1674207577510609?thread_ts=1674167504.408779&cid=C026PTF46F5), and there was a very simple solution with the use of *transformation* to make sure an image would be cropped before it would be saved in Cloudinary.

#### Card error width
By accident, when I put a card number starting with 42424242 but but still not the correct test number from Stripe, I got a long error on the **Checkout** page which changed the whole form. So I set media queries on all fields there to keep the original widths, so now nothing changes when this large error comes up.

### Full testing


#### Browser testing

#### Device testing

Tested extensively on a Dell laptop, and on a Lenovo laptop, and Huawei phone. All works well.

#### Feature testing
|Feature|Expected outcome|Testing performed|Result|Pass/Fail|
| :--- | :--- | :--- | :--- | :--- |
|Navbar|
|Navbar links when logged out|**Log in** and **Register** appear when not logged in|Made sure I am logged out and clicked the links|The links appear and go to the correct pages|Pass|
|Navbar links when logged in as user|**Log out** and **My profile** appear when logged in|Made sure I am logged in and clicked the links|The links appear and go to the correct pages|Pass|
|Navbar links when logged in as admin|**Add lesson**, **Log out** and **My profile** appear when logged in|Made sure I am logged in and clicked the links|The links appear and go to the correct pages|Pass|
|Navbar links to Home|**Home** is always visible, both **Home** and logo go to first home page|Clicked the links|Logo and **Home** go to (first) home page|Pass|
|Navbar cart icon and total|Shows total of lessons in cart, shifts from grey to green when there are lessons, links to **Cart** page|Logo and **Home** go to (first) home page|Pass|
|Home page|
|**Private lessons** and **Group lessons** buttons|Starts roling when you initiate yourself|Made sure I am logged out and clicked the links|The links appear and go to the correct pages|Pass|
|Carousel|Starts roling when you initiate yourself|Made sure I am logged out and clicked the links|The links appear and go to the correct pages|Pass|
|Footer|
|Footer|Links to social media opening in new tabs|Clicked links in footer|Links open in new tabs|Pass|
|**All lessons** page|
|Lesson filtering|Lessons filter according to the **Private lessons** and **Group lessons** buttons on home page, and the **Group - Indoor**, **Group - Outdoor**, **Private - Indoor** and **Private - Outdoor** buttons on this page||Pass|
|Header text adjusts to filter|Header text changes according to which of the filter buttons is clicked||Pass|
|**Add to cart** button adds lesson to cart|Header text changes according to which of the filter buttons is clicked||Pass|
|**Add to cart** button gets disabled when lesson is full|Button changes text to **Not bookable** and gets disabled||Pass|
|Can not add same lesson more than once|When clicking **Add to cart** on already added lesson, you get a message and the lesson is not added to the cart||Pass|
|**Places_left** decreases after each order|After an order, **Places_left** decreases with 1, until 0|Complete payments to create orders via normal pay flow and via webhook, check updated value for **Places_left**|Pass|
|**Cart** page|
|Lessons appear|If you have added lessons, they are here and there is a button to pay, if not, there is a text saying there are no lessons and a link to go back to all lessons||Pass|
|Lessons that have become fully booked but were in a user's cart are removed|When you go to the cart and there is such a lesson, this is removed and there is toast message to inform the user|I added lessons to the cart and afterwards, I manually changed the **Places left** field to 0 for one lesson, then I went to the cart to check|Pass|
|**Checkout** page|
|Lessons from cart are in the overview|If you have added lessons, they are here and there is a button to pay, if not, there is a text saying there are no lessons and a link to go back to all lessons||Pass|
|Not possible to pay for unbookable lessons|If you have passed the cart view and filled in the checkout url, any unbookable lessons that you had in the cart are removed and you are moved back to the **Cart** page with updated cart and feedback message|I added lessons to the cart and afterwards, I manually changed the **Places left** field to 0 for one lesson, then I wrote in the checkout url page, and I got redirected straight back to the cart with the toast message to inform about the removed lesson|Pass|
|If logged in, you can select to save phone number, if not logged in, you are advised to log in or register to save the information in the form|||Pass|
|Stripe integration|The test card numbers from Stripe give the expected result||Pass|
|Webhook order creation|An order is created when payment is received in Stripe, not depending on the checkout success page.|Comment out form submit line in stripe_elements.js, and proceed to complete an order. The website hangs but the order is created.|Pass|
|**Back to cart** button|You can go back to the **Cart** page||Pass|
|**Checkout success** page|
|After payment, the user is referred to the **Checkout success** page|||Pass|
|**Order confirmation** email|
|After payment, the user gets a confirmation email|||Pass|
|**Register** page|
|The **Register** page is only visible when a user is not logged in|||Pass|
|When you register, you need to confirm your email|||Pass|
|**Log in** page|
|The **Log in** page is only visible when a user is not logged in|||Pass|
|After confirming your email from the registration step, you can log in with your username and password|||Pass|
|**Log out** page|
|The **Log out** page is only visible when a user is logged in|||Pass|
|After you click **Log out**, you are logged out|||Pass|
|**My profile** page|
|A logged in user can go to **My profile**|||Pass|
|You can add, edit and delete a phone number, a self-rated level, and a profile image|||Pass|
|If you had selected to save your phone number in the checkout page, it is updated in the profile|||Pass|
|You can find your booking history and go to old order confirmations|||Pass|
|You can go back to your profile form the old order confirmations|||Pass|
|Add lessons when logged in as site admin|
|**Add lesson** page is visible only for site admins|||Pass|
|When you fill in the required fields and submit the form, the lesson is added to the **All lessons** page|||Pass|
|Lessons with passed date are not visible on the **All lessons** page|||Pass|
|When **Places left** is not filled in, it is set to the same as **Capacity**|||Pass|
|Toast message when **Places left** is set to higher value than **Capacity**|||Pass|
|Toast message when **Date** is in the past|||Pass|
|Form validation|||Pass|
|Edit lessons when logged in as site admin|
|**Edit** button is visible on each lesson card only for site admins|||Pass|
|Toast message when editing and specifically when editing a lesson that has been booked|||Pass|
|The form is prefilled with the current lesson information|||Pass|
|Form validation|||Pass|
|Same messages and unctionality as **Add lesson**|||Pass|
|Edited lesson is updated on the **All lessons** page|||Pass|
|Delete lessons when logged in as site admin|
|**Delete** button is visible on each lesson card only for site admins|||Pass|
|**Delete** button opens modal for confirmation|||Pass|
|Modal text depends on whether or not a lesson has been booked before|||Pass|
|When you delete a lesson that has been booked before, it will only be removed from the website. It is still visible in admin, as well as the connected orders lines. When the connected order lines are removed, the lesson can be deleted from the database.|||Pass|
|A lesson that has not been booked before, will be deleted from the database|||Pass|
|Toast messages confirm deletion or permanent deletion|||Pass|
|Toast messages|
||||Pass|




















#### Unfixed bugs
You can not add a lesson to the cart more than once, but if you complete the purchase, you can add the same lesson to the empty cart and pay for it again. I left this like it is, because not a lot of people will force themselves to pay for the same lesson twice by actively adding the lesson to the cart again. If they would, it would be their mistake and they can contact Court Love to cancel it.

Related to this, also when an order is created via the webhook, the lesson remains in the cart. This means that a user can book it again, even if it is not allowed to book the same lesson more than once. But the user does get the order confirmation email, so it is unlikely someone would try to book it again and pay again.


There is another unfixed issue which is when something goes wrong when creating an order via a webhook, and the order is deleted after an updated lesson with a new **Places left** value is saved, this would not be reversed. The reason for this is that I can not test this situation at this point, so I would rather not add any code that could break the webhook flow.
