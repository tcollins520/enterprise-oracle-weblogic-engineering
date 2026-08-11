# ============================================================
# Create WebLogic 14.1.1 Domain: tinacloud
# ============================================================

selectTemplate('Basic WebLogic Server Domain')
loadTemplates()

setOption('DomainName', 'tinacloud')
setOption('OverwriteDomain', 'true')

# AdminServer
cd('/Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', 7001)

# Admin credentials
cd('/Security/base_domain/User/weblogic')
cmo.setPassword('Welcome1!')

# Machine + Node Manager
cd('/')
create('tinacloudMachine', 'Machine')
cd('/Machines/tinacloudMachine')
create('tinacloudMachine', 'NodeManager')
cd('/Machines/tinacloudMachine/NodeManager/tinacloudMachine')
set('ListenAddress', '10.20.2.199')
set('ListenPort', 5556)
set('NMType', 'SSL')

# Managed Server
cd('/')
create('tinacloudMS1', 'Server')
cd('/Servers/tinacloudMS1')
set('ListenAddress', '')
set('ListenPort', 8001)
set('Machine', 'tinacloudMachine')

# ServerStart block (required)
cd('/Servers/tinacloudMS1')
create('tinacloudMS1', 'ServerStart')

cd('/Servers/tinacloudMS1/ServerStart/tinacloudMS1')
set('Arguments', '-Xms256m -Xmx512m')

# Write domain
writeDomain('/u01/app/oracle/config/domains/tinacloud')
closeTemplate()

print('Domain tinacloud created successfully.')
