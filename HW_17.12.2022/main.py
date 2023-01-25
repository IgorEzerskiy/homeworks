# -*- coding: utf-8 -*-
# initializing empty envelops
sum = 0

necessityEnvelop = 0
freedomEnvelop = 0
educationEnvelop = 0
longTermEnvelop = 0
playEnvelop = 0
giveEnvelop = 0

necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

expectedIncome = 1000

print("""Hello.\n
We gonna fill your envelopes by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press CTRL+C to exit script.\n""")


while (sum < expectedIncome):
    line = int(input("\n Enter the amount, please: "))
    sum += line
    necessityEnvelop += line*necRate
    freedomEnvelop += line*ffaRate
    educationEnvelop += line*eduRate
    longTermEnvelop += line*ltssRate
    playEnvelop += line*playRate
    giveEnvelop += line*giveRate

print(f"""At the end we have:\n
      Necessity Envelop has: {int(necessityEnvelop)}\n
      Financial Freedom Envelop has: {int(freedomEnvelop)}\n
      Education Envelop: {int(educationEnvelop)}\n
      Long Term Saving for Spending Envelop has: {int(longTermEnvelop)}\n
      Play Envelop has: {int(playEnvelop)}\n
      Give Envelop has: {int(giveEnvelop)}\n
      +---------------Thanks for using our software----------------+\n""")
