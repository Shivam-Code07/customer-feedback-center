# Customer Feedback Center ⭐

A beginner-friendly customer feedback application built using Python and Tkinter.

## 📌 About the Project

Customer Feedback Center is a desktop GUI application that allows users to rate a service and share their feedback.

Users can select a star rating, write a review, and optionally provide their name and email address. Before submitting, users must accept the terms and conditions and confirm that their feedback is honest.

## ✨ Features

- ⭐ **5-Star Rating:** Rate the service from 1 to 5 stars.
- 💬 **Review Input:** Write feedback in a multiline text box.
- 👤 **Optional Name:** Users can provide their name or skip it.
- 📧 **Optional Email:** Users can provide their email address or skip it.
- ✅ **Consent Checkboxes:** Both confirmations are required to enable submission.
- 📋 **Console Output:** Submitted information is printed in the terminal.
- 🚪 **Not Now Option:** Close the application without submitting.

## 🛠️ Technologies Used

- Python
- Tkinter
- ttk — themed Tkinter widgets

## 📋 Requirements

- Python 3
- Tkinter support

Tkinter is included with many Python installations. Availability depends on how Python was installed.

## 🚀 How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run the following command:

   ```bash
   python customer_feedback_center.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 customer_feedback_center.py
   ```

4. The Customer Feedback Center window should open.
5. Select a rating, write your review, and optionally enter your name and email.
6. Accept both confirmations to enable the Submit button.
7. Click **Submit & Quit** to print the collected information in the terminal.

## 📂 Project Structure

```text
customer-feedback-center/
├── customer_feedback_center.py
└── README.md
```

## ⚠️ Current Limitations

- Feedback is printed in the terminal and is not saved to a file or database.
- Email addresses are not validated.
- The application does not currently verify that a star rating has been selected.
- The review text box starts with instructional text that users must remove themselves.
- The application is a learning project and has not been designed for production use.

## 🔮 Future Improvements

- Add proper placeholder behavior for input fields.
- Validate the email address.
- Require a star rating before submission.
- Save reviews to a CSV file or SQLite database.
- Improve the layout and responsiveness of the interface.
- Display a confirmation message after successful submission.

## 🎯 Learning Goals

This project provides practice with Tkinter widgets, callback functions, variables, event handling, conditional logic, text input, and GUI layout management.

## 📄 License

This project is intended for learning and practice. A license can be added if the project is distributed publicly.
