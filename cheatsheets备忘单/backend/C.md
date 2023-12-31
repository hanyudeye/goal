

## C

C quick reference cheat sheet that provides basic syntax and methods.

## [#](https://quickref.me/c.html#getting-started)Getting Started

### 乱码 
> 国际化下,一种语言 显示正确情况 中文 ，英文 ，如果中文用英文编码显示，会乱码，所以要使用正确的语言。

### hello.c

```c
#include <stdio.h> int main(void) { printf("Hello World!\n"); return 0; }
```

Compile `hello.c` file with `gcc`

```bash
$ gcc hello.c -o hello
```

Run the compiled binary `hello`

```bash
$ ./hello
```

Output => Hello World!

### Variables

```c
int myNum = 15; int myNum2; // do not assign, then assign myNum2 = 15; int myNum3 = 15; // myNum3 is 15 myNum3 = 10; // myNum3 is now 10 float myFloat = 5.99; // floating point number char myLetter = 'D'; // character int x = 5; int y = 6; int sum = x + y; // add variables to sum // declare multiple variables int x = 5, y = 6, z = 50;
```

### Constants

```c
const int minutesPerHour = 60; const float PI = 3.14;
```

Best Practices

```c
const int BIRTHYEAR = 1980;
```

```c
// this is a comment printf("Hello World!"); // Can comment anywhere in file /*Multi-line comment, print Hello World! to the screen, it's awesome */
```

### Print text

```c
printf("I am learning C."); int testInteger = 5; printf("Number = %d", testInteger); float f = 5.99; // floating point number printf("Value = %f", f); short a = 0b1010110; // binary number int b = 02713; // octal number long c = 0X1DAB83; // hexadecimal number // output in octal form printf("a=%ho, b=%o, c=%lo\n", a, b, c); // output => a=126, b=2713, c=7325603 // Output in decimal form printf("a=%hd, b=%d, c=%ld\n", a, b, c); // output => a=86, b=1483, c=1944451 // output in hexadecimal form (letter lowercase) printf("a=%hx, b=%x, c=%lx\n", a, b, c); // output => a=56, b=5cb, c=1dab83 // Output in hexadecimal (capital letters) printf("a=%hX, b=%X, c=%lX\n", a, b, c); // output => a=56, b=5CB, c=1DAB83
```

### Control the number of spaces

```c
int a1 = 20, a2 = 345, a3 = 700; int b1 = 56720, b2 = 9999, b3 = 20098; int c1 = 233, c2 = 205, c3 = 1; int d1 = 34, d2 = 0, d3 = 23; printf("%-9d %-9d %-9d\n", a1, a2, a3); printf("%-9d %-9d %-9d\n", b1, b2, b3); printf("%-9d %-9d %-9d\n", c1, c2, c3); printf("%-9d %-9d %-9d\n", d1, d2, d3);
```

output result

```bash
20 345 700 56720 9999 20098 233 205 1 34 0 23
```

In `%-9d`, `d` means to output in `10` base, `9` means to occupy at least `9` characters width, and the width is not enough to fill with spaces, `-` means left alignment

### Strings

```c
char greetings[] = "Hello World!"; printf("%s", greetings);
```

access string

```c
char greetings[] = "Hello World!"; printf("%c", greetings[0]);
```

modify string

```c
char greetings[] = "Hello World!"; greetings[0] = 'J'; printf("%s", greetings); // prints "Jello World!"
```

Another way to create a string

```c
char greetings[] = {'H','e','l','l','\0'}; printf("%s", greetings); // print "Hell!"
```

Creating String using character pointer (String Literals)

```c
char *greetings = "Hello"; printf("%s", greetings); // print "Hello!"
```

**NOTE**: String literals might be stored in read-only section of memory. Modifying a string literal invokes undefined behavior. You can't modify it.!

`C` **does not** have a String type, use `char` type and create an `array` of characters

### Condition

```c
int time = 20; if (time < 18) { printf("Goodbye!"); } else { printf("Good evening!"); } // Output -> "Good evening!" int time = 22; if (time < 10) { printf("Good morning!"); } else if (time < 20) { printf("Goodbye!"); } else { printf("Good evening!"); } // Output -> "Good evening!"
```

