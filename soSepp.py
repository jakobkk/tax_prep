from constants import LIFE_EXPECTANCY, MORTALITY

def rmd(age, bal, method='1.401(a)(9)-9 Single'):
    annual_payment = bal/(LIFE_EXPECTANCY[method][age])
    return annual_payment/12

def fixed_ammortization(age,bal,method='1.401(a)(9)-9 Single',i=0.05):
    t = LIFE_EXPECTANCY[method][age]
    annual_payment = bal*(i*(1+i)**t)/((1+i)**t-1)
    return annual_payment/12

def fixed_annuitization(age,bal,i):
    i=0.04
    age=50
    bal=100000
    print(([1 - MORTALITY[i_age] for i_age in range(age,age+26)]))




if __name__ == '__main__':
    print(fixed_ammortization(50,400e3,i=0.04)*12)
    fixed_annuitization(50,100e3,0.04)
##    print(cap_gains(82789,125,3))
