package com.svenvandam.hbase.grpc

import com.svenvandam.hbase.grpc.config.HBaseConfig
import org.apache.hadoop.hbase.{TableName, HBaseConfiguration}
import org.apache.hadoop.hbase.HConstants.HBASE_CLIENT_RETRIES_NUMBER
import org.apache.hadoop.hbase.client.{Connection, Table, ConnectionFactory}
import org.apache.hadoop.security.UserGroupInformation

object HBase {

  def getConnection(appConf: HBaseConfig): Connection = {
    val conf = HBaseConfiguration.create()

    appConf.kerberos.foreach { kerberosConfig =>
      conf.set("hbase.security.authentication", "kerberos")
      conf.set("hadoop.security.authentication", "kerberos")
      conf.set("hbase.rpc.protection", "authentication")
      conf.set("hbase.cluster.distributed", "true")
      conf.set("hbase.regionserver.kerberos.principal", kerberosConfig.regionServerKerberosPrincipal)
      conf.set("hbase.master.kerberos.principal", kerberosConfig.masterKerberosPrincipal)
      UserGroupInformation.setConfiguration(conf)
      UserGroupInformation
        .loginUserFromKeytab(
          kerberosConfig.principal,
          kerberosConfig.keytab
        )
    }
    conf.setInt("hbase.zookeeper.property.clientPort", appConf.zookeeperPort)
    conf.set("hbase.zookeeper.quorum", appConf.zookeeperHost)
    conf.set("zookeeper.znode.parent", appConf.zNodeParent)
    conf.setInt(HBASE_CLIENT_RETRIES_NUMBER, 2)
    conf.setInt("hbase.client.serverside.retries.multiplier", 2)
    ConnectionFactory.createConnection(conf)
  }

  def openTable(namespace: String, tableName: String, conn: Connection): Table =
    conn.getTable(TableName.valueOf(namespace, tableName))

  def withTable[T](tableName: String, namespace: String = "default")(f: Table => T)(implicit conn: Connection): T = {
    val table = openTable(namespace, tableName, conn)
    try {
      f(table)
    } finally {
      table.close()
    }
  }
}