### Ternary operator

```c
int age = 20; (age > 19) ? printf("Adult") : printf("Teenager");
```

### Switch

```c
int day = 4; switch (day) { case 3: printf("Wednesday"); break; case 4: printf("Thursday"); break; default: printf("Weekend!"); } // output -> "Thursday" (day 4)
```

### While Loop

```c
int i = 0; while (i < 5) { printf("%d\n", i); i++; }
```

**NOTE**: Don't forget to increment the variable used in the condition, otherwise the loop will never end and become an "infinite loop"!

### Do/While Loop

```c
int i = 0; do { printf("%d\n", i); i++; } while (i < 5);
```

### For Loop

```c
for (int i = 0; i < 5; i++) { printf("%d\n", i); }
```

### Break out of the loop Break/Continue

```c
for (int i = 0; i < 10; i++) { if (i == 4) { break; } printf("%d\n", i); }
```

break out of the loop when `i` is equal to `4`

```c
for (int i = 0; i < 10; i++) { if (i == 4) { continue; } printf("%d\n", i); }
```

Example to skip the value of `4`

### While Break Example

```c
int i = 0; while (i < 10) { if (i == 4) { break; } printf("%d\n", i); i++; }
```

### While continue example

```c
int i = 0; while (i < 10) { i++; if (i == 4) { continue; } printf("%d\n", i); }
```

### Arrays

```c
int myNumbers[] = {25, 50, 75, 100}; printf("%d", myNumbers[0]); // output 25
```

change array elements

```c
int myNumbers[] = {25, 50, 75, 100}; myNumbers[0] = 33; printf("%d", myNumbers[0]);
```

Loop through the array

```c
int myNumbers[] = {25, 50, 75, 100}; int i; for (i = 0; i < 4; i++) { printf("%d\n", myNumbers[i]); }
```

set array size

```c
// Declare an array of four integers: int myNumbers[4]; // add element myNumbers[0] = 25; myNumbers[1] = 50; myNumbers[2] = 75; myNumbers[3] = 100;
```

### Enumeration Enum

```c
enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun };
```

define enum variable

```c
enum week a, b, c; enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun } a, b, c;
```

With an enumeration variable, you can assign the value in the list to it

```c
enum week { Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun }; enum week a = Mon, b = Wed, c = Sat; // or enum week{ Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun } a = Mon, b = Wed, c = Sat;
```

### Enumerate sample applications

```c
enum week {Mon = 1, Tues, Wed, Thurs} day; scanf("%d", &day); switch(day) { case Mon: puts("Monday"); break; case Tues: puts("Tuesday"); break; case Wed: puts("Wednesday"); break; case Thursday: puts("Thursday"); break; default: puts("Error!"); }
```

### User input

```c
// Create an integer variable to store the number we got from the user int myNum; // Ask the user to enter a number printf("Please enter a number: \n"); // Get and save the number entered by the user scanf("%d", &myNum); // Output the number entered by the user printf("The number you entered: %d", myNum);
```

### User input string

```c
// create a string char firstName[30]; // Ask the user to enter some text printf("Enter your name: \n"); // get and save the text scanf("%s", &firstName); // output text printf("Hello %s.", firstName);
```

### memory address

When a variable is created, it is assigned a memory address

```c
int myAge = 43; printf("%p", &myAge); // Output: 0x7ffe5367e044
```

To access it, use the reference operator (`&`)

### create pointer

```c
int myAge = 43; // an int variable printf("%d", myAge); // output the value of myAge(43) // Output the memory address of myAge (0x7ffe5367e044) printf("%p", &myAge);
```

### pointer variable

```c
int myAge = 43; // an int variable int*ptr = &myAge; // pointer variable named ptr, used to store the address of myAge printf("%d\n", myAge); // print the value of myAge (43) printf("%p\n", \&myAge); // output the memory address of myAge (0x7ffe5367e044) printf("%p\n", ptr); // use the pointer (0x7ffe5367e044) to output the memory address of myAge
```

