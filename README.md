# Photon Language 

## Introduction 

Photon is a high-level programming language designed for simplicity and versatility. It combines elements from Python, JavaScript, TypeScript, and CSS to provide a familiar yet powerful programming experience. Photon is heavily object-oriented, offering intuitive syntax for interactions with the console, memory, desktop, and web.

### Key Features:
- **Object-Oriented:** Photon emphasizes object-oriented programming paradigms, making it easy to organize and manipulate data.
- **Intuitive Syntax:** Inspired by JavaScript, Python, and TypeScript, Photon offers a familiar syntax for developers.
- **Console Interaction:** Easily interact with the console using intuitive methods like `console.display("Hello World")`.
- **Memory and Desktop Manipulation:** Photon provides simple yet powerful methods for interacting with memory and desktop elements, such as `ram.display("address")` and `desktop.background("image.png")`.
- **Web Integration:** Interact with web resources seamlessly with built-in methods like `web.load("https://example.com")`.

Photon aims to streamline the development process by providing a language that is easy to learn, yet capable of handling complex tasks efficiently. Whether you're a beginner or an experienced developer, Photon offers the tools you need to bring your ideas to life.

# Photon Documentation

## Initialize workspace
When you have import all the repository on your workscpace you can start code. For simplify all you can download extension : https://marketplace.visualstudio.com/items?itemName=SkyDeveloppement.photon-extension .
For more information on them go to the documentation of the extension.
For benning you must create a file .photon for example "main.photon" and you must initialize the file photon-pack.json which is used by interpreter for many reason. For initialize them write and execute command in a terminal : 
```
start PhotonIDE/init.bat
```
Now you must custom photon-pack.json :
```
{
    "code" : {
        "file" : ["main.photon"], // Where, write the file where you want code
        "version" : "1.0.0", // No modif
        "console" : true, // If you want a console app
        "app" : false, // If you want a dev an app with a window
        "web" : false, // If you want a dev a website
        "subprocess" : false // If you want a dev a process for your computer
    },
    "IDE" : { // No modif
        "version" : "1.0.0", 
        "ID" : "Alpha",
        "kit" : "Devkit6 - 1.0.0"
    },
    "Library" : {
        // Write the library that you want
    },
    "Import" : [], // Write the script and file that you want import
    "Database" : {
        // Write the database that you want import
    }
}
```
When you want execute your code write the command in a terminal :
```
start PhotonIDE/photon.bat
```

Now you are ready for coding !!!

## Basics
The Console
Display messages in the console using:
```
console.display("Hello World!")
```
## Variables
Photon supports several types of variable declarations:

- **const**: For declaring a constant variable whose value cannot be changed.
- **let**: For declaring a variable whose value can be changed.
- **var**: For declaring a variable with a broader scope.
- **secure**: For declaring a secure variable that can only be modified with a specific key.
Examples
```
const pi = 3.14; // A constant for the value of pi
let age = 25; // A variable that can change, such as a person's age
var score = 0; // A global variable for a score in a game
secure password = "myPassword"; // A secure variable for a password
```
