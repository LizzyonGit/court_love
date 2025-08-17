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

### Favicon testing

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
# capacity handler (https://stackoverflow.com/questions/61310901/how-to-update-a-value-from-table-accessed-via-foreign-key-django-orm)
                    # this does not work as the capacity model is changed, it should not. I should change this to a normal field I think. Or have new field in lesson with capacity left that gets updated?






10:27
So first I wanted to use the same field but it was better with a separate field.


Lizzy_4P
  3:11 PM
delete order line item in checkout when places left is 0, did not work I got an error message. so I moved it to the card instead, also changed the direclyt to chekout to go to cart.


Lizzy_4P
  11:24 AM
works good in checkout, but you can go to the cart and see the item there again. but you cant checkout with it
11:29
could add same code to cart view?


Lizzy_4P
  11:50 AM
I put correct code in cart and removed from chekout. Also, in the toast I changed so that you have to go to cart first, so chekout get the updated cart. Now there is an issue if the user would use the chekout url and not go viacart...


Lizzy_4P
  11:58 AM
i put a code in chekout that it goes back to cart incase there is a lesson with 0


Lizzy_4P
  11:05 AM
now you can comple purchase and then add same lesson and pay again. Unfixed bug. But however, not a lot will force themselces to pay twice :)

#### Delete functionality
I had implemented the same delete functionality as in Boutique Ado, but faced issues accessing orders containing only deleted lessons. Opening order lines with a deleted lesson or orders with only deleted lessons resulted in a 500 error in admin. I tried to change the OrderLineItem model setting deleted lessons to Null, but this did not fix it. So I went for a 'soft delete', as suggested on [Stackoverflow](https://stackoverflow.com/questions/42954063/storing-products-in-order-product-is-deleted-after-order-placed). So now from the frontend, site admins can delete a lesson but it will just set the *deleted* field to True, and it will not appear on the website. The site admin will still receive a notification when deleting a lesson that already has been booked before, so they can go to admin and find the order and user details to inform the user about the deletion. They simply go to Order line items, find the order line items with the delete lesson, and go to the orders via the eye ball on the order line item pages.

To prevent issues when a site admin 'hard deletes' a lesson in admin, I set *on_delete=models.PROTECT* for the lesson foreign key on the OrderLineItem model, so site admins should first manually delete order lines/orders if they want to delete a lesson. 

But then I realised that this may not fulfill the CRUD functionality, so in the end, I opted for a combination of the two. When a lesson has been booked, the site admin can not remove it from the database before deleting the connected orders in admin. But when there are no connected orders, the lesson can be permanently deleted from the database with the **Delete** button on the frontend. The modal's content after clicking on **Delete** on a lesson, informs the site admin about which of the two it will be.

#### Date range (unfixed)
Lizzy_4P
  12:35 AM
DateFromToRangeFilter did not work, I could not get it to work, so I remove django_filters and did something else. User story: as a site user, I can select a date range in which I want to see offered lessons so that I can easily adapt the list of lessons on dates I can attend. could have, since people can scroll






12:37
And there will not be super many lessons out there

#### Lesson images
I wanted to have images with the lesson, even though it is not neccesary. So I did not want to give the user the possibility of uploading an image, as it is not neccessary, but I still want to give some choice to the user in which image will be used. So I fount this interesting option of using choices (https://stackoverflow.com/questions/31948172/python-django-form-where-user-selects-from-a-list-of-images, by Pynchia), which seemed easy and enough for the MVP. To make this work, I also followed the instructions of Melvyn Sopacua here (https://groups.google.com/g/django-users/c/iP2TmUHwdDI). 

#### Whitespace validation
The **Add lesson** form has the CharField **Name** and TextField **Description**. They are requered fields, but when I tested to fill in white spaces and click **Add lesson**, it did not give an error. I searched for this issue and found that Django does allow Char- and TextFields to have an empty string even if they are required (i.e. https://forum.djangoproject.com/t/charfield-not-enforcing-null-constraint/35127). So I looked at a solution with customising the form field for these two fields, adding a validator to check for a minimum length of 1 (*validators=[MinLengthValidator(1)]*). But this did not change anything. I then retested the form and treid to fill in the other fields and whitespaces in the **Name** and **Description** field, and then I actually got errors on those fields that they are required. So apparently, these errors are not triggered when most of the fields are empty, but they are triggered when a few are empty.

#### Profile image
remove checkbox in image selection, very weird that it stayd vlue when selected. Something with bootstrap. In the devtools, the correct background colour was set, but it was actually blue. Even though I managed to override it in the checkout form to green, i did not manage to change it to red. So I redid it with a white background and red text.

because my image solution is different than in the walkthrough which has different views for adding and editing, I had an issue since updating hte image is in the same view, and I needed to refresh the page to see the remove button, or to see it removed. So I tried with javascript but that did not work. In the end, a simple redirect to profile url fixes this issue, now the remove option is gone directly after removing an image, and it is added directly after adding an image.

#### Card error width
By accident, when I put a card number starting with 42424242 but but still not the correct test number from Stripe, I got a long error on the **Checkout** page which changed the whole form. So I set media queries on all fields there to keep the original widths, so now nothing changes when this large error comes up.

### Full testing


#### Browser testing

#### Device testing

Tested extensively on a Dell laptop, and on a Lenovo laptop, and Huawei phone. All works well.

#### Feature testing

#### Unfixed bugs
You cannot add a lesson to the cart more than once, but if you complete the purchase, you can add the same lesson to the empty cart and pay for it again. I left this like it is, because not a lot of people will force themselves to pay for the same lesson twice by actively adding the lesson to the cart again. If they would, it would be their mistake and they can contact Court Love to cancel it.