### Dereference

```c
int myAge = 43; // variable declaration int*ptr = &myAge; // pointer declaration // Reference: output myAge with a pointer // memory address (0x7ffe5367e044) printf("%p\n", ptr); // dereference: output the value of myAge with a pointer (43) printf("%d\n", *ptr);
```

## [#](https://quickref.me/c.html#operators)Operators

### Arithmetic Operators

```c
int myNum = 100 + 50; int sum1 = 100 + 50; // 150 (100 + 50) int sum2 = sum1 + 250; // 400 (150 + 250) int sum3 = sum2 + sum2; // 800 (400 + 400)
```

___

<table><tbody><tr><td><code>+</code></td><td>Add</td><td><code>x + y</code></td></tr><tr><td><code>-</code></td><td>Subtract</td><td><code>x - y</code></td></tr><tr><td><code>*</code></td><td>Multiply</td><td><code>x * y</code></td></tr><tr><td><code>/</code></td><td>Divide</td><td><code>x / y</code></td></tr><tr><td><code>%</code></td><td>Modulo</td><td><code>x % y</code></td></tr><tr><td><code>++</code></td><td>Increment</td><td><code>++x</code></td></tr><tr><td><code>--</code></td><td>Decrement</td><td><code>--x</code></td></tr></tbody></table>

### Assignment operator

<table><tbody><tr><td>x <code>=</code> 5</td><td>x <code>=</code> 5</td></tr><tr><td>x <code>+=</code> 3</td><td>x <code>=</code> x <code>+</code> 3</td></tr><tr><td>x <code>-=</code> 3</td><td>x <code>=</code> x <code>-</code> 3</td></tr><tr><td>x <code>*=</code> 3</td><td>x <code>=</code> x <code>*</code> 3</td></tr><tr><td>x <code>/=</code> 3</td><td>x <code>=</code> x <code>/</code> 3</td></tr><tr><td>x <code>%=</code> 3</td><td>x <code>=</code> x <code>%</code> 3</td></tr><tr><td>x <code>&amp;=</code> 3</td><td>x <code>=</code> x <code>&amp;</code> 3</td></tr><tr><td>x <code>|=</code> 3</td><td>x <code>=</code> x <code>|</code> 3</td></tr><tr><td>x <code>^=</code> 3</td><td>x <code>=</code> x <code>^</code> 3</td></tr><tr><td>x <code>&gt;&gt;=</code> 3</td><td>x <code>=</code> x <code>&gt;&gt;</code> 3</td></tr><tr><td>x <code>&lt;&lt;=</code> 3</td><td>x <code>=</code> x <code>&lt;&lt;</code> 3</td></tr></tbody></table>

### Comparison Operators

```c
int x = 5; int y = 3; printf("%d", x > y); // returns 1 (true) because 5 is greater than 3
```

___

<table><tbody><tr><td><code>==</code></td><td>equals</td><td>x <code>==</code> y</td></tr><tr><td><code>!=</code></td><td>not equal to</td><td>x <code>!=</code> y</td></tr><tr><td><code>&gt;</code></td><td>greater than</td><td>x <code>&gt;</code> y</td></tr><tr><td><code>&lt;</code></td><td>less than</td><td>x <code>&lt;</code> y</td></tr><tr><td><code>&gt;=</code></td><td>greater than or equal to</td><td>x <code>&gt;=</code> y</td></tr><tr><td><code>&lt;=</code></td><td>less than or equal to</td><td>x <code>&lt;=</code> y</td></tr></tbody></table>

Comparison operators are used to compare two values

### Logical Operators

<table><tbody><tr><td><code>&amp;&amp;</code></td><td><code>and</code> logical</td><td>returns true if both statements are true</td><td><code>x &lt; 5 &amp;&amp; x &lt; 10</code></td></tr><tr><td><code>||</code></td><td><code>or</code> logical</td><td>returns true if one of the statements is true</td><td><code>x &lt; 5 || x &lt; 4</code></td></tr><tr><td><code>!</code></td><td><code>not</code> logical</td><td>Invert result, return false if true</td><td><code>!(x &lt; 5 &amp;&amp; x &lt; 10)</code></td></tr></tbody></table>

