


# Panther-Calculator

> This is the simplest calculator designed using Tkinter for Windows, Linux and OSX.

&nbsp;



<p align="center">
  <img src="https://user-images.githubusercontent.com/35782113/63217305-18228b80-c112-11e9-8691-b1aac19a10fa.png">
</p>


The calculator has the following keys: 0..9, ., +, -, *, /, //, %, =, ←, CE, exponent (^), square-root (√), pai (π), left Parenthesis, right Parenthesis. 
In any situation the calculator produce a correct result defined by the well known arithmetic rules. We also include a new operator called Floor-Division (//) which provide the integer quotient after division and remove the decimal part. 

If the calculations is impossible, the calculator will display information helping the user to resolve the erroneous situation, like:
- On encountering a "division by 0", the display will show "Cannot divide by 0" and typing the key “CE” will reset the calculator.
- On calculating the square root value of a negative operand, the display will read "Invalid Input".
- On erroneous operand or operation keys the display will read “Invalid Input”. 
- Of course, any situation can be cleared using the main reset key “CE”.


## Example 
&nbsp;


[![Calculator in use ](https://user-images.githubusercontent.com/35782113/63217308-18228b80-c112-11e9-9ecc-34ffa2aceda7.gif)]()

&nbsp;

You can use mouse click or keyboard key to press the key on the calculator interface.
&nbsp;

&nbsp;


&nbsp;



---

## Table of Contents 

- [Getting Started](#getting-started)
- [Building the Windows installer](#building-the-windows-installer)
- [Features](#features)
- [Usage](#usage) 
- [Executable](#executable)
- [To-do](#to-do)
- [Documentation](#documentation)
- [Tests](#tests)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [Donations](#donations)
- [License](#license)

---

## Getting Started

### Prerequisites

There is no specific requirement. This program should work fine with any installation of Python. Although, I used the following software (with their corresponding versions) to run this program:
- Python 3.7.4

### Clone

- Clone this repo to your local machine using `https://github.com/rajenderk18/Panther-Calculator.git`

### Running the Calculator

You can run the program by following the below commands:

```
$ git clone https://github.com/rajenderk18/Panther-Calculator.git
$ cd Panther-Calculator
$ chmod +x calculator.py
$ ./calculator.py

```
or run the calculator.py using python in terminal or command prompt using below command:

```
python calculator.py
```


---
## Building the Windows installer
---

## Features
- Version 0.1
- Cross-platform (can be used on any machine with any operating system.)
- easy to use
- supports common mathematical functions like (Division, Multiplication, Addition, Subtraction, Floor Division, Modulus Operator, Exponentiation and Square-root )
- Supports undo and clear screen
---

## Usage 

![Calculator in use](https://user-images.githubusercontent.com/35782113/63217309-18228b80-c112-11e9-9969-265061dae03c.gif)

## Executable
## To-do
  - [ ] Need to work on Scientific Calculator
  - [ ] Impelent the different themes for the GUI
  - [ ] create a class for mouse cursor hover property.
  - [ ] need to work on programmer calculator. 
 
## Documentation 

### Making the layout of the calculator

For making the layout of the calculator, I used the Tkinter widgets: "Entry" and "Frame". I used the "Entry", for taking input and showing the result. Frame is used to place all the buttons in the calculator. Tkinter provides three options to place the widgets in the window. These are called layout managers or geometry managers in python tkinter:
   - pack
   - grid
   - place

The three layout managers pack, grid, and place should never be mixed in the same master window! Geometry managers serve various functions. They:

  -  arrange widgets on the screen
  -  register widgets with the underlying windowing system
  -  manage the display of widgets on the screen

Arranging widgets on the screen includes determining the size and position of components. Widgets can provide size and alignment information to geometry managers, but the geometry managers has always the final say on the positioning and sizing. 

I used Place geometry manager for placing the buttons in relative positions with frame. Each widget is placed with coordinates of its origin and an exact size. Place is used when the user has the ability to drag and move widgets around. 
The Place geometry manager allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window. The place manager can be accessed through the place method. It can be applied to all standard widgets.

You can see the coordinates of the different buttons in the below pictures. Each button has 0.2 (times of Frame) width and height. We use the background color "White" (bg = white) for the number pad and SystemButtonFace color for the operations buttons.
&nbsp;


&nbsp;


![Calculator Button Coordinates](https://user-images.githubusercontent.com/35782113/63300902-4eddda80-c2a7-11e9-8894-7e6ccc8229aa.png)

&nbsp;


&nbsp;


### Binding functions to the buttons
I created the layout of the calculator with all buttons and text box for entry of input and publishing result. But this is half work done. The main task of performing different operations is done by the function and to make this calculator useful and functional, we need to bind functions to the buttons. The main function used in the program with their purpose are given below:

```
def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type)
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
		"""
    
```
```

def clear(self):
        """
        Allows user to backspace their entry.
        :return: None
        """
```
```
def clear_all(self):
        """
        Allows user to clear the full entry.
        :return: None
        """
```
```
def calculate(self):
        """
        Changes the operation symbols to their mathematical representation used in
        the eval() method.
        :return: None
        """
        
```
```
def flash(self,btn):
        """
        Flashes a corresponding button when key is pressed.
        :param btn: button
        :return: None
        """
```
```
def bind_buttons(self, master):
        """
        Binds keys to their appropriate input
        :param master: root.Tk()
        :return: None
        """
```	
```
def create_widgets(self, master):
        """
        Creates the widgets to be used in the grid.
        :return: None
        """
```

## Tests

---

## Contributing

If interested, you can contribute by following the given step:

1. Fork it using `https://github.com/rajenderk18/Panther-Calculator.git`
2. Create your feature branch (git checkout -b my-new-feature) 🔨🔨🔨
3. Commit your changes (git commit -am 'Added <xyz> feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request 🔃
---

## FAQ

- **Why did you create a new calculator, when there are already many exiting calculator available?**
    - I start this program just for learning purpose. Now, It become a very good calculator program.

- **Why did you create a new calculator in *tkinter*?**
    - Tkinter provide a great GUI for python based program. I enjoy the process of creating the GUI for this calculator in tkinter.
 - **What is '//' operation in the calculator?**
    - This ('//') is floor division operation. It provide the integer quotient for the division operation and remove the after decimal part. Foe example: 20//3 = 6.
 
    
---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://KumarRajender.com" target="_blank">`KumarRajender.com`</a>
- Email me: [rajenderk18@gmail.com](mailto:rajenderk18@gmail.com)

&nbsp;


---

## Donations

- If you think this little calculator is useful to you, then it's a good reason to do a donation.
- Your gratitude and financial help will motivate me to continue improving this an many other project development.

&nbsp;

&nbsp;


| Payment Method | Payment Link |
| --- | --- |
| PayPal |  <a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217312-24a6e400-c112-11e9-9eef-cc1a0bf69747.jpg" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>|
| Patreon |<p align="center"><a href="https://www.patreon.com/bePatron?u=23393229" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217315-253f7a80-c112-11e9-8aed-aa70e001c3d9.png"></a>|
| £ (GBP) | <a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217313-24a6e400-c112-11e9-8c54-a0d8ede0c0b9.png)" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> |
| € Euros	 |<a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63217313-24a6e400-c112-11e9-8c54-a0d8ede0c0b9.png)" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> |
| ₹ (INR) |![INR](https://user-images.githubusercontent.com/35782113/63217311-24a6e400-c112-11e9-896d-debe0ce54dab.png) |
| Buy Me a Coffee |<a href="https://www.buymeacoffee.com/rajenderk18" target="_blank"><img src="https://user-images.githubusercontent.com/35782113/63219307-f8548d00-c13c-11e9-809d-0c531dc1f0d2.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a> |


&nbsp;

&nbsp;

<p align="center">
  <a href="https://www.patreon.com/bePatron?u=23393229" target="_blank">
  <img width="300" height="125" src="https://user-images.githubusercontent.com/35782113/63217310-24a6e400-c112-11e9-9fb6-2d7f6ec2f143.jpg">
    </a>
</p>





---
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://github.com/rajenderk18/Panther-Calculator/blob/master/LICENSE)**
- Copyright 2019 © <a href="http://KumarRajender.com" target="_blank">Rajender Kumar</a>.
