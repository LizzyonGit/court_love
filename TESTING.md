# Court Love - Testing

[Live link to website](https://court-love-8302d0b2e53d.herokuapp.com/)


## Automated testing


### HTML validator

### CSS validator

### Python validator

### Javascript validator

### Lighthouse testing



## Manual testing


### User story testing

### Issues
#### Lesson images
I wanted to have images with the lesson, even though it is not neccesary. So I did not want to give the user the possibility of uploading an image, as it is not neccessary, but I still want to give some choice to the user in which image will be used. So I fount this interesting option of using choices (https://stackoverflow.com/questions/31948172/python-django-form-where-user-selects-from-a-list-of-images, by Pynchia), which seemed easy and enough for the MVP. To make this work, I also followed the instructions of Melvyn Sopacua here (https://groups.google.com/g/django-users/c/iP2TmUHwdDI). 

#### Whitespace validation
The **Add lesson** form has the CharField **Name** and TextField **Description**. They are requered fields, but when I tested to fill in white spaces and click **Add lesson**, it did not give an error. I searched for this issue and found that Django does allow Char- and TextFields to have an empty string even if they are required (i.e. https://forum.djangoproject.com/t/charfield-not-enforcing-null-constraint/35127). So I looked at a solution with customising the form field for these two fields, adding a validator to check for a minimum length of 1 (*validators=[MinLengthValidator(1)]*). But this did not change anything. I then retested the form and treid to fill in the other fields and whitespaces in the **Name** and **Description** field, and then I actually got errors on those fields that they are required. So apparently, these errors are not triggered when most of the fields are empty, but they are triggered when a few are empty.

### Full testing


#### Browser testing

#### Device testing

Tested extensively on a Dell laptop, and on a Lenovo laptop, and Huawei phone. All works well.

#### Feature testing

#### Unfixed bugs
