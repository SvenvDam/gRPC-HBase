package com.svenvandam.hbase.grpc.service

import akka.NotUsed
import akka.stream.Materializer
import akka.stream.scaladsl.Source
import com.svenvandam.hbase.grpc.model.ProtoOps
import com.svenvandam.hbase.grpc.proto._
import com.svenvandam.hbase.grpc.repository.HBaseRepository
import com.typesafe.scalalogging.LazyLogging
import scala.collection.convert.AsScalaConverters
import org.apache.hadoop.hbase.client.{Result => JResult}
import scala.concurrent.Future

class HBaseServiceImpl(hBaseRepository: HBaseRepository)(implicit mat: Materializer)
    extends HBaseService
    with AsScalaConverters
    with LazyLogging {
  implicit val ec = hBaseRepository.ec

  private val noTableError = new IllegalArgumentException("No table supplied!")

  override def get(get: GetRequest): Future[Result] = get.table match {
    case Some(table) =>
      hBaseRepository
        .get(ProtoOps.getToJava(get), table)
        .map(ProtoOps.resultToProto(_, get.includeTimestamp))

    case None =>
      Future.failed(noTableError)
  }

  override def scan(scan: ScanRequest): Source[Result, NotUsed] =
    scan.table match {
      case Some(table) =>
        Source
          .future(hBaseRepository.scan(ProtoOps.scanToJava(scan), table))
          .flatMapConcat { scanner =>
            val it: Iterator[JResult] = asScala(scanner.iterator())
            Source.fromIterator(() => it)
          }
          .map(ProtoOps.resultToProto(_, scan.includeTimestamp))

      case None =>
        Source.failed(noTableError)
    }

  override def delete(delete: DeleteRequest): Future[OK] = delete.table match {
    case Some(table) => hBaseRepository
      .delete(ProtoOps.deleteToJava(delete), table)
      .map(_ => OK())

    case None => Future.failed(noTableError)
  }

  override def put(put: PutRequest): Future[OK] = put.table match {
    case Some(table) => hBaseRepository
      .put(ProtoOps.putToJava(put), table)
      .map(_ => OK())

    case None => Future.failed(noTableError)
  }
}
