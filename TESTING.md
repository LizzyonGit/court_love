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

### Python validator

### Javascript validator

### Lighthouse testing



## Manual testing


### User story testing

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



