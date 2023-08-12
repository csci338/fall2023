---
layout: module
title: "Activity: Keyframes"
type: activity
draft: 1
---

Please download the exercise files (below) and attempt one or more of the following exercises.

<a href="/fall2023/course-files/activities/keyframes.zip" class="nu-button">Download Activity Files <i class="fas fa-download"></i></a>

## Cheatsheet

| **Property** | **Description** |
|--|--|
| **animation-name** | Name of the keyframe you defined.
| **animation-timing-function** | e.g., linear, ease-in, ease-out |
| **animation-delay** | how long to wait before animation starts | 
| **animation-iteration-count** | How many times animation should repeat | 
| **animation-direction** | normal, reverse, alternate, alternate-reverse | 
| **animation-fill-mode** | e.g., forwards, backwards, normal, both (what to do when the animation stops) | 
| **animation-play-state** | e.g., paused, running | 


## Exercise 1: Landscape
See if you can create a landscape animation:

### Uncomment the relevant CSS style blocks
Inside of the `your-task` downloads folder, open `03-keyframes`, and take a look at the HTML and CSS files to get oriented with them. Then, before making any changes to the code, preview the index.html page in your web browser. You should see one cloud moving from left to right.

After previewing your webpage, **uncomment** the following two code blocks inside your `styles.css`:

Inside of #sun:
```css
/* animation-timing-function: linear;
    animation-fill-mode: forwards; 
    animation-name: sunrise;
    animation-delay: 1s;
    animation-duration: 12s; */
```

Also comment out the corresponding keyframe that controls the sunrise:
```css
/* @keyframes sunrise {
    0% { 
        transform: translate(0, 0);
    }
    100% { 
        transform: translate(0, -70vh); 
    }
} */
```

When you’re done, preview the page, noting what changed. You should now see a second cloud moving from right to left.

### Play around with the existing animation

1. Try experimenting with the `animation-delay`, `animation-duration`, and `animation-timing-function` (ease-in, ease-out, ease, etc.) to change the speed and timing of the animation.
2. See if you can make the sun change from orange to yellow as it rises. 
3. See if you can make the size of the sun change as it rises.
    * Hint: Add some additional style rules to the `to {}` block of the `sunrise` keyframe.

### Make one of the clouds move
See if you can make `#cloud1` animate from left to right. To do this, **uncomment** the following two code blocks inside your `styles.css`:

Within the `#cloud1` selector:

```css
/* transform: translate(-30vw, 0); */

/* animation-timing-function: linear;
animation-iteration-count: infinite; 
animation-direction: alternate;
animation-name: moveCloudHorizontally;
animation-delay: 1s;
animation-duration: 18s; */
```

Also comment out the corresponding keyframe that controls the cloud movement:

```css
/* @keyframes moveCloudHorizontally {
    0% { 
        transform: translate(-30vw, 0);
    }
    100% { 
        transform: translate(110vw, 0); 
    }
} */
```

See what happens.


### Add more clouds
See if you can add more clouds that move in different directions and at different speeds.

<img src="/fall2023/assets/images/activities/keyframes/landscape-animation.gif" alt="image of the animation" />

## Exercise 2: Experimenting with keyframes on your homepage
See if you can add a keyframe hover effect (like the ones) in `sample-files/02-heart-infinite` or `sample-files/03-spin-activate-on-hover` in your homepage.