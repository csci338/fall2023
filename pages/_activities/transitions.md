---
layout: module
title: "Activity: Transitions"
type: activity
draft: 1
---

This in-class activity consists of 3 parts:

{:.compact}
1. [Experimenting with some transitions](#part1)
2. [Trying to implement one of the CSS Tricks](#part2)
3. [Experimenting with the ::before and ::after pseudo-classes](#part3)


Please download the exercise files (below).

<a href="/fall2023/course-files/activities/transitions.zip" class="nu-button">Download Activity Files <i class="fas fa-download"></i></a>


{:#part1}
## 1. Experimenting with Transitions

{:.blockquote-no-margin}
> ### Relevant References
> * <a href="https://css-tricks.com/pseudo-class-selectors/" target="_blank">What are pseudoclasses?</a>
> * <a href="https://css-tricks.com/almanac/properties/t/transform/" target="_blank">The transform property</a>


### Uncomment the relevant CSS style blocks
Inside of the `in-class-exercise` folder, take a look at the HTML and CSS files to get oriented with them. Then, before making any changes to the code, preview the `index.html` page in your web browser.

After previewing your webpage, **uncomment** the following lines inside your `styles.css` style block:

```css
/*
#section1 {
    background: #0c7474;
    color: white;
    transition: all 0.3s ease-out;
}

#section1:hover {
    background: purple;
    width: 220px;
    height: 220px;
}
*/
```

When you're done, preview the page, noting what changed. When you hover over the first section, you the section should grow and change color (horray)! 

### Create two more transition effects

Your job is to experiment with the other two section tags (`#section2` and `#section3`) by making some interesting interactions, using transitions. Some tips:

1. To make a <a href="https://www.w3schools.com/css/css3_transitions.asp" target="_blank">transition</a>, you define a transition inside of a style block (e.g., `#section1`) as follows: `transition: <property> <duration> <timing-function> <delay>;` Examples:
    * transition: all 0.3s ease-out;
    * transition: background 1s ease-in;
    * transition: all 3s linear;
    * transition: all 0.3s ease;
    {:.compact}
2. Some properties that you may want to change:
    * border-radius
    * margin
    * padding
    * width
    * height
    * border-width
    * background-color
    * rotation
    * opacity
    * <a href="https://www.w3schools.com/css/css3_2dtransforms.asp" target="_blank">transform</a>. Examples<br>transform: skewX(20deg);<br>transform: rotate(-10deg);
    {:.compact}

Feel free to look at `sample-files/01-pseudo-classes` and `sample-files/02-pseudo-classes-with-transitions` to get ideas.

{:#part2}
## 2. Implement one of the CSS Tricks Effects

{:.blockquote-no-margin}
> ### Relevant References
> * <a href="https://css-tricks.com/css-link-hover-effects/" target="_blank">CSS link hover effects</a> + <a href="https://codepen.io/vanwars/pen/ExeNEWN?editors=0100" target="_blank">CodePen</a>
> * <a href="https://css-tricks.com/4-ways-to-animate-the-color-of-a-text-link-on-hover/" target="_blank">CSS link hover effects: animated underline</a>
> * <a href="https://css-tricks.com/cool-hover-effects-that-use-css-text-shadow/" target="_blank">CSS link hover effects: getting creative with text shadows</a> + <a href="https://codepen.io/vanwars/pen/rNZWdGM?editors=0100" target="_blank">CodePen</a>

When you're done with parts 1-2, please try experimenting with hyperlink hover effects. Recall that hyperlinks have several relevant states that you want to style:

{:.compact}
* a
* a:link
* a:hover (the main interactive state)
* a:focus (if the person tabs to the link)
* a:visited (if you want the style of visited links to look different)
* a:active (if you want a different style when the person clicks the link)

Click on some of the "CSS Tricks" links above, and see if you can implement one of the techniques that you find interesting.


{:#part3}
## 3. selector::before and selector::after pseudo-classes

If you have time, try to implement a "before" or an "after" pseudo-class on an eleement. See the `sample-files/01-pseudo-classes` folder for some examples (or you can copy in the example and then adapt it).
