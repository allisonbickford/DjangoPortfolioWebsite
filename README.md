# DjangoPortfolioWebsite

This is a porfolio website for my coding projects. Ideally this will be a functioning website that can display my work to potential employers, evenutally using a host. I'd like to include my finished projects from github as well as a basic "About" and "Contact" page. 

## Home

Now that I've been working on the home page for a while, I've learned a lot about Django and its compatibilities with other languages and files. I will do my best to record any findings related to these.

### Handwriting Animation

This animation took me **forever** to get right, and the solution involved a free trial of Illustrator. I tried using Inkscape and I wish I could've found a solution so I could share it, but the SVG ended up being super bloated and unusable. I was able to draw outlines, but I couldn't get a filled animation like the one on my main page. SVG animations like this one are extremely powerful for website design, and learning how to create this animation can help understand how to create many others. I referenced lots of guides, but mainly [this one](https://youtu.be/DOv6eYgCSz4).

### Border Hover Animation

Originally I used a border hover animation by using a shadow. Here is a quick implementation:

```     
.preview-option {
        border-style: solid;
        transition: box-shadow 0.6s linear;
}

.preview-option:hover {
        border-color: #ff9933;
        box-shadow: 0px 0px 0px 5px #ff9933;
}
```

### jQuery

Currently my project does not use jQuery, but these instructions could still be useful.

Having never used jQuery, it seemed like the most robust solution for what I needed, and it looked so simple. But getting it to work with my app was much less simple. Here are the steps that I used to get jQuery working with Django:

1. ```$ pip install django-jquery``` 
(use pip3 for python3, or at least that's what I did)

2. add ```'jquery'``` to "INSTALLED_APPS" in "<your_project_folder>/settings.py"

3. in "settings.py", add ```STATIC_ROOT = '<app_name>/static'``` and ensure the file contains ```STATIC_URL = '/static/'```. This will make it easier to reference JavaScript files in your static folder. However, this will place the JavaScript library in your app's static folder. I suppose you could relocate this if you so desired.

4. ```$python manage.py collectstatic``` this will place the JQuery file in your specified folder above. It will also create some folders and prompt you for changing your files. It did not change any files I had in "/static/<app_name>/", but backing up any js or css file would be a good idea.

5. ensure ```{% load static %}``` is in your template file. Then, you will need the following line to make your jQuery work (this what fixed my issues):
```<script type="text/javascript" src="{% static 'js/jquery.js' %}"></script>```
"js" is the folder that contains your jquery library, and "jquery.js" should be a really complicated looking file. Now jQuery's will work, granted they're placed in <script> tags. I referenced my external javascript file (named "change_preview.js") with this line:
```<script type="text/javascript" src="{% static 'main_content/change_preview.js' %}"></script>```
  
This is what made my jQuery work, but make sure to include ```$(document).ready(function () {...}``` otherwise jQuery will never understand that your page has loaded and therefore will never run. When I was researching my jQuery not running, this was the most common issue for others.

Note: when using jQuery to replace html, I simply concatonated the tags in quotes to data attributes in my html. I found this was the best way to avoid using django template language variables and html in jQuery (not that it works anyway, but if you wanted to use it, put your django stuff in single quotes). I had an issue where I couldn't name html data attributes to certain things, like "data-description" (so I used "data-text" instead). This line might be useful for anyone attempting to mix html and jQuery:
```$(".project-preview").html("<h2>"+$(this).data('title')+"</h2><p>"+$(this).data('text')+"</p>");```

Note 2: When using addClass() or removeClass() in jQuery, don't use the "." that would normally be included in lines like ```$(".myclass")``` in the parameter. Instead it looks like ```$(".myclass").removeClass("myclass")```. Notice the use of periods.

## About

This page includes a brief description of my current professional state. This will include basic HTML tags to organize it, most likely not using much CSS styling. I still haven't decided on the styling, but I want to make it more interesting to look at.

## Projects

This should include a brief description of each project, and an ability to navigate to each project's respective detail page.

### Project Details

Project details will include the project title, link to repository, and any interesting information, like code snippets or useful processes. As I work on more projects, I'd like to include more detailed information about progress during each project. 

## Contact

This will be form to email me at my school email. I would like to avoid using my personal phone number on this page, and potential employers will most likely have my number anyway. Still, I think this would be a useful addition for now. It might prove to be unneccesary and may be replaced with a blog later.
