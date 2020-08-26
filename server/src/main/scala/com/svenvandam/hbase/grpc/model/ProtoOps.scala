package com.svenvandam.hbase.grpc.model

import com.google.protobuf.ByteString
import com.svenvandam.hbase.grpc.proto._
import org.apache.hadoop.hbase.client.{Get => JGet, Put => JPut, Delete => JDelete, Result => JResult, Scan => JScan}
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.hbase.{CellUtil, Cell => JCell}

object ProtoOps {
  def getToJava(protoGet: GetRequest): JGet = {
    val get = new JGet(Bytes.toBytes(protoGet.row))

    protoGet.maxVersions.foreach(get.readVersions)

    (protoGet.minTime, protoGet.maxTime) match {
      case (Some(min), Some(max)) => get.setTimeRange(min, max)
      case (None, Some(max))      => get.setTimestamp(max)
      case _                      =>
    }

    protoGet.columns.foreach {
      case Family(f)                 => get.addFamily(Bytes.toBytes(f))
      case Column(family, qualifier) => get.addColumn(Bytes.toBytes(family), Bytes.toBytes(qualifier))
      case ColumnQuery.Empty         =>
    }

    get
  }

  def scanToJava(protoScan: ScanRequest): JScan = {
    val scan = new JScan()
    protoScan.startRow.foreach(s => scan.withStartRow(Bytes.toBytes(s)))
    protoScan.stopRow.foreach(s => scan.withStopRow(Bytes.toBytes(s)))
    protoScan.prefix.foreach(s => scan.setRowPrefixFilter(Bytes.toBytes(s)))
    protoScan.maxVersions.foreach(scan.readVersions)

    (protoScan.minTime, protoScan.maxTime) match {
      case (Some(min), Some(max)) => scan.setTimeRange(min, max)
      case (None, Some(max))      => scan.setTimestamp(max)
      case _                      =>
    }

    protoScan.columns.foreach {
      case Family(f)                 => scan.addFamily(Bytes.toBytes(f))
      case Column(family, qualifier) => scan.addColumn(Bytes.toBytes(family), Bytes.toBytes(qualifier))
      case ColumnQuery.Empty         =>
    }

    scan
  }

  def putToJava(protoPut: PutRequest): JPut = {
    val put = new JPut(Bytes.toBytes(protoPut.row))
    for {
      ColumnValues(col, vals)         <- protoPut.values
      Column(family, qualifier) <- col
      value                     <- vals
    } value match {
      case ValueVersion(v, Some(t)) =>
        put.addColumn(
          Bytes.toBytes(family),
          Bytes.toBytes(qualifier),
          t,
          v.toByteArray
        )
      case ValueVersion(v, None) =>
        put.addColumn(
          Bytes.toBytes(family),
          Bytes.toBytes(qualifier),
          v.toByteArray
        )
    }

    put
  }

  def deleteToJava(protoDelete: DeleteRequest): JDelete = {
    val delete = new JDelete(Bytes.toBytes(protoDelete.row))

    val (addLatest, addVersioned): ((Array[Byte], Array[Byte]) => JDelete, (Array[Byte], Array[Byte], Long) => JDelete) =
      if (protoDelete.singleVersion) {
        (delete.addColumn(_, _), delete.addColumn(_, _, _))
      } else {
        (delete.addColumns(_, _), delete.addColumns(_, _, _))
      }

    for {
      colVersion <- protoDelete.columns
      col        <- colVersion.column
    } colVersion.timestamp match {
      case Some(t) => addVersioned(Bytes.toBytes(col.family), Bytes.toBytes(col.qualifier), t)
      case None    => addLatest(Bytes.toBytes(col.family), Bytes.toBytes(col.qualifier))
    }

    delete
  }

  def resultToProto(jResult: JResult, includeTimestamp: Boolean): Result = {
    val columns = jResult
      .rawCells()
      .groupBy { cell =>
        (Bytes.toString(CellUtil.cloneFamily(cell)), Bytes.toString(CellUtil.cloneQualifier(cell)))
      }
      .toSeq
      .map {
        case ((family, qualifier), cells) =>
          ColumnValues(
            Some(Column(family, qualifier)),
            cells.map(cellToValueVersion(_, includeTimestamp))
          )
      }

    Result(
      Bytes.toString(jResult.getRow),
      columns
    )
  }

  private def cellToValueVersion(cell: JCell, includeTimestamp: Boolean): ValueVersion =
    ValueVersion(
      ByteString.copyFrom(CellUtil.cloneValue(cell)),
      if (includeTimestamp) Some(cell.getTimestamp) else None
    )
}