### Operator Examples

```c
unsigned int a = 60; /*60 = 0011 1100 */ unsigned int b = 13; /*13 = 0000 1101 */ int c = 0; c = a & b; /*12 = 0000 1100 */ printf("Line 1 -the value of c is %d\n", c); c = a | b; /*61 = 0011 1101 */ printf("Line 2 -the value of c is %d\n", c); c = a ^ b; /*49 = 0011 0001 */ printf("Line 3 -the value of c is %d\n", c); c = ~a; /*-61 = 1100 0011 */ printf("Line 4 -The value of c is %d\n", c); c = a << 2; /*240 = 1111 0000 */ printf("Line 5 -the value of c is %d\n", c); c = a >> 2; /*15 = 0000 1111 */ printf("Line 6 -The value of c is %d\n", c);
```

### Bitwise operators

<table><tbody><tr><td><code>&amp;</code></td><td>Bitwise AND operation, "AND" operation by binary digits</td><td><code>(A &amp; B)</code> will get <code>12</code> which is 0000 1100</td></tr><tr><td><code>|</code></td><td>Bitwise OR operator, "or" operation by binary digit</td><td><code>(A | B)</code> will get <code>61</code> which is 0011 1101</td></tr><tr><td><code>^</code></td><td>XOR operator, perform "XOR" operation by binary digits</td><td><code>(A ^ B)</code> will get <code>49</code> which is 0011 0001</td></tr><tr><td><code>~</code></td><td>Inversion operator, perform "inversion" operation by binary bit</td><td><code>(~A)</code> will get <code>-61</code> which is 1100 0011</td></tr><tr><td><code>&lt;&lt;</code></td><td>binary left shift operator</td><td><code>A &lt;&lt; 2</code> will get <code>240</code> which is 1111 0000</td></tr><tr><td><code>&gt;&gt;</code></td><td>binary right shift operator</td><td><code>A &gt;&gt; 2</code> will get <code>15</code> which is 0000 1111</td></tr></tbody></table>

## [#](https://quickref.me/c.html#data-types)Data Types

### Basic data types

<table><tbody><tr><td><code>char</code></td><td>1 byte</td><td><code>−128</code> ~ <code>127</code></td><td>single character/alphanumeric/ASCII</td></tr><tr><td><code>signed char</code></td><td>1 byte</td><td><code>−128</code> ~ <code>127</code></td><td>-</td></tr><tr><td><code>unsigned char</code></td><td>1 byte</td><td><code>0</code> ~ <code>255</code></td><td>-</td></tr><tr><td><code>int</code></td><td><code>2</code> to <code>4</code> bytes</td><td><code>−32,768</code> ~ <code>32,767</code></td><td>store integers</td></tr><tr><td><code>signed int</code></td><td>2 bytes</td><td><code>−32,768</code> ~ <code>32,767</code></td><td></td></tr><tr><td><code>unsigned int</code></td><td>2 bytes</td><td><code>0</code> ~ <code>65,535</code></td><td></td></tr><tr><td><code>short int</code></td><td>2 bytes</td><td><code>−32,768</code> ~ <code>32,767</code></td><td></td></tr><tr><td><code>signed short int</code></td><td>2 bytes</td><td><code>−32,768</code> ~ <code>32,767</code></td><td></td></tr><tr><td><code>unsigned short int</code></td><td>2 bytes</td><td><code>0</code> ~ <code>65,535</code></td><td></td></tr><tr><td><code>long int</code></td><td>4 bytes</td><td><code>-2,147,483,648</code> ~ <code>2,147,483,647</code></td><td></td></tr><tr><td><code>signed long int</code></td><td>4 bytes</td><td><code>-2,147,483,648</code> ~ <code>2,147,483,647</code></td><td></td></tr><tr><td><code>unsigned long int</code></td><td>4 bytes</td><td><code>0</code> ~ <code>4,294,967,295</code></td><td></td></tr><tr><td><code>float</code></td><td>4 bytes</td><td><code>3.4E-38</code> ~ <code>3.4E+38</code></td><td></td></tr><tr><td><code>double</code></td><td>8 bytes</td><td><code>1.7E-308</code> ~ <code>1.7E+308</code></td><td></td></tr><tr><td><code>long double</code></td><td>10 bytes</td><td><code>3.4E-4932</code> ~ <code>1.1E+4932</code></td><td></td></tr></tbody></table>

