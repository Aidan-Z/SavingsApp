from tkinter import *
from tkinter import messagebox
from customtkinter import *
import numpy as np
import matplotlib.pyplot as plt



#in the future could try OOP version of this...
#lots of tedious code for no reason...

#--------------------------------------------------------------------
def slider_percent(value):
    x = int(value)
    percentage_label.configure(root, text=f"{x}%")

#--------------------------------------------------------------------
def graphs():

    if len(savings_entry.get()) ==0 or len(checking_entry.get()) == 0:
        messagebox.showinfo(title="error", message="Balance Field is Empty")

    #account balance
    savings_acc = float(savings_entry.get())
    checking_acc = float(checking_entry.get())

    #objects to buy (goals)
    g1 = goal1.get().capitalize()
    g2 = goal2.get().capitalize()
    g3 = goal3.get().capitalize()
    g4 = goal4.get().capitalize()
    g5 = goal5.get().capitalize()

    #cost of goals
    c1 = float(cost1.get())
    c2 = float(cost2.get())
    c3 = float(cost3.get())
    c4 = float(cost4.get())
    c5 = float(cost5.get())

    #total cost of all savings goals
    total_savings_cost = float(c1+c2+c3+c4+c5)

    # total available funds of user
    tot_funds = float(savings_acc+checking_acc)

    #emergency fund as % of total funds
    emergency_fund = float(tot_funds * (slider.get() * (10 ** -2)))

    #costs as percent of total FLOATS
    c1p = (c1/total_savings_cost)*100
    c2p = (c2/total_savings_cost)*100
    c3p = (c3/total_savings_cost)*100
    c4p = (c4/total_savings_cost)*100
    c5p = (c5/total_savings_cost)*100

    #funds as percent of total costs  ---------------> HERE: 'TypeError: 'float' object is not callable'
    s1 = (tot_funds*(c1p*(10 ** -2)))
    s2 = (tot_funds*(c2p*(10 ** -2)))
    s3 = (tot_funds*(c3p*(10 ** -2)))
    s4 = (tot_funds*(c4p*(10 ** -2)))
    s5 = (tot_funds*(c5p*(10 ** -2)))

    #data lists for graphs/charts
    saving_goals = (c1, c2, c3, c4, c5, emergency_fund) #costs / slices
    goals = [g1, g2, g3, g4, g5, 'emergency_fund'] #objects
    slice_colors = ["#0CC612", "#0CA0C6", "#220CC6", "#EB9721", "#B021EB", "#C60C0C"]
    explode_slice = [0, 0, 0, 0, 0, 0.3]

    current_savings_as_p = (s1, s2, s3, s4, s5, emergency_fund)

    X_axis = np.arange(len(goals))

    plt.bar(X_axis - 0.2, saving_goals, 0.4, label='Total Cost') #Total cost of goals
    plt.bar(X_axis + 0.2, current_savings_as_p, 0.4, label='Current Funds') #the amount i have reletive to these goals

    plt.xticks(X_axis, goals)
    plt.xlabel("Goals")
    plt.ylabel("Prices")
    plt.title(f'Current Funds: ${tot_funds}\n'
              f'Required Funds: ${total_savings_cost}\n'
              f'Current Deficit: ${tot_funds-total_savings_cost}')
    plt.legend()
    plt.show()

    #----------------------------------
    #PIE CHART of Distribution of Funds:

    # plt.pie(saving_goals, labels=goals, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'},
    #         colors=slice_colors, explode=explode_slice)
    # plt.title(f"Distribution of Funds - Total Funds: ${tot_funds}\n"
    #           f"Savings: ${savings_acc}\n"
    #           f"Checking: ${checking_acc}")
    #
    # plt.tight_layout()
    # plt.show()
    #
    #
    # messagebox.showinfo(title="Funds", message=f"Total Funds: ${tot_funds}\n"
    #                                            f"Required Funds: ${total_savings_cost}\n"
    #                                            f"Current Deficit: ${tot_funds-total_savings_cost}")

#--------------------------------------------------------------------
# SCREEN
#---------
root = CTk()
root.title("Savings Consultant")
root.minsize(width=400, height=400)
root.config(padx=20, pady=10)
#---------
# MAIN PROMPT
#---------
main_label = CTkLabel(root, text='Fill in the boxes:', fg_color="transparent", font=("Arial", 13, "bold"))
main_label.grid(row=0, column=1, pady=10)
#---------
# SAVING ACC BALANCE
#---------
savings_label = CTkLabel(root, text=' Balance in Savings:', fg_color="transparent")
savings_label.grid(row=1, column=0, pady=5, sticky='W')

savings_entry = CTkEntry(root, width=70)
savings_entry.grid(row=1, column=1)
#savings_entry.insert(0, x)   -> x: open a csv file and extract amount in savings, same for checking
#---------
# CHECKING ACC BALANCE
#---------
checking_label = CTkLabel(root, text='Balance in Checking:', fg_color="transparent")
checking_label.grid(row=2, column=0, pady=5, sticky='W')

checking_entry = CTkEntry(root, width=70)
checking_entry.grid(row=2, column=1)
#---------
# GOAL LABEL
#---------
goal_label = CTkLabel(root, text='Enter some savings goals:', fg_color="transparent")
goal_label.grid(row=3, column=0, pady=5, sticky="W")
#---------
# GOALS
#---------
goal1 = CTkEntry(root, width=160)
goal1.grid(row=4, column=0, pady=3, sticky="W")
goal2 = CTkEntry(root, width=160)
goal2.grid(row=5, column=0, pady=3, sticky="W")
goal3 = CTkEntry(root, width=160)
goal3.grid(row=6, column=0, pady=3, sticky="W")
goal4 = CTkEntry(root, width=160)
goal4.grid(row=7, column=0, pady=3, sticky="W")
goal5 = CTkEntry(root, width=160)
goal5.grid(row=8, column=0, pady=3, sticky="W")
#---------
# COST LABEL
#---------
goal_cost_label = CTkLabel(root, text='Prices:', fg_color="transparent")
goal_cost_label.grid(row=3, column=2, pady=5)
#---------
# COST
#---------
cost1 = CTkEntry(root, width=100)
cost1.grid(row=4, column=2, pady=3)
cost2 = CTkEntry(root, width=100)
cost2.grid(row=5, column=2, pady=3)
cost3 = CTkEntry(root, width=100)
cost3.grid(row=6, column=2, pady=3)
cost4 = CTkEntry(root, width=100)
cost4.grid(row=7, column=2, pady=3)
cost5 = CTkEntry(root, width=100)
cost5.grid(row=8, column=2, pady=3)
#---------
# GRAPH SAVINGS BUTTON
#---------
calc_button = CTkButton(root, text="Graph Savings", command=graphs, width=100)
calc_button.grid(row=10, column=2, pady=10)
#---------
# SLIDER
#---------
slider_label = CTkLabel(root, text='Money % to emergency fund?:', fg_color="transparent", font=("Arial", 11, "bold"))
slider_label.grid(row=9, column=0, pady=2)

slider = CTkSlider(root, from_=0, to=100, width=160, command=slider_percent, number_of_steps=100)
slider.grid(row=10, column=0, pady=2)
#---------
# SLIDER %
#---------
percentage_label = CTkLabel(root, text=f"{int(slider.get())}%", fg_color="transparent", font=("Arial", 12, "bold"))
percentage_label.grid(row=9, column=1, pady=2)
#---------


root.mainloop()
