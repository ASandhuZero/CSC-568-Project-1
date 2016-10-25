# CSC568 Project 1: A\* Financial Advisor
This is Project 1 for CSC-568 Fall Semester.

The A\* Financial Advisor is a program that both generates a financial model based off of standard deviations of interest rates and uses an A\* algorithm to determine the most optimal investment plan given different periods of time and interest rates during those times. 

The first part uses QuantLib Python, which creates a search space of time and interest rates based off of a general principle. 

The next part uses A\* to find the optimal combination of time periods and interest rates in the search space generated. This determines what interest rates for which time periods produce the most return on investment. For example, is it better to invest for 3 months at interest rate x, and then reinvest for another 3 months at interest rate y or invest for 6 months at interest rate z. It will determine the best combination of investments given time periods and the interest rates during those time periods.

Intalling QuantLib:

For Linux - http://quantlib.org/install/linux-python.shtml
For Mac OS X - http://quantlib.org/install/macosx-python.shtml
For Windows - https://vineetv.wordpress.com/2015/07/07/installing-quantlib-python-windows/