### Data types

```c
// create variables int myNum = 5; // integer float myFloatNum = 5.99; // floating point number char myLetter = 'D'; // string // High precision floating point data or numbers double myDouble = 3.2325467; // print output variables printf("%d\n", myNum); printf("%f\n", myFloatNum); printf("%c\n", myLetter); printf("%lf\n", myDouble);
```

___

<table><tbody><tr><td><code>char</code></td><td>character type</td></tr><tr><td><code>short</code></td><td>short integer</td></tr><tr><td><code>int</code></td><td>integer type</td></tr><tr><td><code>long</code></td><td>long integer</td></tr><tr><td><code>float</code></td><td>single-precision floating-point type</td></tr><tr><td><code>double</code></td><td>double-precision floating-point type</td></tr><tr><td><code>void</code></td><td>no type</td></tr></tbody></table>

### Basic format specifiers

<table><tbody><tr><td><code>%d</code> or <code>%i</code></td><td><code>int</code> integer</td></tr><tr><td><code>%f</code></td><td><code>float</code> single-precision decimal type</td></tr><tr><td><code>%lf</code></td><td><code>double</code> high precision floating point data or number</td></tr><tr><td><code>%c</code></td><td><code>char</code> character</td></tr><tr><td><code>%s</code></td><td>for <code>strings</code> strings</td></tr></tbody></table>

### Basic format specifiers

<table><tbody><tr><td>Octal</td><td><code>%ho</code></td><td><code>%o</code></td><td><code>%lo</code></td></tr><tr><td>Decimal</td><td><code>%hd</code></td><td><code>%d</code></td><td><code>%ld</code></td></tr><tr><td>Hexadecimal</td><td><code>%hx</code> /<code>%hX</code></td><td><code>%x</code> /<code>%X</code></td><td><code>%lx</code> /<code>%lX</code></td></tr></tbody></table>

### Data format example

```c
int myNum = 5; float myFloatNum = 5.99; // floating point number char myLetter = 'D'; // string // print output variables printf("%d\n", myNum); printf("%f\n", myFloatNum); printf("%c\n", myLetter);
```

## [#](https://quickref.me/c.html#c-preprocessor)C Preprocessor

### Preprocessor Directives

<table><tbody><tr><td><code>#define</code></td><td>define a macro</td></tr><tr><td><code>#include</code></td><td>include a source code file</td></tr><tr><td><code>#undef</code></td><td>undefined macro</td></tr><tr><td><code>#ifdef</code></td><td>Returns true if the macro is defined</td></tr><tr><td><code>#ifndef</code></td><td>Returns true if the macro is not defined</td></tr><tr><td><code>#if</code></td><td>Compile the following code if the given condition is true</td></tr><tr><td><code>#else</code></td><td>Alternative to <code>#if</code></td></tr><tr><td><code>#elif</code></td><td>If the <code>#if</code> condition is false, the current condition is <code>true</code></td></tr><tr><td><code>#endif</code></td><td>End a <code>#if...#else</code> conditional compilation block</td></tr><tr><td><code>#error</code></td><td>Print an error message when standard error is encountered</td></tr><tr><td><code>#pragma</code></td><td>Issue special commands to the compiler using the standardized method</td></tr></tbody></table>

```c
// replace all MAX_ARRAY_LENGTH with 20 #define MAX_ARRAY_LENGTH 20 // Get stdio.h from the system library #include <stdio.h> // Get myheader.h in the local directory #include "myheader.h" #undef FILE_SIZE #define FILE_SIZE 42 // undefine and define to 42
```

### Predefined macros

