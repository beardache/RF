#!/usr/bin/python

import rflib
import bitstring
import time

prefix = "000000000000000000000000000000000"
pwm_key = "100000000101000010000101000010101000010100001010000100001010100001000010100001010100001000010101000010100001010000101000010000101000010100001010000101010000101000010000101010000100001010100001000010100001010100001010000101000010100001"


full_pwm = '{}{}'.format(prefix, pwm_key)

rf_data = bitstring.BitArray(bin=full_pwm).tobytes()

d = rflib.RfCat()
d.setMdmModulation(rflib.MOD_ASK_OOK)
d.setFreq(433919678)
d.setMdmDRate(3600)
d.makePktFLEN(len(rf_data))

for i in range(10):
	d.RFxmit(rf_data, repeat=19)
	time.sleep(1)
d.setModeIDLE()
