import messages from "./message-module.js";

function assert(condition, message) {
    if (condition) {
        console.log("Success:", message);
        return true;
    } else {
        console.log("Failure:", message);
        return false;
    }
}

function testHelloWorld() {
    return assert(
        messages.helloWorld() === "Hello world!",
        "helloWorld() string works as expected"
    );
}
function runTests(allTests) {
    let successes = 0;
    allTests.forEach((test) => {
        successes += test();
    });
    console.log(successes, "out of", allTests.length, "succeeded.");
}

runTests([testHelloWorld]);