<table><tbody><tr><td><code>__DATE__</code></td><td>The current date, a character constant in the format "MMM DD YYYY"</td></tr><tr><td><code>__TIME__</code></td><td>The current time, a character constant in the format "HH:MM:SS"</td></tr><tr><td><code>__FILE__</code></td><td>This will contain the current filename, a string constant</td></tr><tr><td><code>__LINE__</code></td><td>This will contain the current line number, a decimal constant</td></tr><tr><td><code>__STDC__</code></td><td>Defined as <code>1</code> when the compiler compiles against the <code>ANSI</code> standard</td></tr></tbody></table>

`ANSI C` defines a number of macros that you can use, but you cannot directly modify these predefined macros

#### Predefined macro example

```c
#include <stdio.h> int main() { printf("File :%s\n", __FILE__); printf("Date :%s\n", __DATE__); printf("Time :%s\n", __TIME__); printf("Line :%d\n", __LINE__); printf("ANSI :%d\n", __STDC__); }
```

### Macro continuation operator ()

A macro is usually written on a single line.

```c
#define message_for(a, b) \ printf(#a " and " #b ": We love you!\n")
```

If the macro is too long to fit on a single line, use the macro continuation operator `\`

### String Constantization Operator (#)

```c
#include <stdio.h> #define message_for(a, b) \ printf(#a " and " #b ": We love you!\n") int main(void) { message_for(Carole, Debra); return 0; }
```

When the above code is compiled and executed, it produces the following result:

```
<span>Carole</span> <span>and</span> Debra: We love you!
```

When you need to convert a macro parameter to a string constant, use the string constant operator `#`

### tag paste operator (##)

```c
#include <stdio.h> #define tokenpaster(n) printf ("token" #n " = %d", token##n) int main(void) { int token34 = 40; tokenpaster(34); return 0; }
```

### defined() operator

```c
#include <stdio.h> #if !defined (MESSAGE) #define MESSAGE "You wish!" #endif int main(void) { printf("Here is the message: %s\n", MESSAGE); return 0; }
```

### Parameterized macros

```c
int square(int x) { return x * x; }
```

The macro rewrites the above code as follows:

```c
#define square(x) ( (x) * (x) )
```

No spaces are allowed between the macro name and the opening parenthesis

```c
#include <stdio.h> #define MAX(x,y) ( (x) > (y) ? (x) : (y) ) int main(void) { printf("Max between 20 and 10 is %d\n", MAX(10, 20)); return 0; }
```

## [#](https://quickref.me/c.html#c-function)C Function

### Function declaration and definition

```c
int main(void) { printf("Hello World!"); return 0; }
```

The function consists of two parts

```c
void myFunction() { // declaration declaration // function body (code to be executed) (definition) }
```

___

-   `Declaration` declares the function name, return type and parameters _(if any)_
-   `Definition` function body _(code to execute)_

___

```c
// function declaration void myFunction(); // main method int main() { myFunction(); // --> call the function return 0; } void myFunction() {// Function definition printf("Good evening!"); }
```

### Call function

```c
// create function void myFunction() { printf("Good evening!"); } int main() { myFunction(); // call the function myFunction(); // can be called multiple times return 0; } // Output -> "Good evening!" // Output -> "Good evening!"
```

### Function parameters

```c
void myFunction(char name[]) { printf("Hello %s\n", name); } int main() { myFunction("Liam"); myFunction("Jenny"); return 0; } // Hello Liam // Hello Jenny
```

### Multiple parameters

```c
void myFunction(char name[], int age) { printf("Hi %s, you are %d years old.\n",name,age); } int main() { myFunction("Liam", 3); myFunction("Jenny", 14); return 0; } // Hi Liam you are 3 years old. // Hi Jenny you are 14 years old.
```

### Return value

```c
int myFunction(int x) { return 5 + x; } int main() { printf("Result: %d", myFunction(3)); return 0; } // output 8 (5 + 3)
```

two parameters

```c
int myFunction(int x, int y) { return x + y; } int main() { printf("Result: %d", myFunction(5, 3)); // store the result in a variable int result = myFunction(5, 3); printf("Result = %d", result); return 0; } // result: 8 (5 + 3) // result = 8 (5 + 3)
```

