package com.svenvandam.hbase.grpc.service

import akka.NotUsed
import akka.stream.scaladsl.Source
import com.svenvandam.hbase.grpc.model.ProtoOps
import com.svenvandam.hbase.grpc.proto._
import com.svenvandam.hbase.grpc.repository.HBaseRepository
import com.typesafe.scalalogging.LazyLogging
import scala.collection.convert.AsScalaConverters
import org.apache.hadoop.hbase.client.{Result => JResult}

class HBaseServiceImpl(hBaseRepository: HBaseRepository)
    extends HBaseService
    with AsScalaConverters
    with LazyLogging {
  implicit val ec = hBaseRepository.ec

  override def get(get: Get): Source[Cell, NotUsed] = get.table match {
    case Some(table) =>
      Source
        .future(hBaseRepository.get(ProtoOps.getToJava(get), table))
        .flatMapConcat(resultToSource)

    case None =>
      Source.failed(new IllegalArgumentException("No table supplied"))
  }

  override def scan(scan: Scan): Source[Cell, NotUsed] =
    scan.table match {
      case Some(table) =>
        Source
          .future(hBaseRepository.scan(ProtoOps.scanToJava(scan), table))
          .flatMapConcat { scanner =>
            val it: Iterator[JResult] = asScala(scanner.iterator())
            Source.fromIterator(() => it)
          }
          .flatMapConcat(resultToSource)

      case None =>
        Source.failed(new IllegalArgumentException("No table supplied"))
    }

  private def resultToSource(result: JResult): Source[Cell, NotUsed] = {
    Source
      .fromIterator(() => result.rawCells().iterator)
      .map(ProtoOps.cellToProto)
  }
}
