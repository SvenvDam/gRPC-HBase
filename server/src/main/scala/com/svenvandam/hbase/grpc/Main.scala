package com.svenvandam.hbase.grpc

import java.util.concurrent.Executors
import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.stream.ActorMaterializer
import com.svenvandam.hbase.grpc.config.ApplicationConfig
import com.svenvandam.hbase.grpc.proto.HBaseServiceHandler
import com.svenvandam.hbase.grpc.repository.HBaseRepository
import com.svenvandam.hbase.grpc.service.HBaseServiceImpl
import scala.concurrent.ExecutionContext

object Main {
  def main(args: Array[String]): Unit = {

    val appConf = ApplicationConfig.load()

    val hbaseExecutionContext =
      ExecutionContext
        .fromExecutor(
          Executors
            .newFixedThreadPool(appConf.hBase.requestParallelism)
        )

    val hBaseConn = HBase.getConnection(appConf.hBase)

    val hBaseRepository = new HBaseRepository(hBaseConn, hbaseExecutionContext)

    implicit val system = ActorSystem("HBase-gRPC-server")
    implicit val mat = ActorMaterializer()

    val service = HBaseServiceHandler(new HBaseServiceImpl(hBaseRepository))

    Http().bindAndHandleAsync(
      service,
      appConf.http.host,
      appConf.http.port
    )

  }
}
