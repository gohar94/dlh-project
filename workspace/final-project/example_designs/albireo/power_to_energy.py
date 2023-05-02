import math


# Powers of 10
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
print("CONSTANTS:")
alexnet_macs          = 834600961
print(f"{'alexnet_macs':<25} {prefix(alexnet_macs):>11}")
total_energy_joules   = 2.90 * MILLI
print(f"{'total_energy_joules':<25} {prefix(total_energy_joules):>10}J")
total_latency_seconds = 0.13 * MILLI 
print(f"{'total_latency_seconds':<25} {prefix(total_latency_seconds):>10}s")
mrr_power_percent     = 0.331
print(f"{'mrr_power_percent':<25} {mrr_power_percent * 100:>10}%")
mzm_power_percent     = 0.152
print(f"{'mzm_power_percent':<25} {mzm_power_percent * 100:>10}%")
num_mrrs              = 2 * 9 * 5
print(f"{'num_mrrs':<25} {num_mrrs:>11}")
num_mzms              = 9
print(f"{'num_mzms':<25} {num_mzms:>11}")


# Derived values
print("\nDERIVED:")
energy_per_mac = total_energy_joules / alexnet_macs
print(f"{'energy_per_mac':<25} {prefix(energy_per_mac):>10}J")
energy_all_mrrs = energy_per_mac * mrr_power_percent
print(f"{'energy_all_mrrs':<25} {prefix(energy_all_mrrs):>10}J")
energy_per_mrr = energy_all_mrrs / num_mrrs
print(f"{'energy_per_mrr':<25} {prefix(energy_per_mrr):>10}J")
energy_all_mzms = energy_per_mac * mzm_power_percent
print(f"{'energy_all_mzms':<25} {prefix(energy_all_mzms):>10}J")
energy_per_mzm = energy_all_mzms / num_mzms
print(f"{'energy_per_mzm':<25} {prefix(energy_per_mzm):>10}J")
total_power_watts = total_energy_joules / total_latency_seconds
print(f"{'total_power_watts':<25} {prefix(total_power_watts):>10}W")
