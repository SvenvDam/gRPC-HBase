package com.svenvandam.hbase.grpc.config

import com.typesafe.config.ConfigFactory

case class ApplicationConfig(hBase: HBaseConfig, http: HttpConfig)

case class HBaseConfig(zookeeperHost: String,
                       zookeeperPort: Int,
                       zNodeParent: String,
                       requestParallelism: Int,
                       kerberos: Option[KerberosConfig])

case class KerberosConfig(
    keytab: String,
    principal: String,
    regionServerKerberosPrincipal: String = "hbase/_HOST@PRD.KLM.COM",
    masterKerberosPrincipal: String = "hbase/_HOST@PRD.KLM.COM"
)

case class HttpConfig(host: String, port: Int)

object ApplicationConfig {
  def load(): ApplicationConfig = {
    val config = ConfigFactory.load()

    val kerberosConfig = if (config.hasPath("kerberos")) {
      Some(
        KerberosConfig(
          config.getString("kerberos.keytab"),
          config.getString("kerberos.principal")
        )
      )
    } else {
      None
    }

    ApplicationConfig(
      HBaseConfig(
        config.getString("hbase.zookeeper-host"),
        config.getInt("hbase.zookeeper-port"),
        config.getString("hbase.znode-parent"),
        config.getInt("hbase.request-paralellism"),
        kerberosConfig
      ),
      HttpConfig(config.getString("http.host"), config.getInt("http.port"))
    )
  }
}
