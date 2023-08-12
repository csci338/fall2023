---
layout: two-column
title: Final Exam (JavaScript)
draft: 1
points: 20
due_date: 2023-02-10
---

<style>
    img.preview {
        max-width: 60%;
        min-width: 500px;
    }
</style>


<a href="/fall2023/course-files/exams/final-exam.zip" class="nu-button">Download Starter Files <i class="fas fa-download"></i></a>

## Required: DOM Manipulation
Open the `exercise01` folder and add click event handlers to all of the div tags. When a div element is clicked, its background should change color (pick any color you like). When you’re done, your page should look like the demo shown below:


<img class="medium frame" src="/fall2023/assets/images/quizzes/quiz03/exercise01.gif" />


## Optional: Functions & Loops

{:.blockquote-no-margin}
> If you're worried about the paper portion of the exam and would like to show your JavaScript knowledge via code, try implementing the following task described below. Completing this task won't count against you, but will help your score if you accidentally messed up a a question in the paper-based exam.


Open the `exercise02` folder and examine all of the files. Inside of `main.js`, there is a `fetchCourses` function (already built for you) that fetches all of the UNCA course offerings for Spring, 2023: (<a href="https://meteor.unca.edu/registrar/class-schedules/api/v1/courses/2023/spring/">here</a>). Note that by modifying the year or term in the URL string, you can also view course offerings from previous semesters. 

### Your job
1. Modify the *function body* of the `displayResults(courses)` function so that it outputs to the `#results` element only courses that offered within the **CSCI department.** You may use any kind of loop that you like.
2. Ensure that your HTML snippet displays the following information for each course (using a template literal like we did in `HW7`):
    * Title
    * Instructor
    * Location
    * Days (i.e., which days does the course meet?)
3. Location and Days may be `null`. That's OK for this exercise (though in real life, you'd probably want to output a friendlier message).

<img class="large frame" src="/fall2023/assets/images/quizzes/quiz03/exercise03.png" />

**Hints**
* Loop through the `courses` array.
* If the current course's `Department` property is "CSCI", then insert an HTML representation of the course into the `<div class="results"></div>` container. 
* Partial credit will be given.
* We went over this in Lectures 22-24 (and there are lecture videos that you can even follow along with).
* A sample of the HTML representation of a course is shown below, and also in `exercise03/template.html`:

```html
 <section class="course">
    <h3>NM 101.001: Digital Design Principles</h3>
    <ul>
        <li>Instructor: Cosette, Ashe</li>
        <li>Location: OWE 305</li>
        <li>Days: MW</li>
    </ul>
</section>
```

## What to Submit
**Please read carefully:** Doublecheck your work to make sure you've completed the first task (the second task is optional). Then, update your homepage by adding a link to `javascript-exercises/exercise01` (required) and a link to `javascript-exercises/exercise02` (optional). Sarah's final exam looks like this: <a href="https://vanwars.github.io/csci185-coursework/" target="_blank">https://vanwars.github.io/csci185-coursework/</a>

After committing and syncing your changes to GitHub, paste the following links into the Moodle under the Final Exam submission section:

1. A link to your **homepage** on GitHub pages.
2. A link to your GitHub **code repository** (where your code files are stored).

If your GitHub is not working for whatever reason, just zip your **COMPLETED** `final-exam` folder and upload it to the Moodle.