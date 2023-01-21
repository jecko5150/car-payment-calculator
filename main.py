from tkinter import *


def payment():
    tax_rate = (int(tax_entry.get())) * .01
    terms = int(term_entry.get())
    price = float(price_entry.get())
    apr = (float(apr_entry.get())) * .01
    doc_fees = int(doc_entry.get())
    state = int(fees_entry.get())
    money = int(money_down_entry.get())
    sub_total = price + doc_fees + state
    tax_dollar = (price + doc_fees) * tax_rate
    total_financed = sub_total + tax_dollar - money
    monthly = (round(((total_financed * apr) / terms), 2)) + round((total_financed/terms), 2)
    payment_box.insert(0, str(monthly))
    financed_box.insert(0, str(total_financed))


# --------------------SETUP


window = Tk()
window.title("Payment Calculator")
window.config(padx=100, pady=50, background='gray')

# canvas = Canvas(width=300, height=300, highlightthickness=0)


app_title = Label(text="Payment Calculator", background='gray', fg='white', font=('Courier', 25, 'bold'),
                  justify='center'
                  )

price_label = Label(text="Price", background='gray', fg='white', font=('Courier', 10, 'bold'))
price_entry = Entry(width=20, font=('Courier', 10, 'normal'))

money_down_label = Label(text="Down", background='gray', fg='white', font=('Courier', 10, 'bold'))
money_down_entry = Entry(width=20, font=('Courier', 10, 'normal'))

fees_label = Label(text='State Fees', background='gray', fg='white', font=('Courier', 10, 'bold'))
fees_entry = Entry(width=10, font=('Courier', 10, 'normal'))
fees_entry.insert(0, "331")

doc_label = Label(text='Dealer Fees', background='gray', fg='white', font=('Courier', 10, 'bold'))
doc_entry = Entry(width=10, font=('Courier', 10, 'normal'))
doc_entry.insert(0, "500")

apr_label = Label(text="APR", background='gray', fg='white', font=('Courier', 10, 'bold'))
apr_entry = Entry(width=10, font=('Courier', 10, 'normal'))

term_label = Label(text="Term", background='gray', fg='white', font=('Courier', 10, 'bold'))
term_entry = Entry(width=10, font=('Courier', 10, 'normal'))

days_to_label = Label(text="Days:", background='gray', fg='white', font=('Courier', 10, 'bold'))
days_to_entry = Entry(width=10, font=('Courier', 10, 'normal'))

tax_label = Label(text="Tax Rate", background='gray', fg='white', font=('Courier', 10, 'bold'))
tax_entry = Entry(width=5, font=('Courier', 10, 'normal'))

payment_label = Label(text='Monthly', background='gray', fg='white', font=('Courier', 10, 'bold'))
payment_box = Entry(width=10, font=('Courier', 10, 'normal'))

financed = Label(text="Amount Financed", background='gray', fg='white', font=('Courier', 10, 'bold'))
financed_box = Entry(width=10, font=('Courier', 10, 'normal'))

payment_button = Button(width=30, text="Get Payment", command=payment, font=('Courier', 10, 'normal'))

app_title.grid(column=0, row=0, columnspan=3)
price_label.grid(column=0, row=1, sticky='w')
price_entry.grid(column=0, row=2, sticky='w')
money_down_label.grid(column=0, row=3, sticky='w')
money_down_entry.grid(column=0, row=4, sticky='w')
fees_label.grid(column=0, row=5, sticky='w')
fees_entry.grid(column=0, row=6, sticky='w')
doc_label.grid(column=0, row=7, sticky='w')
doc_entry.grid(column=0, row=8, sticky='w')
payment_label.grid(column=0, row=9, sticky='w')
payment_box.grid(column=0, row=10, sticky='w')

apr_label.grid(column=1, row=1, sticky='w')
apr_entry.grid(column=1, row=2, sticky='w')
term_label.grid(column=1, row=3, sticky='w')
term_entry.grid(column=1, row=4, sticky='w')
days_to_label.grid(column=1, row=5, sticky='w')
days_to_entry.grid(column=1, row=6, sticky='w')
tax_label.grid(column=1, row=7, sticky='w')
tax_entry.grid(column=1, row=8, sticky='w')
financed.grid(column=1, row=9, sticky='w')
financed_box.grid(column=1, row=10, sticky='w')

spacers = Label(text=" \n ", background='gray', fg='white')
spacers.grid(column=0, row=11, columnspan=2)
payment_button.grid(column=0, row=12, columnspan=2, stick='w')

window.mainloop()
