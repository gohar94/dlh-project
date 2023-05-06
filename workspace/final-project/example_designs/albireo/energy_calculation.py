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


# Constants
alexnet_macs                = 834600961
total_energy_joules         = 2.90 * MILLI
total_latency_seconds       = 0.13 * MILLI 
mrr_power_percent           = 0.331
mzm_power_percent           = 0.152
weight_caches_power_percent = 0.0013
num_mrrs                    = 2 * 9 * 5
num_mzms                    = 9
num_weight_caches           = 9
TIA_power_percent           = 0.0062
ADC_power_percent           = 0.058
DAC_power_percent           = 0.349
num_TIA                     = 45
num_ADC                     = 9
num_DAC                     = 1


print("CONSTANTS:")
print(f"{'alexnet_macs':<25} {prefix(alexnet_macs):>11}")
print(f"{'total_energy_joules':<25} {prefix(total_energy_joules):>10}J")
print(f"{'total_latency_seconds':<25} {prefix(total_latency_seconds):>10}s")
print(f"{'mrr_power_percent':<25} {mrr_power_percent * 100:>10}%")
print(f"{'mzm_power_percent':<25} {mzm_power_percent * 100:>10}%")
print(f"{'weight_caches_power_percent':<25} {weight_caches_power_percent * 100:>8}%")
print(f"{'num_mrrs':<25} {num_mrrs:>11}")
print(f"{'num_mzms':<25} {num_mzms:>11}")
print(f"{'num_weight_caches':<25} {num_weight_caches:>11}")
print(f"{'TIA_power_percent':<25} {TIA_power_percent * 100:>10}%")
print(f"{'ADC_power_percent':<25} {ADC_power_percent * 100:>10}%")
print(f"{'DAC_power_percent':<25} {DAC_power_percent * 100:>10}%")
print(f"{'num_TIA':<25} {num_TIA:>11}")
print(f"{'num_ADC':<25} {num_ADC:>11}")


# Derived values
energy_per_compute       = total_energy_joules / alexnet_macs
total_power_watts        = total_energy_joules / total_latency_seconds

energy_all_mrrs          = energy_per_compute * mrr_power_percent
energy_all_mzms          = energy_per_compute * mzm_power_percent
energy_all_weight_caches = energy_per_compute * weight_caches_power_percent
energy_all_TIAs          = energy_per_compute * TIA_power_percent
energy_all_ADC           = energy_per_compute * ADC_power_percent
energy_all_DAC           = energy_per_compute * DAC_power_percent

energy_per_mrr           = energy_all_mrrs / num_mrrs
energy_per_mzm           = energy_all_mzms / num_mzms
energy_per_weight_cache  = energy_all_weight_caches / num_weight_caches
energy_per_TIA           = energy_all_TIAs / num_TIA
energy_per_ADC           = energy_all_ADC / num_ADC
energy_per_DAC           = energy_all_DAC / num_DAC


print("\nDERIVED:")
print(f"{'energy_per_compute':<25} {prefix(energy_per_compute):>10}J")
print(f"{'energy_all_mrrs':<25} {prefix(energy_all_mrrs):>10}J")
print(f"{'energy_per_mrr':<25} {prefix(energy_per_mrr):>10}J")
print(f"{'energy_all_mzms':<25} {prefix(energy_all_mzms):>10}J")
print(f"{'energy_per_mzm':<25} {prefix(energy_per_mzm):>10}J")
print(f"{'energy_all_weight_caches':<25} {prefix(energy_all_weight_caches):>10}J")
print(f"{'energy_per_weight_cache':<25} {prefix(energy_per_weight_cache):>10}J")
print(f"{'energy_all_TIAs':<25} {prefix(energy_all_TIAs):>10}J")
print(f"{'energy_per_TIAs':<25} {prefix(energy_per_TIA):>10}J")
print(f"{'energy_all_ADC':<25} {prefix(energy_all_ADC):>10}J")
print(f"{'energy_per_ADC':<25} {prefix(energy_per_ADC):>10}J")
print(f"{'energy_all_DAC':<25} {prefix(energy_all_DAC):>10}J")
print(f"{'energy_per_DAC':<25} {prefix(energy_per_DAC):>10}J")
print(f"{'total_power_watts':<25} {prefix(total_power_watts):>10}W")


def percent_to_decimal(x):
    return x/100

def area_to_base(area, units):
    return area * (units * units)


total_albireo_area = area_to_base(124.66, MILLI)

mzi_area = total_albireo_area * percent_to_decimal(3.7)
dac_area = total_albireo_area * percent_to_decimal(0.03)
adc_area = total_albireo_area * percent_to_decimal(0.4)
mrr_area = total_albireo_area * percent_to_decimal(0.8)

print()
print("MZI area in mm^2: {:.4f}".format(area_to_base(mzi_area, 1/MILLI)))
print("DAC area in mm^2: {:.4f}".format(area_to_base(dac_area, 1/MILLI)))
print("ADC area in mm^2: {:.4f}".format(area_to_base(adc_area, 1/MILLI)))
print("MRR area in mm^2: {:.4f}".format(area_to_base(mrr_area, 1/MILLI)))
print()

print()
print("MZI area in um^2: {:.4f}".format(area_to_base(mzi_area, 1/MICRO)))
print("DAC area in um^2: {:.4f}".format(area_to_base(dac_area, 1/MICRO)))
print("ADC area in um^2: {:.4f}".format(area_to_base(adc_area, 1/MICRO)))
print("MRR area in um^2: {:.4f}".format(area_to_base(mrr_area, 1/MICRO)))
print()