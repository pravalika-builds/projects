import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LogisticRegression

# Sample loan data
# [Income, Credit Score, Loan Amount, Existing Loans]
X = [
    [25000, 550, 200000, 3],
    [30000, 600, 150000, 2],
    [45000, 700, 200000, 1],
    [50000, 750, 250000, 0],
    [60000, 800, 300000, 0],
    [35000, 650, 180000, 1],
    [20000, 500, 250000, 4],
    [70000, 820, 350000, 0],
    [40000, 680, 220000, 1],
    [28000, 520, 200000, 3]
]

# 0 = Rejected, 1 = Approved
y = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]

# Train ML model
model = LogisticRegression()
model.fit(X, y)


def predict_loan():
    try:
        income = float(income_entry.get())
        credit_score = float(credit_entry.get())
        loan_amount = float(loan_entry.get())
        existing_loans = int(existing_entry.get())

        prediction = model.predict(
            [[income, credit_score, loan_amount, existing_loans]]
        )

        if prediction[0] == 1:
            result_label.config(
                text="Loan Approved ✅"
            )
        else:
            result_label.config(
                text="Loan Rejected ❌"
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


# Create window
root = tk.Tk()
root.title("AI Loan Approval Prediction")
root.geometry("500x500")

title = tk.Label(
    root,
    text="AI Loan Approval Prediction",
    font=("Arial", 20, "bold")
)
title.pack(pady=25)

tk.Label(root, text="Monthly Income (₹)").pack()
income_entry = tk.Entry(root)
income_entry.pack(pady=5)

tk.Label(root, text="Credit Score").pack()
credit_entry = tk.Entry(root)
credit_entry.pack(pady=5)

tk.Label(root, text="Loan Amount (₹)").pack()
loan_entry = tk.Entry(root)
loan_entry.pack(pady=5)

tk.Label(root, text="Existing Loans").pack()
existing_entry = tk.Entry(root)
existing_entry.pack(pady=5)

predict_button = tk.Button(
    root,
    text="Predict Loan",
    command=predict_loan,
    font=("Arial", 12, "bold")
)
predict_button.pack(pady=25)

result_label = tk.Label(
    root,
    text="Enter details and click Predict",
    font=("Arial", 14)
)
result_label.pack(pady=15)

root.mainloop()