### Recursive example

```c
int sum(int k); int main() { int result = sum(10); printf("%d", result); return 0; } int sum(int k) { if (k > 0) { return k + sum(k -1); } else { return 0; } }
```

### Mathematical functions

```c
#include <math.h> void main(void) { printf("%f", sqrt(16)); // square root printf("%f", ceil(1.4)); // round up (round) printf("%f", floor(1.4)); // round up (round) printf("%f", pow(4, 3)); // x(4) to the power of y(3) }
```

___

-   `abs(x)` absolute value
-   `acos(x)` arc cosine value
-   `asin(x)` arc sine
-   `atan(x)` arc tangent
-   `cbrt(x)` cube root
-   `cos(x)` cosine
-   the value of `exp(x)` Ex
-   `sin(x)` the sine of x
-   tangent of `tan(x)` angle

## [#](https://quickref.me/c.html#c-structures)C Structures

### Create structure

```c
struct MyStructure { // structure declaration int myNum; // member (int variable) char myLetter; // member (char variable) }; // end the structure with a semicolon
```

Create a struct variable called `s1`

```c
struct myStructure { int myNum; char myLetter; }; int main() { struct myStructure s1; return 0; }
```

### Strings in the structure

```c
struct myStructure { int myNum; char myLetter; char myString[30]; // String }; int main() { struct myStructure s1; strcpy(s1. myString, "Some text"); // print value printf("my string: %s", s1.myString); return 0; }
```

Assigning values to strings using the `strcpy` function

### Accessing structure members

```c
// create a structure called myStructure struct myStructure { int myNum; char myLetter; }; int main() { // Create a structure variable called myStructure called s1 struct myStructure s1; // Assign values to the members of s1 s1.myNum = 13; s1.myLetter = 'B'; // Create a structure variable of myStructure called s2 // and assign it a value struct myStructure s2 = {13, 'B'}; // print value printf("My number: %d\n", s1.myNum); printf("My letter: %c\n", s1.myLetter); return 0; }
```

Create different structure variables

```c
struct myStructure s1; struct myStructure s2; // Assign values to different structure variables s1.myNum = 13; s1.myLetter = 'B'; s2.myNum = 20; s2.myLetter = 'C';
```

### Copy structure

```c
struct myStructure s1 = { 13, 'B', "Some text" }; struct myStructure s2; s2 = s1;
```

In the example, the value of `s1` is copied to `s2`

### Modify value

```c
// Create a struct variable and assign it a value struct myStructure s1 = { 13, 'B' }; // modify the value s1.myNum = 30; s1.myLetter = 'C'; // print value printf("%d %c %s", s1.myNum, s1.myLetter);
```

## [#](https://quickref.me/c.html#file-processing)file processing

### File processing function

<table><tbody><tr><td><code>fopen()</code></td><td><code>open</code> a new or existing file</td></tr><tr><td><code>fprintf()</code></td><td>write data to <code>file</code></td></tr><tr><td><code>fscanf()</code></td><td><code>read</code> data from a file</td></tr><tr><td><code>fputc()</code></td><td>write a character to <code>file</code></td></tr><tr><td><code>fgetc()</code></td><td><code>read</code> a character from a file</td></tr><tr><td><code>fclose()</code></td><td><code>close</code> the file</td></tr><tr><td><code>fseek()</code></td><td>set the file pointer to <code>the given position</code></td></tr><tr><td><code>fputw()</code></td><td>Write an integer <code>to</code> a file</td></tr><tr><td><code>fgetw()</code></td><td><code>read</code> an integer from a file</td></tr><tr><td><code>ftell()</code></td><td>returns the current <code>position</code></td></tr><tr><td><code>rewind()</code></td><td>set the file pointer to the beginning of the file</td></tr></tbody></table>

There are many functions in the C library to `open`/`read`/`write`/`search` and `close` files

### Open mode parameter

