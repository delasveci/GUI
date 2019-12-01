print "hi user"
print "we are going to calculate your gross salary per week"

h_week = raw_input('How many hours you work per week: ')
try:
    float(h_week)
except:
    print 'You have enter an no acceptable value of hours'
    quit()

rate = raw_input('How is the rate per hour: ')
try:
    float(rate)
except:
    print 'You have enter an no acceptable value of rate'
    quit()


def print_puta():
    print 'imprimiendo a tu madre'


if int(h_week) > 40:
    gross = float(h_week) * float(rate) + 5 * (float(h_week) - 40)
else:
    gross = float(h_week) * float(rate)

print 'Your gross salary is ', gross, ' dolars/week'

print_puta()
