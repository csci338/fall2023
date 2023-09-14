---
layout: assignment-two-column
title: "Writing Tests in JavaScript & Python"
type: lab
draft: 1
points: 6
abbreviation: Lab 4
num: 4
start_date: 2023-09-19
due_date: 2023-09-24

---

## 1. Reading & Reference Materials

* <a href="https://circleci.com/blog/unit-testing-vs-integration-testing" target="_blank">High-level overview of unit v. integration testing.
* <a href="https://abseil.io/resources/swe-book/html/ch11.html" target="_blank">Chapter 11. Testing Overview</a>
* <a href="https://programmingwithmosh.com/wp-content/uploads/2019/02/Python-Cheat-Sheet.pdf" target="_blank">Python Reference</a>
* <a href="https://quickref.me/javascript.html" target="_blank">JavaScript Reference</a>

## 2. Introduction & Background
In this lab you will be doing a few things:
1. Pulling down the latest changes from the main branch of the <a href="https://github.com/csci338/class-exercises-fall2023" target="_blank">class-exercises-fall2023</a> repo.
1. Implementing a "rock paper scissors" function (described below) in both Python and JavaScript.
1. Writing "vanilla" unit tests for your "rock paper scissors" functions (in both Python and JavaScript).
1. Adapting the "vanilla" unit tests you wrote to a testing framework (in both Python and JavaScript).

## 3. Set Up
Navigate to your `csci338/class-exercises-fall2023` folder on the CLI.
Then check which branch you're on:

```bash
git branch
```

Check that all of your changes have been committed:

```bash
git status
```

If there are any modified files, stage and commit them:

```bash
git add .
git commit -m "some meaningful message"
```

