from raw_data import raw_target_ips  # -> Ham veriler
from raw_data import safe_ips  # -> Sunucu IP



unique_targets = set(raw_target_ips)

final_targets = unique_targets.difference(safe_ips)

print(len(raw_target_ips))
print(len(unique_targets))
print(final_targets)