<table><tbody><tr><td><code>r</code></td><td>Open a text file in <code>read</code> mode, allowing the file to be read</td></tr><tr><td><code>w</code></td><td>Open a text file in <code>write</code> mode, allowing writing to the file</td></tr><tr><td><code>a</code></td><td>Open a text file in <code>append</code> mode<br>If the file does not exist, a new one will be created</td></tr><tr><td><code>r+</code></td><td>Open a text file in <code>read-write</code> mode, allowing reading and writing of the file</td></tr><tr><td><code>w+</code></td><td>Open a text file in <code>read-write</code> mode, allowing reading and writing of the file</td></tr><tr><td><code>a+</code></td><td>Open a text file in <code>read-write</code> mode, allowing reading and writing of the file</td></tr><tr><td><code>rb</code></td><td>Open a binary file in <code>read</code> mode</td></tr><tr><td><code>wb</code></td><td>Open binary file in <code>write</code> mode</td></tr><tr><td><code>ab</code></td><td>Open a binary file in <code>append</code> mode</td></tr><tr><td><code>rb+</code></td><td>open binary file in <code>read-write</code> mode</td></tr><tr><td><code>wb+</code></td><td>Open binary file in <code>read-write</code> mode</td></tr><tr><td><code>ab+</code></td><td>open binary file in <code>read-write</code> mode</td></tr></tbody></table>

### Open the file: fopen()

```c
#include <stdio.h> void main() { FILE *fp; char ch; fp = fopen("file_handle.c", "r"); while (1) { ch = fgetc(fp); if (ch == EOF) break; printf("%c", ch); } fclose(fp); }
```

After performing all operations on the file, the file must be closed with `fclose()`

### Write to file: fprintf()

```c
#include <stdio.h> void main() { FILE *fp; fp = fopen("file.txt", "w"); // open the file // write data to file fprintf(fp, "Hello file for fprintf..\n"); fclose(fp); // close the file }
```

### Read the file: fscanf()

```c
#include <stdio.h> void main() { FILE *fp; char buff[255]; // Create a char array to store file data fp = fopen("file.txt", "r"); while(fscanf(fp, "%s", buff) != EOF) { printf("%s ", buff); } fclose(fp); }
```

### Write to file: fputc()

```c
#include <stdio.h> void main() { FILE *fp; fp = fopen("file1.txt", "w"); // open the file fputc('a',fp); // write a single character to the file fclose(fp); // close the file }
```

### Read the file: fgetc()

```c
#include <stdio.h> #include <conio.h> void main() { FILE *fp; char c; clrscr(); fp = fopen("myfile.txt", "r"); while( (c = fgetc(fp) ) != EOF) { printf("%c", c); } fclose(fp); getch(); }
```

### Write to file: fputs()

```c
#include<stdio.h> #include<conio.h> void main() { FILE *fp; clrscr(); fp = fopen("myfile2.txt","w"); fputs("hello c programming",fp); fclose(fp); getch(); }
```

### Read files: fgets()

```c
#include<stdio.h> #include<conio.h> void main() { FILE *fp; char text[300]; clrscr(); fp = fopen("myfile2.txt", "r"); printf("%s", fgets(text, 200, fp)); fclose(fp); getch(); }
```

### fseek()

```c
#include <stdio.h> void main(void) { FILE *fp; fp = fopen("myfile.txt","w+"); fputs("This is Book", fp); // Set file pointer to the given position fseek(fp, 7, SEEK_SET); fputs("Kenny Wong", fp); fclose(fp); }
```

set the file pointer to the given position

### rewind()

```c
#include <stdio.h> #include <conio.h> void main() { FILE *fp; char c; clrscr(); fp = fopen("file.txt", "r"); while( (c = fgetc(fp) ) != EOF) { printf("%c", c); } rewind(fp); // move the file pointer to the beginning of the file while( (c = fgetc(fp) ) != EOF) { printf("%c", c); } fclose(fp); getch(); } // output // Hello World! Hello World!
```

### ftell()

```c
#include <stdio.h> #include <conio.h> void main () { FILE *fp; int length; clrscr(); fp = fopen("file.txt", "r"); fseek(fp, 0, SEEK_END); length = ftell(fp); // return current position fclose(fp); printf("File size: %d bytes", length); getch(); } // output // file size: 18 bytes
```