Now switch to your main branch (if you're not already on it) and verify that you're on it:

```bash
git checkout main
git branch    # should be an asterik next to main
```

Pull down the new code for `lab04`:

```bash
git pull
```

Create a new branch from main (with the updated code files) called `lab04-your-username`, and verify that you're on the new branch:

```bash
git checkout -b lab04-your-username
git branch    # should be an asterik next to lab04-your-username
```

Finally, make a copy the `lab04` in your "username" directory. When you're done, you shoud have a folder structure that looks something like this in your folder:

```bash

class-exercises-fall2023
├── lab04           # original copy
...
└── your-username
    ├── README.md
    ├── getting-started-app
    └── lab04       # your copy -- you will edit the files in this folder
```

You will be editing the copy of `lab04` inside `your-username` folder. Please don't edit or delete the original files.

## 4. JavaScript Tasks
Please start by completing the JavaScript tasks, which are located in the `javascript_rps` folder (`rps` stands for "rock paper scissors").

### 4.1. Implement the "Rock Paper Scissors" function
Open `your-task.js` and take a look at the `rps` function, which should look like this:

```js
export function rps(hand1, hand2) {
    // finish this code:
    if (hand1 === "rock" && hand2 === "paper") {
        return "Paper wins!";
    } else {
        return "invalid";
    }
}
```

Your job is to implement the following logic and return the corresponding message (exactly as it is shown below):
* If one hand is **rock** and the other is **paper**, return the string **"Paper wins!"**
* If one hand is **paper** and the other is **scissors**, return the string **"Scissors wins!"**
* If one hand is **scissors** and the other is **rock**, return the string **"Rock wins!"**
* If both hands are the same (and have valid arguments), return **"Tie!"**
* If anything other than rock, paper, or scissors are passed in, return **"Invalid"**

### 4.2. Writing tests without a framework
As you are writing your `rps` function, write corresponding tests to verify your implementation for different possible arguments that a user might pass in. 

You will first write some tests **without** a framework. To help you, we have written two helper functions in `helpers.js`. The high-level point here is that anyone can write and run tests without using a fancy testing library. Please open the `run-tests-vanilla.js` file to inspect how these two helper functions are used. Pause and try and understand what this code does.

When you've thought about it, please run the test suite by navigating into the `javascript_rps` file and running the following command:

```shell
npm test
```

Your should see the following output:

```shell
> node run-tests-vanilla.js

----------------------------------------------------
✅ Success: it returns "Hello world!"
✅ Success: paper beats rock
❌ Failure: paper beats rock (flipped)
----------------------------------------------------

😬 Only  2 out of 3 tests passed.
```

To understand what the `npm test` command did, open the `package.json` file and see if you can see what the `npm test` command actually invoked.

Please write additional tests to ensure that all possible inputs yield the expected output. As you make new test functions, don't forget to add the name of the function definition to the list of tests that are passed into the `runAllTests` function (at the bottom of the file).


### 4.3. Writing rests with a framework (Mocha)
Now that you have implemented the `rps` function and written the corresponding tests using "vanilla" JavaScript, you are going to try rewriting your tests to use a JavaScript testing framework called Mocha. 

#### Install Mocha
Mocha offers a set of functions and objects that organize your tests and make them easier to define and write. It also requires that all tests be placed in a folder called `tests`. Install Mocha via the npm package manager by typing `npm install` on the CLI. This command reads the `package.json` file and installs all of the specified dependencies. Look at all of the dependencies that were just created! Is leftpad in there?


#### Run the mocha tests
To run the tests, you must do two things. First, modify `package.json` by setting the test value to "mocha" (instead of "node run-tests-vanilla.js"):

```json
"scripts": {
    "test": "mocha"
}
```

Second, issue the following command on the CLI from within the "javascript_rps" directory:
    
```
npm test
```

If you did it correctly you should see output that looks like the following:

```bash
> mocha



  Hello World Tests
    ✔ returns "Hello world!"

  Rock Paper Scissors Tests
    1) knows that paper beats rock


  1 passing (3ms)
  1 failing

  1) Rock Paper Scissors Tests
       knows that paper beats rock:

      AssertionError [ERR_ASSERTION]: 'invalid' == 'Paper wins!'
      + expected - actual

      -invalid
      +Paper wins!
      
      at Context.<anonymous> (file:///Users/svanwart/unca/csci338/fall2023/course-website/course-files/labs/lab04/javascript_rps/test/run-tests-mocha.js:60:16)
      at process.processImmediate (node:internal/timers:478:21)
```


#### Rewrite your tests using the Mocha conventions
Once you have successfully run the tests, open the `tests/run-tests-mocha.js` file and see if you can understand what's going on. Pause and think. What is the same and what is different?

After inspecting the code, please add new mocha tests to exhaustively test the `rps` function using the Mocha helper functions. Note that instead of your functions returning true or false, you need to use Node's built-in `assert` module. 

## 5. Python Tasks
When you've completed your JavaScript tasks, you're going to do the same thing all over again, using Python. The Python version of these files is located in the `python_rps` folder. Please navigate to it using your CLI.

### 5.1. Implement the "Rock Paper Scissors" function
Open `your-task.py` and take a look at the rps function, which should look like this:

```python
def rps(hand1, hand2):
    # finish this code:
    if hand1 == "rock" and hand2 == "paper":
        return "Paper wins!"
    else:
        return "Invalid"
```

Your job is to implement the function using the same logic as described above.


### 5.2. Writing tests without a framework
As you are writing your rps function, write corresponding tests to verify your implementation for different possible arguments that a user might pass in.

Like before, you will first write your tests without a framework. To help you, we have written two helper functions in `helpers.py`. Please open the `run_tests_vanilla.py` file to inspect how these two helper functions are used. Pause and try and understand what this code does.

When you’ve thought about it, please run the test suite by navigating into the `python_rps` folder and running the following command:

```bash
python3 run_tests_vanilla.py
```

You should see the following output:

```bash
python3 run_tests_vanilla.py
--------------------------------------------------
✅ Success: It returns "Hello world!"
✅ Success: Paper beats rock
❌ Failure: Paper beats rock (flipped)
--------------------------------------------------

😬 Only  2 out of 3 tests passed.
```

Please write additional tests to ensure that all possible inputs yield the expected output. As you make new test functions, don’t forget to add the name of the function definition to the list of tests that are passed into the `run_all_tests` function (at the bottom of the file).

### 5.3. Writing rests with a framework (unittest)

1. BACKGROUND / SET-UP
----------------------------------------------------------
The unittest module is part of the Python language, and
offers programmers a set of convenience functions and classes 
for organizing and writing tests.

Learn more here: https://docs.python.org/3/library/unittest.html 


2. YOUR TASK
----------------------------------------------------------
Below, a "starter" test class has been defined for you.
It includes two "starter tests" that you can use a model for 
writing your tests. Your job is to implement the remaining tests 
(based on the logic you already figured out from run_tests_vanilla.py).
Note that instead of having your functions return True or False, 
you will now need to use the unittest.TestCase methods. Examples:

    self.assertTrue
    self.assertEqual

List of possible methods described here: 
    https://docs.python.org/3/library/unittest.html 


3. RUNNING THE TESTS
----------------------------------------------------------
To run these tests, issue the following command on the CLI
(from within the python_rps directory):

    python3 run_tests_framework.py --verbose


## 6. What to Submit