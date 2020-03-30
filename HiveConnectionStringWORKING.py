
import pyodbc

strFileDSNAsAstring = "DRIVER=Cloudera ODBC Driver for Apache Hive;USEUNICODESQLCHARACTERTYPES=1; \
SSL=0;SERVICEPRINCIPALCANONICALIZATION=0;SERVICEDISCOVERYMODE=0;SCHEMA=database;PORT=port; \
KRBSERVICENAME=hive;KRBREALM=uppercaserealm;KRBHOSTFQDN=fqdnhost;INVALIDSESSIONAUTORECOVER=1; \
HOST=host;HIVESERVERTYPE=2;GETTABLESWITHQUERY=0;ENABLETEMPTABLE=0;DESCRIPTION=Hive; \
DELEGATEKRBCREDS=0;AUTHMECH=1;ASYNCEXECPOLLINTERVAL=100;APPLYSSPWITHQUERIES=1;CAIssuedCertNamesMismatch=1;"

try:
  pyodbc.pooling = False
  conn = pyodbc.connect(strFileDSNAsAstring, autocommit=True)
except:
  print("failure.")
else:
  conn.close()
  print("success.")    
