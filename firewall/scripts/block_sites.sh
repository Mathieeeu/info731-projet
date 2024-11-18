#!/bin/bash
echo "Configuring firewall..."

# Permettre le trafic entrant et transféré des IP autorisées
while IFS= read -r ip; do
  iptables -A INPUT -s $ip -j ACCEPT
  iptables -A FORWARD -s $ip -j ACCEPT
done < allowed_ips.txt

# Bloquer les domaines spécifiques pour toutes les IP non autorisées
while IFS= read -r domain; do
  resolved_ip=$(dig +short "$domain" | head -n 1)
  echo "Blocking $domain ($resolved_ip)"
  if [ -n "$resolved_ip" ]; then
    iptables -A FORWARD -d "$resolved_ip" -j REJECT --reject-with icmp-host-prohibited
  fi
done < blocked_sites.txt

echo "Firewall configured."
