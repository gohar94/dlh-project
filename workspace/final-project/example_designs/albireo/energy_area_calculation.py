import math


# Powers of 10
MICRO = 10**-6
MILLI = 10**-3
MEGA  = 10**6
GIGA  = 10**9


def sign(x, value=1):
    """Mathematical signum function.

    :param x: Object of investigation
    :param value: The size of the signum (defaults to 1)
    :returns: Plus or minus value

    Source: https://stackoverflow.com/a/29749228/3132415
    """
    return -value if x < 0 else value


def prefix(x, dimension=1):
    """Give the number an appropriate SI prefix.

    :param x: Too big or too small number.
    :returns: String containing a number between 1 and 1000 and SI prefix.

    Source: https://stackoverflow.com/a/29749228/3132415
    """
    if x == 0:
        return "0  "

    l = math.floor(math.log10(abs(x)))
    if abs(l) > 24:
        l = sign(l, value=24)

    div, mod = divmod(l, 3*dimension)
    return "%.3g %s" % (x * 10**(-l + mod), " kMGTPEZYyzafpnµm"[div])


def area_m_to_micro(x):
    """Given an area in m^2, convert it to um^2.
    """
    return x * 1000000000000


def percent_to_decimal(x):
    """Convert a percentage to decimal.
    """
    return x/100

# Constants
alexnet_macs                = 834600961
total_energy_joules         = 2.90 * MILLI
total_latency_seconds       = 0.13 * MILLI 
mrr_power_percent           = 0.331
mzm_power_percent           = 0.152
weight_caches_power_percent = 0.0013
num_plcg                    = 9
num_plcu                    = 3
num_mrr                    = num_plcg * num_plcu * 2 * 9 * 5
num_mzm                    = num_plcu * 9
num_weight_caches           = num_plcg * 1
TIA_power_percent           = 0.0062
ADC_power_percent           = 0.058
DAC_power_percent           = 0.349
num_TIA                     = 45
num_ADC                     = num_plcg * 1
num_DAC                     = 1
num_AWG                     = num_plcg
num_star_coupler            = num_plcg * num_plcu


print("Energy:")
print(f"{'alexnet_macs':<25} {prefix(alexnet_macs):>11}")
print(f"{'total_energy_joules':<25} {prefix(total_energy_joules):>10}J")
print(f"{'total_latency_seconds':<25} {prefix(total_latency_seconds):>10}s")
print(f"{'mrr_power_percent':<25} {mrr_power_percent * 100:>10}%")
print(f"{'mzm_power_percent':<25} {mzm_power_percent * 100:>10}%")
print(f"{'weight_caches_power_percent':<25} {weight_caches_power_percent * 100:>8}%")
print(f"{'num_mrr':<25} {num_mrr:>11}")
print(f"{'num_mzm':<25} {num_mzm:>11}")
print(f"{'num_weight_caches':<25} {num_weight_caches:>11}")
print(f"{'TIA_power_percent':<25} {TIA_power_percent * 100:>10}%")
print(f"{'ADC_power_percent':<25} {ADC_power_percent * 100:>10}%")
print(f"{'DAC_power_percent':<25} {DAC_power_percent * 100:>10}%")
print(f"{'num_TIA':<25} {num_TIA:>11}")
print(f"{'num_ADC':<25} {num_ADC:>11}")
print(f"{'num_AWG':<25} {num_AWG:>11}")
print(f"{'num_star_coupler':<25} {num_star_coupler:>11}")


# Derived values
energy_per_compute       = total_energy_joules / alexnet_macs
total_power_watts        = total_energy_joules / total_latency_seconds

energy_all_mrrs          = energy_per_compute * mrr_power_percent
energy_all_mzms          = energy_per_compute * mzm_power_percent
energy_all_weight_caches = energy_per_compute * weight_caches_power_percent
energy_all_TIAs          = energy_per_compute * TIA_power_percent
energy_all_ADC           = energy_per_compute * ADC_power_percent
energy_all_DAC           = energy_per_compute * DAC_power_percent

