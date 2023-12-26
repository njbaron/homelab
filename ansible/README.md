# OS install and hardening

## My plan

1. Install proxmox and run post install scripts
   1. https://tteck.github.io/Proxmox/
      1. Post install script
      2. Proxmox VE Processor Microcode
      3. Ubuntu 22.04 VM
2. Deploy a new vm from the proxmox gui
3. Setup the host
   1. Update the host
   2. Enable QEMU guest agent
   3. Harden SSH
   4. Setup Unattended upgrade
      1. https://www.linuxcapable.com/how-to-configure-unattended-upgrades-on-ubuntu-linux/
      2. https://wiki.debian.org/UnattendedUpgrades
   5. Setup Uncomplicated Firewall
      1. https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04
      2. https://docs.ansible.com/ansible/latest/collections/community/general/ufw_module.html
   6. Setup Crowdsec
      1. https://docs.crowdsec.net/docs/getting_started/install_crowdsec/
      2. https://github.com/alf149/ansible-role-crowdsec
   7. Install Docker
4. Deploy Docker Apps
   1. ...


# Things that I used as research for this plan.

## Crowdsec
https://www.crowdsec.net/blog/tutorial-crowdsec-v1-1

## Maybe to deploy VMs we might play with Terraform and Packer
https://www.youtube.com/watch?v=1nf3WOEFq1Y
https://www.youtube.com/watch?v=dvyeoDBUtsU

## Harden ssh
https://www.digitalocean.com/community/tutorials/how-to-harden-openssh-on-ubuntu-20-04

## How to protect Linux from Hackers // My server security strategy!
https://www.youtube.com/watch?v=Bx_HkLVBz9M

### Auto upgrade

1. Unattended upgrade
   - os upgrade package

2. Watchtower
   - automatic upgrade of docker

### Ssh Hardening

1. set a strong password or use a ssh key
2. edit sshd_config
    - Remove root log in
    - remove password login
3. Teleport?

### Network security

1. use a firewall - "uncomplicated firewall"
    - Does not apply by default to docker containers

### Reverse proxy

1. Use a reverse proxy to protect most web apps
2. nginx proxy manager
3. traefik

### Use a vpn to access some things

1. tailscale, wiregaurd, openvpn
2. dmz?

### Intrusion Prevention System (IPS)

1. fail to ban
2. crowdsec

### Application isolation

1. Apparmor - for non-docker apps
2. docker

## Self-Hosting Security Guide for your HomeLab
https://www.youtube.com/watch?v=Cs8yOmTJNYQ

### Alternate options
1. Self hosted VPN - Only allows people with vpn access to get to the machine.
2. Dont host it at home - Host it in the cloud

### Overview
1. Ensure all machines firmware and hardware are up to date
   1. Motherboard
   2. os
   3. firewall
   4. os

2. virtual or bare metal?
   1. ensure that everything will be updated

3. Ensure you are using a supported os
   1. supported and not EOL
   2. least privileges possible
   3. application firewall

4. Containers
   1. make sure the contrainer engine is up to date
   2. use official sourced containers
   3. make sure to use the minimal image container
   4. tag pinning. latest? or pin to a version? watchtower

5. Networking
   1. Segment your network is a must
      1. subnetting/vlan
      2. isolate trusted devices from possibly compromised devices
      3. iot device isolation
   2. external network
      1. How users and deviced enter the network
      2. only use the ports that you must need
      3. reverse proxy
      4. use a reverse proxy before traffic even enters the home. Cloudflare proxy
         1. dynamic dns to cloudflare
         2. only allow requests forwarded from cloudflare through your firewall
   3. firewall rules
      1. Block certain countries

6. Intrusion Prevention/Detection systems
   1. Use them regardless on the firewall

7. Internal reverse proxy
   1. easy way to redirect external network to the server
   2. allows for tls cert termination
   3. Traefik
      1. middleware and authentication with 2fa
      2. authalea/authentik/keycloak

8. Side quest - tunneling

## 10 Tips for Hardening your Linux Servers
https://www.youtube.com/watch?v=Jnxx_IAC0G4

1.  02:42  # Adjust your mindset
    - Dont expect that you can create something that is unhackable. Be ready for anything at all times.
2. 04:59  #   Number 2 : Patch your servers (and no excuses)
3. 07:59  #   Number 3 : Strengthen your passwords
4. 09:10  #   Number 4 : Don't open services to the public internet (unless you have no other choice)
5. 11:32  #   Number 5 : Lock down SSH
   1. Remove password auth
   2. lockdown ip addresses that can be used
   3. better keys
6. 13:41  #   Number 6 : Implement as many as layers of security as possible
   1. Fail2ban
   2. firewall
   3. lockdown ssh
7. 15:12  #   Number 7 : Implement reliable backups that are fully tested
   1. Tested backups
   2. 3 different places
      1. 1 of which is off site
   3. Test the restores
8. 16:57  #   Number 8 : Take advantage of monitoring tools
   1. nagios and zebb? graphana?
   2. login notifications
9.  18:41  #   Number 9 : Consider a third party security audit 
    1.  Expensive. but maybe there is an automated way to do it with a homelab?
10. 20:02  # Number 10 : Implement a business continuity plan

## The COMPLETE Linux Hardening, Privacy & Security Guide!
https://www.youtube.com/watch?v=Sa0KqbpLye4

### Zone 1
1. What distro
   1. fedora
   2. debian
   3. arch
2. Use a strong password
   1. avoid root login 
   2. use a password manager. strong and unique
3. encryption
   1. the entire disk
4. firewall
   1. use one
   2. ufw uncomplicated firewall
5. Use a vpn?
6. DNS use a private one
7. keep the install as minimal as possible
8. FOSS
9. Settings
   1.  Remove all permissions as you can.
10. auto update things

### Zone 2
1. Move to FOSS
2. ensure to use 2fa

### Zone 3
1. Isolate your applications
   1. apparmor or firejail
      1. sandbox different apps installed on the computer
   2. SELinux
2. Hardening
   1. basic - https://linuxhint.com/linux_security_hardening_checklist/
   2. advanced - https://github.com/shaurya-007/NSA-Linux-Hardening-docs
3. 