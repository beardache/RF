#!/usr/bin/python

import rflib
import bitstring

prefix = '00000000000000'
key = '1101010101000101010101000'

pwm_key = ''.join(['110' if b == '1' else '100' for b in key])
full_pwm = '{}{}'.format(prefix, pwm_key)

print('Sending full PWM key: {}'.format(full_pwm))
print('hex: {}').format(bitstring.BitArray(bin=full_pwm))

rf_data = bitstring.BitArray(bin=full_pwm).tobytes()

d = rflib.RfCat()
d.setMdmModulation(rflib.MOD_ASK_OOK)
d.makePktFLEN(len(rf_data))
d.setMdmDRate(4800)
d.setMdmSyncMode(0)
d.setFreq(433508967)

d.RFxmit(rf_data, repeat=5)
d.setModeIDLE()
