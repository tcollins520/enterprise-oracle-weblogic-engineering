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

[oracle@ip-10-20-2-199 scripts]$ cat create_tinacloud_jdbc_final.py
# ============================================================
# V2 Enterprise Oracle/WebLogic Engineering
# EnterpriseMiddlewareDS
# WebLogic Server 14.1.1
# Oracle Database 12.2.0.1
# ============================================================

connect('weblogic','Welcome1!','t3://10.20.2.199:7001')

# ------------------------------------------------------------
# Clear any incomplete edit session from previous attempt
# ------------------------------------------------------------

edit()

try:
    cancelEdit('y')
    print 'Previous incomplete edit session cancelled.'
except:
    print 'No previous edit session to cancel.'

# ------------------------------------------------------------
# Start clean edit session
# ------------------------------------------------------------

edit()
startEdit()

print '============================================================'
print 'Creating EnterpriseMiddlewareDS'
print '============================================================'

# ------------------------------------------------------------
# Create JDBC System Resource
# ------------------------------------------------------------

cd('/')

ds = create('EnterpriseMiddlewareDS', 'JDBCSystemResource')

jdbc = ds.getJDBCResource()
jdbc.setName('EnterpriseMiddlewareDS')
jdbc.setDatasourceType('GENERIC')

# ------------------------------------------------------------
# Oracle JDBC Driver
# ------------------------------------------------------------

driver = jdbc.getJDBCDriverParams()

driver.setDriverName('oracle.jdbc.OracleDriver')
driver.setUrl(
    'jdbc:oracle:thin:@//10.20.2.147:1521/tinacloud12c'
)
driver.setPassword('Welcome1!')

# Disable XA
driver.setUseXaDataSourceInterface(false)

# ------------------------------------------------------------
# Database User
# ------------------------------------------------------------

properties = driver.getProperties()

userProperty = properties.createProperty('user')
userProperty.setValue('APP_USER')

print 'Oracle JDBC credentials configured.'

# ------------------------------------------------------------
# Connection Pool
# ------------------------------------------------------------

pool = jdbc.getJDBCConnectionPoolParams()

pool.setInitialCapacity(1)
pool.setMinCapacity(1)
pool.setMaxCapacity(10)

print 'Connection pool configured.'

# ------------------------------------------------------------
# JNDI / Transaction Configuration
# ------------------------------------------------------------

dataSourceParams = jdbc.getJDBCDataSourceParams()

dataSourceParams.setJNDINames(
    jarray.array(
        ['jdbc/EnterpriseMiddlewareDS'],
        String
    )
)

dataSourceParams.setGlobalTransactionsProtocol('None')

print 'JNDI configured: jdbc/EnterpriseMiddlewareDS'

# ------------------------------------------------------------
# Target Managed Server
# ------------------------------------------------------------

target = getMBean('/Servers/tinacloudMS1')

ds.addTarget(target)

print 'Target configured: tinacloudMS1'

# ------------------------------------------------------------
# Save
# ------------------------------------------------------------

print '============================================================'
print 'Saving configuration...'
print '============================================================'

save()

# ------------------------------------------------------------
# Activate
# ------------------------------------------------------------

print '============================================================'
print 'Activating configuration...'
print '============================================================'

activate()

print '============================================================'
print 'SUCCESS'
print '============================================================'
print 'Data Source : EnterpriseMiddlewareDS'
print 'JNDI        : jdbc/EnterpriseMiddlewareDS'
print 'Database    : 10.20.2.147:1521/tinacloud12c'
print 'User        : APP_USER'
print 'Target      : tinacloudMS1'
print '============================================================'

disconnect()
exit()
