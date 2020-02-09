package com.svenvandam.hbase.grpc.model

import com.google.protobuf.ByteString
import com.svenvandam.hbase.grpc.proto._
import org.apache.hadoop.hbase.client.{Get => JGet, Scan => JScan}
import org.apache.hadoop.hbase.{Cell => JCell}
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.hbase.CellUtil

object ProtoOps {
  def getToJava(protoGet: Get): JGet = {
    val get = new JGet(Bytes.toBytes(protoGet.row))

    protoGet.maxVersions.foreach(get.readVersions)

    (protoGet.minTime, protoGet.maxTime) match {
      case (Some(min), Some(max)) => get.setTimeRange(min, max)
      case (None, Some(max))      => get.setTimestamp(max)
      case _                      => get
    }

    protoGet.columns.foreach {
      case (family, cols) =>
        if (cols.columns.isEmpty) get.addFamily(Bytes.toBytes(family))
        else
          cols.columns.foreach(
            qualifier =>
              get.addColumn(Bytes.toBytes(family), Bytes.toBytes(qualifier))
          )
    }

    get
  }

  def scanToJava(protoScan: Scan): JScan = {
    val scan = new JScan()
    protoScan.startRow.foreach(s => scan.withStartRow(Bytes.toBytes(s)))
    protoScan.stopRow.foreach(s => scan.withStopRow(Bytes.toBytes(s)))
    protoScan.prefix.foreach(s => scan.setRowPrefixFilter(Bytes.toBytes(s)))
    protoScan.maxVersions.foreach(scan.readVersions)

    (protoScan.minTime, protoScan.maxTime) match {
      case (Some(min), Some(max)) => scan.setTimeRange(min, max)
      case (None, Some(max))      => scan.setTimestamp(max)
      case _                      => scan
    }

    protoScan.columns.foreach {
      case (family, cols) =>
        if (cols.columns.isEmpty) scan.addFamily(Bytes.toBytes(family))
        else
          cols.columns.foreach { qualifier =>
            scan.addColumn(Bytes.toBytes(family), Bytes.toBytes(qualifier))
          }
    }
    scan
  }

  def cellToProto(javaCell: JCell): Cell =
    Cell(
      Bytes.toString(CellUtil.cloneRow(javaCell)),
      Bytes.toString(CellUtil.cloneFamily(javaCell)),
      Bytes.toString(CellUtil.cloneQualifier(javaCell)),
      javaCell.getTimestamp,
      ByteString.copyFrom(CellUtil.cloneValue(javaCell))
    )
}