energy_per_mrr           = energy_all_mrrs / num_mrr
energy_per_mzm           = energy_all_mzms / num_mzm
energy_per_weight_cache  = energy_all_weight_caches / num_weight_caches
energy_per_TIA           = energy_all_TIAs / num_TIA
energy_per_ADC           = energy_all_ADC / num_ADC
energy_per_DAC           = energy_all_DAC / num_DAC


print("")
print(f"{'total_power_watts':<25} {prefix(total_power_watts):>10}W")
print(f"{'energy_all_mrrs':<25} {prefix(energy_all_mrrs):>10}J")
print(f"{'energy_all_mzms':<25} {prefix(energy_all_mzms):>10}J")
print(f"{'energy_all_weight_caches':<25} {prefix(energy_all_weight_caches):>10}J")
print(f"{'energy_all_TIAs':<25} {prefix(energy_all_TIAs):>10}J")
print(f"{'energy_all_ADC':<25} {prefix(energy_all_ADC):>10}J")
print(f"{'energy_all_DAC':<25} {prefix(energy_all_DAC):>10}J")

print()
print(f"{'energy_per_compute':<25} {prefix(energy_per_compute):>10}J")
print(f"{'energy_per_mrr':<25} {prefix(energy_per_mrr):>10}J")
print(f"{'energy_per_mzm':<25} {prefix(energy_per_mzm):>10}J")
print(f"{'energy_per_weight_cache':<25} {prefix(energy_per_weight_cache):>10}J")
print(f"{'energy_per_TIAs':<25} {prefix(energy_per_TIA):>10}J")
print(f"{'energy_per_ADC':<25} {prefix(energy_per_ADC):>10}J")
print(f"{'energy_per_DAC':<25} {prefix(energy_per_DAC):>10}J")


total_albireo_area_m2 = 124.66 * MILLI * MILLI
mzm_area              = total_albireo_area_m2 * percent_to_decimal(3.7)
dac_area              = total_albireo_area_m2 * percent_to_decimal(0.03)
adc_area              = total_albireo_area_m2 * percent_to_decimal(0.4)
mrr_area              = total_albireo_area_m2 * percent_to_decimal(0.8)
awg_area              = total_albireo_area_m2 * percent_to_decimal(72)
star_coupler_area     = total_albireo_area_m2 * percent_to_decimal(17)


print()
print("\nArea:")
print("Total area in um^2: {:.4f}".format(area_m_to_micro(total_albireo_area_m2)))
print("Total MZM area in um^2: {:.4f}".format(area_m_to_micro(mzm_area)))
print("Total DAC area in um^2: {:.4f}".format(area_m_to_micro(dac_area)))
print("Total ADC area in um^2: {:.4f}".format(area_m_to_micro(adc_area)))
print("Total MRR area in um^2: {:.4f}".format(area_m_to_micro(mrr_area)))
print("Total AWG area in um^2: {:.4f}".format(area_m_to_micro(awg_area)))
print("Total star coupler area in um^2: {:.4f}".format(area_m_to_micro(star_coupler_area)))


per_mzm_area          = mzm_area / num_mzm
per_mrr_area          = mrr_area / num_mrr
per_dac_area          = dac_area / num_DAC
per_adc_area          = adc_area / num_ADC
per_awg_area          = awg_area / num_AWG
per_star_coupler_area = star_coupler_area / num_star_coupler


print("")
print("Each MZM area in um^2: {:.4f}".format(area_m_to_micro(per_mzm_area)))
print("Each DAC area in um^2: {:.4f}".format(area_m_to_micro(per_dac_area)))
print("Each ADC area in um^2: {:.4f}".format(area_m_to_micro(per_adc_area)))
print("Each MRR area in um^2: {:.4f}".format(area_m_to_micro(per_mrr_area)))
print("Each AWG area in um^2: {:.4f}".format(area_m_to_micro(per_awg_area)))
print("Each star coupler area in um^2: {:.4f}".format(area_m_to_micro(per_star_coupler_area)))
print()
