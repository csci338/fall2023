---
layout: module
title: "Activity: Background Images"
type: activity
draft: 1
---

<style>
    .tips td:first-child, .tips th:first-child {
        width: 200px;
    }
</style>

Please download the exercise files (below).

<a href="/fall2023/course-files/activities/background-media.zip" class="nu-button">Download Activity Files <i class="fas fa-download"></i></a>

## 1. Uncomment the relevant CSS properties
Open `in-class-exercise` and take a look at the HTML and CSS files to get oriented with them. Then, before making any changes to the code, preview the `index.html` page in your web browser.
    
After previewing your webpage, **uncomment** the following lines inside your `styles.css` file within your `header` style block. 

```css
  /* background-image: url('solar-eclipse.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position-x: center;
    background-position-y: center; */
```

When you're done, preview the page, noting what changed. You should now see a background image in your `header` of a solar eclipse.

Next, uncomment the following lines within your `#section2` style block:

```css
/* background-image: url('solar-eclipse-multiples.jpg');
background-repeat: no-repeat;
background-position: center right;
background-size: contain;
background-attachment: fixed; */
```

When you're done, preview the page. You should now see a background image of a series of photos of an eclipse behind a box of white text. The image should be anchored as you scroll. 
* Note that if you remove the `background-attachment: fixed;` declaration, the background image will move with the scroll bar (no anchoring). Try it!

## 2. Add Custom Images
Customize this page with your own background images.

* If you're looking for free images, check out: 
    * <a href="https://www.pexels.com/" target="_blank">pexels.com</a>
    * <a href="https://unsplash.com/" target="_blank">unsplash.com</a>
    {:.compact}
* When you've found some images that you like, save them inside of the `in-class-exercise` folder, and update the background-image file paths to point to your files. 
* If you want to explore some of the other background properties, take a look at <a href="https://www.w3schools.com/cssref/css3_pr_background.asp" target="_blank">W3 Schools</a>


## 3. Try Out the Filters
If you have time, also try playing with some of the background filters. Here is a <a href="https://www.w3schools.com/cssref/css3_pr_filter.asp" target="_blank">list of available filters</a> (also on W3 Schools).  The options for the filter property are:

* none
* blur()
* brightness()
* contrast()
* drop-shadow()
* grayscale()
* hue-rotate()
* invert()
* opacity()
* saturate()
* sepia()
* url()
{:.compact}

Hint: try adding `filter: invert(180);` to the `header` style block in your CSS file to see what happens.


## 4. Try adding a video background
* Take a look at the video background sample files and see if you can add a section somewhere on the page that has a video background.
* Both <a href="https://www.pexels.com/search/videos/background%20videos/" target="_blank">pexels.com</a> has some free video backgrounds that you can download.

