# Day-81-First-And-Last-Two

Day 81/100 - Python Program to Create a New String Made up of First and Last 2 Characters

# Create New String from First and Last 2 Characters

A program to dynamically generate a new string by extracting and combining only the first two and the last two characters of a user-provided string sequence.

## 📝 Description

This program processes a string of text inputted by the user and constructs a much shorter, concatenated version based on specific positional indices.

The logic is efficiently contained within the `create_new_string(input_string)` function. It first implements a safety check: `if len(input_string) < 2:`. If the user provides a string containing fewer than two characters, the function immediately returns an empty string `""` to prevent unexpected duplication or errors.

If the string is long enough, the script utilizes Python's built-in extended slice syntax. It grabs the first two characters using `input_string[:2]` and concatenates them with the last two characters extracted using `input_string[-2:]`. Finally, the driver code accepts the user input, executes the function, and prints the resulting newly formed string to the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text provided by the user via the terminal prompt.



### Output:

* A formatted string stating: "New string: [result]".



### Rules:

1. The program must prompt the user to input a string.


2. The core logic must be encapsulated in a function named `create_new_string(input_string)`.


3. The function must return an empty string if the length of the input is less than 2.


4. The function must use string slicing to combine `[:2]` and `[-2:]`.


5. The driver code must capture the returned value and print it to the console.



---

## 💡 Examples

### Example 1 (Standard Word)

**Input:**

```text
Python

```

**Output:**

```text
New string: Pyon

```

**Explanation:** The slice `[:2]` extracts "Py", and the slice `[-2:]` extracts "on". Concatenating them together results in "Pyon".

### Example 2 (Two-Character String)

**Input:**

```text
Hi

```

**Output:**

```text
New string: HiHi

```

**Explanation:** Because the string length is exactly 2, it bypasses the empty string check. The slice `[:2]` extracts the entire string ("Hi"), and the slice `[-2:]` also extracts the entire string ("Hi"), resulting in "HiHi".

### Example 3 (Single Character String)

**Input:**

```text
A

```

**Output:**

```text
New string: 

```

**Explanation:** The length of the string is 1, which triggers the `if len(input_string) < 2:` condition. The function safely returns an empty string `""`.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 81.py").

```bash
git clone https://github.com/adiaryaz/Day-81-First-And-Last-Two.git
cd first-and-last-two

```

2. **Run the program**:

```bash
python "Day 81.py"

```

Enter any word or sequence of characters when prompted to instantly see it compressed into just its starting and ending pairs!
