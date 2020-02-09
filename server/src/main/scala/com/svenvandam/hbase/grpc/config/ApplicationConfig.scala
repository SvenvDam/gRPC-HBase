package com.svenvandam.hbase.grpc.config

import com.typesafe.config.ConfigFactory

case class ApplicationConfig(
    hBase: HBaseConfig,
    http: HttpConfig
)

case class HBaseConfig(
    zookeeperHost: String,
    zookeeperPort: Int,
    zNodeParent: String,
    requestParallelism: Int
)

case class HttpConfig(
  host: String,
    port: Int
)

object ApplicationConfig {
  def load(): ApplicationConfig = {
    val config = ConfigFactory.load()

    ApplicationConfig(
      HBaseConfig(
        config.getString("hbase.zookeeper-host"),
        config.getInt("hbase.zookeeper-port"),
        config.getString("hbase.znode-parent"),
        config.getInt("hbase.request-paralellism")
      ),
      HttpConfig(
        config.getString("http.host"),
        config.getInt("http.port")
      )
    )
  }
}